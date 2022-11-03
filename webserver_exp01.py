from socket import *
import sys

# AF_INET : ipv4 주소 사용
# SOCK_STREAM : TCP/IP 프로토콜 사용
serverSocket = socket(AF_INET, SOCK_STREAM)

# IP = 192.168.0.7
serverPort = 6789

# port number를 이용하여 소켓과 서버 포트를 연결한 뒤, client의 연결을 기다린다.
serverSocket.bind(('', serverPort))
serverSocket.listen(1) # parameter는 해당 소켓이 동시접속을 허용하는 클라이언트 수

while True:
    print('The server is ready to receive')
    # client와 새로운 연결 생성한다.
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


