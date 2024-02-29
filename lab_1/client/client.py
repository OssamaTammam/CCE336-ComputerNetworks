import socket


def main():
    messages = [
        "Wpython Socker Server",
        "LpythonSockerServer",
        "UPYTHONSOCKETSERVER",
        "R1234567890",
        "TpythonSocketServer123",
        "pythonSocketServer123",
    ]

    HOST, PORT = "localhost", 9999

    for message in messages:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))

        sock.sendall(bytes(message + "\n", "utf-8"))
        response = str(sock.recv(1024), "utf-8")

        sock.close()

        print(f"Sent:   {message}\nReceived:    {response}\n")

    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))

        message = input("Enter a message: ")
        sock.sendall(bytes(message + "\n", "utf-8"))
        response = str(sock.recv(1024), "utf-8")

        sock.close()

        print(f"Sent:   {message}\nReceived:    {response}\n")


if __name__ == "__main__":
    main()
