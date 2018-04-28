from socket import *


host = "localhost"
port = 34567
buf = 1024
addrs = (host, port)

while True:
	tcsk = socket(AF_INET, SOCK_STREAM)
	tcsk.connect(addrs)
	data = raw_input(">")
	if not data:
		break
	tcsk.send(data+"\r\n")
	data = tcsk.recv(buf)
	if not data:
		break
	print data.strip()
	tcsk.close()