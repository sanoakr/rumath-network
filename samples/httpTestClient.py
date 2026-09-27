# HTTP test client program
import socket
# リモート（サーバ）ホスト名
HOST = 'localhost'
# リモート（サーバ）ホストのポート番号
port = int(input())
# リモート（サーバ）上のファイル名
file = input()
# GET リクエスト
# HTTP の行末は CRLF（\r\n）。送る側は RFC どおりに厳密に書く（RFC 9112 §2.2）
req = f"GET /{file} HTTP/1.1\r\nHost: {HOST}\r\n\r\n".encode()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, port))
    s.sendall(req)
    print('Send', repr(req.decode()))
    # 1 回の recv() で応答全体が届くとは限らないので、
    # サーバが接続を閉じる（recv() が b'' を返す）まで読み続ける
    data = b""
    while True:
        chunk = s.recv(1024)
        if not chunk:
            break
        data += chunk
    print('Received', data.decode())
