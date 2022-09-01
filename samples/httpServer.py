# HTTP server program
import socket
import sys

args = sys.argv
argc = len(args)

port = 50007
file = "server.html"
cType = b"Content-Type: text/html; charset=utf-8\r\n\r\n"
htHead = b"<html><body>"
htTail = b"</html></body>"

if argc > 2:
    print("Usage:", args[0], "[port]")
    exit()
elif argc > 1:
    port = int(args[1])

HOST = ""  # サーバホスト名（'' とすると実行マシン上の接続可能な全てのホスト名）
print("port=", port, ", file=", file)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)  # ex2.1-2 メモを参照
    s.bind((HOST, port))
    while True:
        s.listen(1)
        conn, addr = s.accept()
        with conn:
            print("Connected by,", addr)
            data = b""
            while True:
                data += conn.recv(1024)
                if b"\r\n\r\n" in data:
                    break
            print("Received:", data.decode(), end="")  # 改行しない

            rData = b"HTTP/1.1 "
            if data.startswith(b"GET "):
                try:
                    with open(file) as f:
                        rData += b"200 OK\r\n" + cType
                        rData += f.read().encode() + b"\r\n"
                except OSError:
                    rData += b"404 Not Found\r\n" + cType
                    rData += htHead + file.encode() + b" is not found" + htTail

            conn.sendall(rData)
            print("Sent:", rData.decode())
            conn.close()
