import socket

def start_client():
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the server's address and port
    server_address = ('localhost', 4000)
    client_socket.connect(server_address)

    try:
        # Send data
        message = 'Hello, this is the client!'
        print(f"Sending: {message}")
        client_socket.sendall(message.encode())

        # Look for the response
        amount_received = 0
        amount_expected = len(message)
        
        while amount_received < amount_expected:
            data = client_socket.recv(16)
            amount_received += len(data)
            print(f"Received: {data.decode()}")

    finally:
        # Closing the socket
        client_socket.close()

if __name__ == '__main__':
    start_client()
