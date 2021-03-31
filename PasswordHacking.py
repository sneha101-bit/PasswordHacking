import socket
import sys
import itertools
import string

str_list = string.ascii_lowercase + str(string.digits)
print(str_list)
alpha_list = [x for x in str_list]
args = sys.argv
host_name = '127.0.0.1'
port = args[1]
address = (host_name, int(port))

def match_pass():
    for attempt in range(1, 5):
        for val in itertools.product(alpha_list, repeat=attempt):
            yield ''.join(val)

with socket.socket() as client_socket:
    client_socket.connect(address)

    for password in match_pass():
        client_socket.send(password.encode())
        if client_socket.recv(1024).decode() == "Connection Success!":
            print(password)
            break

client_socket.close()
