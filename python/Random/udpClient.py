from socket import *


host = "localhost"
port = 34567
buf = 1024
addrs = (host, port)

usck = socket(AF_INET, SOCK_DGRAM)

while True:
	data = raw_input(">")
	if not data:
		break
	usck.sendto(data, addrs)
	data, addr = usck.recvfrom(buf)
	if not data:
		break
	print(data)
usck.close()