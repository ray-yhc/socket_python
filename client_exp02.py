from socket import *
import os
import sys
import time

Host = '192.168.0.7'
Port = 6789

# AF_INET : ipv4 주소 사용
# SOCK_STREAM : TCP/IP 프로토콜 사용
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((Host, Port))

message = input("요청할 파일 이름 : ")
clientSocket.sendall(message.encode())

data = clientSocket.recv(4096)
data_iter = 0

# 불러온 데이터를 저장할 경로 지정
os.chdir("/Users/raycho/Documents/yoonhocho/2022/coding_edu/socket_python/client")
nowdir = os.getcwd() # 현재의 경로 저장

with open(nowdir+"/"+message, "wb") as f:
    try:
        while data :
            f.write(data)
            data_iter = data_iter + 1
            data = clientSocket.recv(4096)
            print("파일 %s (seq: %d) is received" % (message, data_iter))
            time.sleep(0.5)
    except Exception as ex :
        print(ex)

