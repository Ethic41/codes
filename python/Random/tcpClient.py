from socket import *


host = "localhost"
port = 23456
buf = 1024
addrs = (host, port)

tcsk = socket(AF_INET, SOCK_STREAM)
tcsk.connect(addrs)

while True:
	data = raw_input("> ")
	if not data:
		break
	tcsk.send(data)
	data = tcsk.recv(buf)
	if not data:
		break
	print data
tcsk.close()
