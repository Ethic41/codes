from socket import *
from time import ctime


host = ""
port = 23456
buf = 1024
addrs = (host, port)

tsck = socket(AF_INET, SOCK_STREAM)
tsck.bind(addrs)
tsck.listen(5)

while True:
	print "Waiting for a connection......"
	tcls, addr = tsck.accept()
	print "Established connection from: ", addr

	while True:
		data = tcls.recv(buf)
		if not data:
			break
		tcls.send("["+str(ctime())+"]" +" "+ data)
	tcls.close()
tsck.close()