import socket
from get_ip import get_ip
from time import ctime
from subnetter import subnetter
from discover_online_host import discover

port = 4134
msg = "hello" #this is an inbuilt message that is identified by the server...
cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def main():
    print "Initiating finding host..."
    my_ip = get_ip() # Retrieve the ip of the current working interface...
    print("ip obtained..."+my_ip)
    ip = my_ip
    #subnetter take an ip address in format "192.168.43.236" and return the form
    #"192.168.43." removing the last part
    subnet = subnetter(ip)
    print("subnetted..."+subnet)
    hosts = discover(subnet)
    print hosts

if __name__=="__main__":
    main()
