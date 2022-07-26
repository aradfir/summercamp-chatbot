import socket
import importlib
import concurrent.futures

HOST = "127.0.0.1"
PORT = 1043
MAX_WORKERS = 100
MAX_BUFFER_SIZE = 9999999999999999999
clients_data = dict()


def data_calc(arg_str: str):
    # remove last item (fin)
    # cast all items to float
    # find function to call from first two params
    # calculate and return
    arg_split = arg_str.split()
    try:
        module = importlib.import_module(arg_split[0])
        func = getattr(module, arg_split[1])
        return func(map(float, arg_split[2:-1]))
    except ModuleNotFoundError as e:
        return "No such module found!"
    except AttributeError as e:
        return "No such function found"
    except Exception as e:
        return f"Error: {e}"


def handler(conn, addr):
    with conn:
        print(f"New connection accepted from {addr}")
        clients_data[addr] = ""
        while True:
            data = conn.recv(MAX_BUFFER_SIZE)
            if not data:
                break

            clients_data[addr] += data.decode('utf-8')
            print(clients_data[addr])
            if clients_data[addr].endswith('fin'):
                answer = data_calc(clients_data[addr])
                conn.sendall(str(answer).encode())

        clients_data.pop(addr)
        print(f"Client {addr} disconnected!")


if __name__ == '__main__':
    pool = concurrent.futures.ThreadPoolExecutor(MAX_WORKERS)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        while True:
            s.listen()
            connection, address = s.accept()
            pool.submit(handler, connection, address)
