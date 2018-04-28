from socket import *
from format import *

print("""
            ##############>>>>>>>>>>^^<<<<<<<<<<##############
            #  Welcome to my first half duplex chat client   #
            #                 By Ethical                     #
            #                Sep 12th 2017                   #
            #  This is a simple chat client that can only    #
            #    either sent message or receive message but  #
            #    not both at a time that is why it is half   #
            #                     duplex                     #
            ##############>>>>>>>>>>^^<<<<<<<<<<##############
   """)
buf = 20480
host = raw_input("host:\n")
port = 4134
addr = (host, port)
cs = socket(AF_INET,SOCK_STREAM) # cs means 'client socket'
cs.connect(addr)
print("\nConnected to "+str(addr))

def main():
    try:
        while(True):
            message = raw_input("\n> ")
            message = message + "\r\a"
            sent = cs.send(message)
            recv_message()
    except KeyboardInterrupt,e:
        error(e)
    except Exception,e:
        error(e)


def recv_message():
    try:
        msg = []
        while(True):
            recved = cs.recv(buf)
            msg.append(recved)
            if recved[-2:] == "\r\a":
                put_together = "".join(msg) # put the message together
                put_together = put_together[0:-2] # remove the \r\a character
                print(format(put_together)) # print message in a nicely formatted way...
                break
    except KeyboardInterrupt,e:
        error(e)
    except Exception,e:
        error(e)

if __name__=="__main__":
    main()
