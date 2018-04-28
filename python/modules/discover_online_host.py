import socket

port = 4134

def discover(subnet):
    try:
        online_hosts = []
        for i in range(1,256):
            try:
                us = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
                us.settimeout(1)
                us.sendto("hello", (subnet+str(i),port))
                print "sent hello to "+subnet+str(i)+":"+str(port)
                data = us.recvfrom(2048)
                print str(data[0])+" received from "+str(data[1])
                if str(data[0]) == "hi":
                    online_hosts.append(subnet+str(i))
                    print "found one..."
                else:
                    pass
                us.close()
            except socket.timeout:
                print("timed out...")
                pass
        return online_hosts
    except KeyboardInterrupt:
        print("Keyboard Interrupt...closing...")
        us.close()
        exit()
    #finally:
    #0    us.close(

if __name__=="__main__":
    discover(subnet)
