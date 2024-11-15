import socket


HOST, PORT = '127.0.0.1', 1025

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    #s.sendall(b"Hello, world")









# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
#     sock.connect((HOST, PORT))
#     while True:
#         data = input("Type the message to send:")
#         data_bytes = data.encode()  # str to bytes
#         sock.sendall(data_bytes)
#
#         print("Received:", data)