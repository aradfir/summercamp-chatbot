import socket
from random import randint
from time import sleep
import threading

HOST = "127.0.0.1"
PORT = 1043
NUM_ABUSERS = 1
MAX_LEN = 20
MAX_VALUE = 1000000
THREAD_TIMEOUT = 1000
BUFFER_SIZE = 1024


def make_random_client():
    input_list_len = randint(1, MAX_LEN)
    input_list = []
    for i in range(input_list_len):
        input_list.append(str(randint(-MAX_VALUE, +MAX_VALUE)))

    str_data = b'builtins sum ' + " ".join(input_list).encode() + b" fin"
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print("sending part 1")
        s.sendall(str_data[:10])
        sleep(2)
        print("sending part 2")
        s.sendall(str_data[10:])
        data = s.recv(BUFFER_SIZE)
        print(f"Sum of {input_list} is {data.decode()}")


all_threads = []
for i in range(NUM_ABUSERS):
    t = threading.Thread(target=make_random_client)
    all_threads.append(t)
    t.start()

for i in range(NUM_ABUSERS):
    all_threads[i].join(THREAD_TIMEOUT)
