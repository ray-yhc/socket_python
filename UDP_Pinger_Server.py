from socket import *
import random

# AF_INET : ipv4 주소 사용
# SOCK_DGRAM : UDP/IP 프로토콜 사용
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverPort = 6785
serverSocket.bind(('', serverPort))

while True:
    rand = random.randint(0,10)

    message, address = serverSocket.recvfrom(1024)
    message = message.upper()

    # rand가  4 미만일 경우 packet loss 가 발생했다고 간주하고 넘어간다.(40% 확률)
    if rand < 4:
        continue

    # 받은 메시지를 다시 재전송
    serverSocket.sendto(message, address)

