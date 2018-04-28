from socket import *

host = raw_input("host: ")
port = 4134
addrs = (host, port)

def main():
    while(True):
        ts = socket(AF_INET, SOCK_STREAM)
        ts.connect(addrs)
        data = raw_input("> ")
        if not data:
            print("Invalid data entered closing...")
            break
        ts.send(data +"\r\n")
        data = ts.recv(20480)
        if not data:
            print("The remote host sent invalid data.....closing...")
            break
        print(data.strip())
        ts.close()

if __name__=="__main__":
    main()
