import socket


def main():
    messages = {
        "Wpython Socker Server": 3,
        "LpythonSockerServer": 16,
        "UPYTHONSOCKETSERVER": 18,
        "R1234567890": 10,
        "TpythonSocketServer123": 22,
        "pythonSocketServer123": "pythonSocketServer123",
    }

    HOST, PORT = "localhost", 9999
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))

    for message in messages:
        sock.sendall(bytes(message, "utf-8"))
        res = sock.recv(1024)
        response = str(res, "utf-8")
        correct = True if response == messages[message] else False

        print(f"Sent:   {message}\nReceived:    {response}\nCorrect:    {correct}\n\n")

    while True:
        message = input("Enter a message: ")
        sock.sendall(bytes(message, "utf-8"))
        response = str(sock.recv(1024), "utf-8")

        print(f"Sent:   {message}\nReceived:    {response}\n\n")


if __name__ == "__main__":
    main()
