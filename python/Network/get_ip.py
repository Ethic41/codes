import socket

# this will retrieved the ip address of the working interface of this host....
#this was obtained from http://stackoverflow.com
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("10.255.255.255",1))
        ip = s.getsockname()[0]
    except:
        ip = "127.0.0.1"
    finally:
        s.close()
        return ip

if __name__=="__main__":
    get_ip()
