#http://code.activestate.com/recipes/578247-basic-threaded-python-tcp-server/
import socket
import sys

def start_client():
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "127.0.0.1"
    port = 8888

    try:
        soc.connect((host, port))
    except:
        print("Connection error")
        sys.exit()


    message = input()

    while message != 'quit':
        soc.sendall(message.encode("utf8"))
        if soc.recv(5120).decode("utf8") == "pitu":
            print('??')        # null operation

        message = input()

    soc.send(b'--quit--')

if __name__ == "__main__":
    start_client()