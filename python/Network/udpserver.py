from socket import *
from time import ctime

host = ""
port = 4134
ss = socket(AF_INET, SOCK_DGRAM)
ss.bind((host, port))

def main():
    try:
        while(True):
            print("waiting for incoming connection....")
            data, addr = ss.recvfrom(20480)
            ss.sendto(("["+ctime()+"] "+data), addr)
            print("data received from ["+str(addr)+"] and sent back with time stamp...")
        ss.close()
        exit()
    except Exception, e:
        print(e)
        exit()

if __name__=="__main__":
    main()
