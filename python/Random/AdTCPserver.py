from SocketServer import TCPServer as TCP, StreamRequestHandler as SRH
from time import ctime

host = ""
port = 34567
addrs = (host, port)


class MyRequestHandler(SRH):
	def handle(self):
		print("Connection from "+str(self.client_address))
		self.wfile.write("["+str(ctime())+"]"+str(self.rfile.readline()))


tcpServ = TCP(addrs, MyRequestHandler)

print "Waiting for connection...."
tcpServ.serve_forever()