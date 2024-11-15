import socket
import threading

# Функция для обработки каждого клиента
def handle_client(client_socket, client_address):
    print(f"Подключен клиент: {client_address}")
    try:
        while True:
            # Получаем сообщение от клиента
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break  # Если сообщение пустое, клиент отключился
            print(f"Сообщение от {client_address}: {message}")
            # Отправляем сообщение обратно клиенту
            response = f"Эхо: {message}"
            client_socket.send(response.encode('utf-8'))
    except Exception as e:
        print(f"Ошибка с клиентом {client_address}: {e}")
    finally:
        print(f"Клиент {client_address} отключился")
        client_socket.close()

# Настройка сервера
def start_server(host='127.0.0.1', port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Сервер запущен на {host}:{port}")

    try:
        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Новое соединение: {client_address}")
            # Создаем поток для клиента
            client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
            client_thread.start()
    except KeyboardInterrupt:
        print("\nСервер останавливается...")
    finally:
        server_socket.close()

if __name__ == "__main__":
    start_server()
