import socket
from random import randint
HOST = "127.0.0.1"
PORT = 1036


len=randint(1,20)
l=[]
for i in range(len):
    l.append(str(randint(-10000,10000)))
str_data=" ".join(l).encode()
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    s.sendall(str_data)
    data=s.recv(1024)
    print(f"Sum of {l} is {data.decode()}")