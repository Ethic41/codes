from socket import *
from format import format

host = "" # mean any host can connect...
port = 4134 # my mysterious port
buf = 20480 # buffer size
addr = (host, port) # tuple of address
ss = socket(AF_INET, SOCK_STREAM) # stream socket sc means 'server socket'
ss.bind(addr) # bind socket to the address
ss.listen(5)
print("""
            ##############>>>>>>>>>>^^<<<<<<<<<<##############
            #  Welcome to my first half duplex chat server   #
            #                 By Ethical                     #
            #                Sep 12th 2017                   #
            #  This is a simple chat server that can only    #
            #    either sent message or receive message but  #
            #    not both at a time that is why it is half   #
            #                     duplex                     #
            ##############>>>>>>>>>>^^<<<<<<<<<<##############
   """)
print("\nlistening for incoming connection...")

def main():
    try:
        while(True):
            conn, addrs = ss.accept()
            print("\nconnection has been established from "+str(addrs))
            while(True):
                recv_message(conn)
    except KeyboardInterrupt,e:
        print("exiting...")
        exit()
    except Exception,e:
        print(e)
        pass


def recv_message(conn):
    msg = []
    while(True):
        recved = conn.recv(buf) # contain the received message could be comlete or not
        msg.append(recved) # append the message to the list
        if recved[-2:] == "\r\a":
            put_together = "".join(msg) # put the message together
            put_together = put_together[0:-2] # remove the \r\a character
            print(format(put_together)) # print message in a nicely formatted way...
        send_message(conn)
        break

def send_message(conn):
    try:
        message = raw_input("\n> ")
        message = message + "\r\a" # '\r\a' indicate the end of a message...
        sent = conn.send(message)
    except Exception,e:
        print(e)
        pass


if __name__=="__main__":
    main()
