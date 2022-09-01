# Echo client program
import socket

HOST = 'localhost'        # リモート（サーバ）ホスト名
PORT = 50007              # リモート（サーバ）ホストのポート番号

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    send= b'Hello, world'
    s.sendall(send)
    print('Send', repr(send))
    data = s.recv(1024)
    print('Received', repr(data))
