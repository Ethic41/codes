from socket import *
from time import ctime

host = ""
port = 4134
addrs = (host, port)
buf = 20480
us = socket(AF_INET, SOCK_DGRAM)
us.bind(addrs)
ss = socket(AF_INET, SOCK_STREAM)
ss.bind(addrs)
ss.listen(5)
print "server listening for incoming... "

def main():
    try:
        while(True):
            data = us.recvfrom(buf)
            print("connection from "+str(data[1]))
            print str(data[0])
            if str(data[0]) == "hello":
                us.sendto("hi", (data[1]))
                print "data sent..."+str(data[1])
            else:
                print("closing now...")
                us.close()
    except KeyboardInterrupt:
        us.close()
    except Exception,e:
        raise#print("Error: "+str(e)
    finally:
        exit()

def comm():
    try:
        while(True):
            conn, addr = ss.accept()
            print "connection established from "+str(addr)
            data = conn.recv(buf)
            if not data:
                print("Invalid data received closing connection...")
                break
            elif str(data) == "hello":
                conn.send("hi")
            else:
                conn.send("["+ctime()+"] "+data)
    except KeyboardInterrupt:
        print "Initiation Shutdown..."
    except Exception,e:
        print "Error: "+str(e)
    finally:
        conn.close()
        exit()

if __name__=="__main__":
    main()
