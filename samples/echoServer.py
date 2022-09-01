# Echo server program
import socket

HOST = ''                 # サーバホスト名（'' とすると実行マシン上の接続可能な全てのホスト名）
PORT = 50007              # サーバポート番号

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data: break
            print('Received', repr(data))
            conn.sendall(data)
            print('Send', repr(data))
