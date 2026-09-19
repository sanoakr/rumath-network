# HTTP server program
import socket

port = 50080
file = "server.html"
# HTTP のヘッダ行は CRLF（\r\n）で終える（RFC 9112 §2.2）
cType = b"Content-Type: text/html; charset=utf-8\r\n"
htHead = b"<html><body>"
htTail = b"</body></html>"
# サーバホスト名（'' とすると実行マシン上の接続可能な全てのホスト名）
HOST = ""
print(f"port={port}, file={file}")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # setsockopt() については第5回ページのメモを参照
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    s.bind((HOST, port))
    while True:
        s.listen(1)
        conn, addr = s.accept()
        with conn:
            print("Connected by,", addr)
            data = b""
            while True:
                chunk = conn.recv(1024)
                # 空行が来ないまま相手が接続を閉じた場合に抜ける
                # （これが無いと無限ループになる）
                if not chunk:
                    break
                data += chunk
                # ヘッダの終わりは空行。RFC では CRLF だが、LF だけを送ってくる
                # クライアントもあるので、受け取る側は両方を認める
                if b"\r\n\r\n" in data or b"\n\n" in data:
                    break
            # 改行しない
            print("Received:", data.decode(), end="")

            rData = b"HTTP/1.1 "
            if data.startswith(b"GET "):
                try:
                    # テキストモードで開くと OS によって改行が変換されるので "rb" で読む
                    with open(file, "rb") as f:
                        # ステータス行・ヘッダ・空行・本文の順に組み立てる
                        rData += b"200 OK\r\n" + cType + b"\r\n"
                        rData += f.read()
                except OSError:
                    rData += b"404 Not Found\r\n" + cType + b"\r\n"
                    rData += htHead + file.encode() + b" is not found" + htTail

            conn.sendall(rData)
            print("Sent:", rData.decode())
            conn.close()
