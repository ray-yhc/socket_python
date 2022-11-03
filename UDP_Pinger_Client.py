import sys, time
from socket import *

argv = sys.argv
host = argv[1]
port = argv[2]
timeout = 3.5

# AF_INET : ipv4 주소 사용
# SOCK_DGRAM : UDP/IP 프로토콜 사용
clientSocket = socket(AF_INET, SOCK_DGRAM)
# timeout 시간 설정
clientSocket.settimeout(timeout)

port = int(port)
ptime = 0

while ptime<10:
    ptime += 1
    data = "Ping " + str(ptime) + " " + time.asctime()

    try :
        RTTb = time.time() # 전송 시작 시각 측정

        clientSocket.sendto(data.encode(), (host,port)) # 송신
        message, address = clientSocket.recvfrom(1024) # 수신

        RTTa = time.time() # 수신 도착 시각 측정
        print("Reply from" + address[0] + ": " + message.decode())

        # 총 소요된 RTT 측정
        RTT = RTTa-RTTb
        print("RTT : %.4f msec\n" %(RTT))


    except Exception as ex :
        # print(ex)
        print("Request timed out.\n")
        continue
clientSocket.close()


