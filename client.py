import socket
import time
import threading

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('192.168.1.203', 4000)
    client_socket.connect(server_address)

    # Start a thread to listen for user input to close the connection
    stop_thread = threading.Event()

    def check_for_exit():
        input("Press Enter to exit...\n")
        stop_thread.set()
        client_socket.close()

    user_input_thread = threading.Thread(target=check_for_exit)
    user_input_thread.start()

    try:
        message = 'Hello, this is the client!'
        print(f"Sending: {message}")
        client_socket.sendall(message.encode())

        while not stop_thread.is_set():
            data = client_socket.recv(16)
            if not data:
                print("Connection closed by the server.")
                break
            print(f"Received: {data.decode()}")
            time.sleep(1)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client_socket.close()
        print("Connection closed.")
        user_input_thread.join()

if __name__ == '__main__':
    start_client()

