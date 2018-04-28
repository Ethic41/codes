from time import ctime
from SocketServer import (TCPServer as TCP, StreamRequestHandler as SRH)

host = ""
port = 4134
addrs = (host, port)

class MyRequestHandler(SRH):
    def handle(self):
        print "connected from "+str(self.client_address)
        self.wfile.write("["+ctime()+"] "+str(self.rfile.readline()))

ts = TCP(addrs, MyRequestHandler)
print "waiting for incoming connection...."
ts.serve_forever()
