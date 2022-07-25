import socket
from random import randint
from time import sleep
import threading
HOST = "127.0.0.1"
PORT = 1041
NUM_ABUSERS=1000
def make_random_client():
    len = randint(1, 20)
    l = []
    for i in range(len):
        l.append(str(randint(-10000, 10000)))
    str_data = b'builtins sum ' + " ".join(l).encode() + b" fin"
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print("sending part 1")
        s.sendall(str_data[:10])
        sleep(2)
        print("sending part 2")
        s.sendall(str_data[10:])
        data = s.recv(1024)
        print(f"Sum of {l} is {data.decode()}")
all_threads=[]
for i in range(NUM_ABUSERS):
    t=threading.Thread(target=make_random_client)
    all_threads.append(t)
    t.start()
for i in range(NUM_ABUSERS):
    all_threads[i].join(1000)