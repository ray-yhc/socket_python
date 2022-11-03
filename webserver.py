# import socket
# import sys
#
#
#
# serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# # serverIP = "165.132.5.137"
# serverPort = 6789
#
# serverSocket.bind(("", serverPort))
# serverSocket.listen()
#
# while True:
#     print("The server is ready to receive")
#     connectionSocket, addr = serverSocket.accept()
#
#     try :
#         message = serverSocket.recv(409).decode()
#         filename = message.split()[1]
#         print(filename)
#         f = open(filename[1:])
#         outputdata = f.read()
#         connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
#
#         for i in range(0, len(outputdata)):
#             connectionSocket.send(outputdata[i].encode())
#         connectionSocket.send("\r\n".encode())
#
#         connectionSocket.close()
#
#     except IOError:
#         connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
#         connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())
#
#         connectionSocket.close()
#
# serverSocket.close()
# sys.exit()


from socket import *
import sys

serverSocket = socket(AF_INET, SOCK_STREAM)

serverPort = 6788

serverSocket.bind(('', serverPort))
serverSocket.listen(1)

while True:
    print('The server is ready to receive')
    connectionSocket, addr = serverSocket.accept()

    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())

        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())

        connectionSocket.send("\r\n".encode())
        connectionSocket.close()

    except IOError:
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())
        connectionSocket.close()

serverSocket.close()
sys.exit()


