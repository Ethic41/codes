from socket import *
from time import ctime


while True:
	try:
		host = raw_input("Enter the hostname or IP: ")
		port = raw_input("Port: ")
	except Exception, e:
		print e
		print "Please check your input..."
	else:
		if not host:
			host = "localhost"
		if not port:
			port = 23456
		break

buf = 1024
addrs = (host, port)

tcsk = socket(AF_INET, SOCK_STREAM)
tcsk.connect(addrs)

while True:
	try:
		print("Connected to "+host+" on port "+str(port))
		data = raw_input("["+str(ctime())+"] ")
		if not data:
			tcsk.close()
			break
		tcsk.send(data)
		data = tcsk.recv(buf)
		if not data:
			tcsk.close()
			break
		print(data)
	except Exception, e:
		print e
		print "please check your input"
tcsk.close()