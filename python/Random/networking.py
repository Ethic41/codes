from socket import *
from time import ctime


host = ""
port = 80
buf = 1024
addrs = (host, port)

tsck = socket(AF_INET, SOCK_STREAM)
tsck.bind(addrs)
tsck.listen(5)

while True:
	print "Waiting for a connection......"
	tsck.send("Welcome")
	tcls, addr = tsck.accept()
	print "Established connection from: ", addr

	while true:
		data = tcls.recv(buf)
		if not data:
			break
		tcls.send(str(ctime()), data)
	tcls.close()
tcsk.close()