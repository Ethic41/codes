from socket import *
from time_format import time_format
import threading


buf = 20480
inc_host = "" #incoming host can be anyone
port = 4134
addr = (inc_host, port)

def main():
    try:
        print("""
                ##############>>>>>>>>>>^^<<<<<<<<<<##############
                #    Welcome to my first full duplex chat App    #
                #                 By Ethical                     #
                #                Sep 12th 2017                   #
                #  This is a simple chat server that can send    #
                #     and receive message at the same time       #
                #   it is designed to be fast and portable and   #
                #              yet very reliable.                #
                ##############>>>>>>>>>>^^<<<<<<<<<<##############
           """)
        listning = threading.Thread(target=listner, args="") #create listner thread
        sending = threading.Thread(target=sender, args="" ) #create sender thread
        listning.start() #start listning
        sending.start() #start sending
    except Exception, e:
        raise


def listner():
    try:
        listner_sock = socket(AF_INET, SOCK_STREAM)
        #listner_sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        listner_sock.bind(addr)
        listner_sock.listen(2)
        while(True):
            conn, addrs = listner_sock.accept()
            print(addrs[0]+" has joined")
            while(True):
                recv_message(conn)
    except Exception,e:
        raise


def recv_message(conn):
    try:
        msg = []
        while(True):
            recved = conn.recv(buf)
            msg.append(recved)
            if recved[-2:] == "\r\a":
                put_together = "".join(msg) # put the message together
                put_together = put_together[0:-2] # remove the \r\a character
                print(time_format(put_together)) # print message in a nicely formatted way...with time
            break
    except Exception,e:
        raise


def sender():
    try:
        host = raw_input("\nhost>") # specify host address to connect to..
        addr = (host, port) #host and port tuple
        send_sock = socket(AF_INET, SOCK_STREAM)
        #send_sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        send_sock.connect(addr)
        conn = send_sock
        while(True):
            send_message(conn)
    except Exception,e:
        raise


def send_message(conn):
    try:
        message = raw_input("\n> ")
        message = message + "\r\a" # '\r\a' indicate the end of a message...
        sent = conn.send(message)
    except Exception,e:
        raise

if __name__ == '__main__':
    main()
