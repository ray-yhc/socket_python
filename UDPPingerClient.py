import sys, time
from socket import *

argv = sys.argv
host = argv[1]
port = argv[2]
timeout = 3.5

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(timeout)

port = int(port)
ptime = 0

while ptime<10:
    ptime += 1
    data = "Ping " + str(ptime) + " " + time.asctime()

    try :
        RTTb = time.time()
        clientSocket.sendto(data.encode(), (host,port))
        message, address = clientSocket.recvfrom(1024)
        RTTa = time.time()
        print("Reply from" + address[0] + ": " + message.decode())
        RTT = RTTa-RTTb
        print("RTT : %.4f msec" %(RTT))
    except Exception as ex :
        # print(ex)
        print("Request timed out.")
        continue
clientSocket.close()


