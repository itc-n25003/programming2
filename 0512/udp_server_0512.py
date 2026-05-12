import socket

host = "127.0.0.1"
port = 55555

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((host, port))

print(f"UDPサーバー起動中... {host}:{port}")
while True:
    data, addr = sock.recvfrom(1024)
    print(f"受信: {data} from {addr}")  # バイナリデータをそのまま表示
    if data == b"exit":
        print("終了コマンドを受信。サーバーを終了します。")
        break
    elif data == b"hello":
        print("world!")
        break

sock.close()
