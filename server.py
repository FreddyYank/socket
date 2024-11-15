import socket

HOST, PORT = '127.0.0.1', 1025

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()

    print(f"Connected by {addr}")

    while True:
        data = conn.recv(1024)
        conn.sendall(data)