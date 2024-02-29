import socketserver
import Handler


def main():
    HOST, PORT = "localhost", 9999
    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), Handler) as server:
        server.serve_forever()


if __name__ == "__main__":
    main()
