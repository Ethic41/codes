from socket import *
from time import ctime

host = ""
port = 4134
ss = socket(AF_INET, SOCK_STREAM)
ss.bind((host, port))
ss.listen(5)
print("Server started listening on port: "+str(port)+"\n")

def main():
    try:
        while(True):
            conn, addr = ss.accept()
            print("connection established from "+str(addr)+"\n")
            while(True):
                data = conn.recv(2)
                if not data:
                    print("Invalid data received from %s closing connection..." % str(addr))
                    break
                send = conn.send("["+ctime()+"]"+data+" on "+str((host, port)))
            conn.close()
        ss.close()
    except Exception, e:
        print(e)
        exit()

if __name__=="__main__":
    main()
