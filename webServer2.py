from socket import *
import sys
import time

serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 6789
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

while True:
    print('The server is ready to receive')
    clientSocket, addr = serverSocket.accept()

    try:
        message = clientSocket.recv(4096)
        print('Received from', addr, message)
        filename = message
        f = open(filename)
        data_iter = 0
        with open(filename, 'rb') as f:
            try:
                outputdata = f.read(1024)
                while outputdata:
                    clientSocket.send(outputdata) # 데이터를 보낸다.
                    data_iter = data_iter + 1
                    outputdata = f.read(1024) # 4096 바이트를 읽는다.
                    print("파일 %s (seq: %d) is sent" % (filename, data_iter))
                    time.sleep(5)
            except Exception as ex:
                print(ex)
        clientSocket.close()

    except IOError:
        clientSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        clientSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())
        clientSocket.close()

serverSocket.close()
sys.exit()
