from socket import *
from time import ctime

host = raw_input("Enter hostname...\n")
port = 4134
cs = socket(AF_INET, SOCK_DGRAM)

def main():
    try:
        while(True):
            data = raw_input(">")
            if not data:
                break
            cs.sendto(data, (host, port))
            data, addr = cs.recvfrom(20480)
            if not data:
                print("Invalid data...closing...")
                break
            print(data)
    except Exception, e:
        raise

if __name__=="__main__":
    main()
