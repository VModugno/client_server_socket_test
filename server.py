import socket

def start_server():
    # Set up a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to server address and server port
    server_address = ('localhost', 4000)
    server_socket.bind(server_address)

    # Listen for incoming connections (1 client at a time)
    server_socket.listen(1)

    print(f"Server is running on {server_address[0]} at port {server_address[1]}")
    print("Waiting for a connection...")

    # Wait for a client to connect
    connection, client_address = server_socket.accept()

    try:
        print(f"Connection from {client_address}")

        # Receive the data in small chunks
        while True:
            data = connection.recv(16)
            print(f"Received: {data.decode()}")

            if data:
                print("Sending data back to the client...")
                connection.sendall(data)
            else:
                print("No data from client, closing connection.")
                break
    finally:
        # Clean up the connection
        connection.close()

if __name__ == '__main__':
    start_server()
