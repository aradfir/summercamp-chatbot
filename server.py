import socket
import threading
HOST = "127.0.0.1"
PORT = 1036
def data_calc(arg_str:str):
    return sum(map(float,arg_str.split()))
def handler(conn,addr):
    with conn:
        print(f"New connection accepted from {addr}")
        while True:
            data=conn.recv(1024)
            if not data:
                break
            answer=data_calc(data.decode('utf-8'))

            conn.sendall(str(answer).encode())
        print(f"Client {addr} disconnected!")


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen()
    conn,addr=s.accept()
    threading.Thread(target=handler,args=(conn,addr)).start()