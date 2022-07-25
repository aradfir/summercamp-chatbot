import socket
import threading
import importlib
HOST = "127.0.0.1"
PORT = 1037
client_datas = dict()


def data_calc(arg_str: str):
    # remove last item (fin)
    # cast all items to float
    # return sum
    splited=arg_str.split()
    try:
        module=importlib.import_module(splited[0])
        func = getattr(module, splited[1])
        return func(map(float, splited[2:-1]))
    except Exception as e:
        print("No module found!")
    return "Error in finding module/function"





def handler(conn, addr):
    with conn:
        print(f"New connection accepted from {addr}")
        client_datas[addr] = ""
        while True:
            data = conn.recv(99999999)

            if not data:
                break
            client_datas[addr] += data.decode('utf-8')
            if client_datas[addr].endswith('fin'):
                answer = data_calc(client_datas[addr])
                conn.sendall(str(answer).encode())

        client_datas.pop(addr)
        print(f"Client {addr} disconnected!")


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    while True:
        s.listen()
        conn, addr = s.accept()
        threading.Thread(target=handler, args=(conn, addr)).start()
