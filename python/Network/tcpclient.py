from socket import *
from time import ctime

host = raw_input("Enter hostname...:\n")
port = 4134
cs = socket(AF_INET, SOCK_STREAM)
cs.connect((host,port))
print("connected to "+host+":"+str(port))

def main():
    try:
        while(True):
            data = raw_input(">")
            if not data:
                print("Not valid data...closing connection...")
                break
            sent = cs.send(data)
            print(str(sent)+" of "+str(len(data))+" sent")
            data = cs.recv(2048)
            if not data:
                print("No valid data received....closing connection")
                break
            print(data)
        cs.close()
    except Exception, e:
        print(e)
        exit()

if __name__=="__main__":
    main()
