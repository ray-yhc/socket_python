from socket import *
import sys
import time

# AF_INET : ipv4 주소 사용
# SOCK_STREAM : TCP/IP 프로토콜 사용
serverSocket = socket(AF_INET, SOCK_STREAM)

serverPort = 6789

# port number를 이용하여 소켓과 서버 포트를 연결한 뒤, client의 연결을 기다린다.
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

while True:
    print('The server is ready to receive')

    clientSocket, addr = serverSocket.accept()
    print("Connected by ", addr)

    try:
        message = clientSocket.recv(4096) # 한번에 최대 4096바이트만 읽어오도록 한다.
        print('Received from', addr, message)
        filename = message
        f = open(filename) # 요청한 파일 경로를 통해 파일을 읽는다.
        data_iter = 0
        with open(filename, 'rb') as f:
            try:
                outputdata = f.read(4096)  # 한번에 4096 바이트씩 읽어온다.
                while outputdata:
                    clientSocket.send(outputdata) # 데이터를 보낸다.
                    data_iter = data_iter + 1
                    outputdata = f.read(4096) # 4096 바이트를 읽는다.
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
