# Echo client program
import socket

host = input()
port = int(input())

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    while True:
        send = input().encode()
        if send == 'quit'.encode():
            break
        s.sendall(send)
        print('Send', repr(send))
        data = s.recv(1024)
        print('Received', repr(data))
        print('Decoded', data.decode())
