from socket import *
from time import ctime

host = ""
port = 34567
buf = 1024
addrs = (host, port)

usck = socket(AF_INET, SOCK_DGRAM)
usck.bind(addrs)

while True:
	print("Waiting for incoming connection......")
	data, addr = usck.recvfrom(buf)
	usck.sendto(str(ctime())+" "+data, addr)
	print("Received data has been sent to ", addr)
usck.close()