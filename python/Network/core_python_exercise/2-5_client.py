from socket import *
import re

host = raw_input("hostname:\n>")
port = input("port:\n>")
buf = 20480
addr = (host, port)
cs = socket(AF_INET,SOCK_STREAM)
cs.connect(addr)
print("connecting to "+str(addr)+"...")

def main():
    try:
        print("Welcome, available commands\n")
        print(cs.recv(buf))
        enter_commands()
    except KeyboardInterrupt,e:
        error(e)
    except Exception, e:
        error(e)

def enter_commands():
    try:
        while(True):
            command = raw_input("command:\n>")
            check_command(command)
    except Exception, e:
        error(e)

def check_command(command):
    try:
        if command == "date":
            date()
        elif command == "os":
            os_call()
        elif command == "ls":
            ls()
        elif re.match("ls .", command):
            ls_dir(command)
        elif command == "quit":
            print("shutdown requested client going away...")
            cs.shutdown(SHUT_RDWR)
            cs.close()
            exit()
        else:
            print("Invalid command or command not available for you...")
    except Exception,e:
        error(e)

def date():
    try:
        sent = cs.send("date")
        if not sent:
            print("connection broken...not sent")
        data = cs.recv(buf)
        print(format(data)) # format data in a fancy way...
    except Exception, e:
        error(e)

def os_call():
    try:
        sent = cs.send("os")
        if not sent:
            print("connection broken...not sent")
        data = cs.recv(buf)
        print(format(data))
    except Exception,e:
        error(e)

def ls():
    try:
        sent = cs.send("ls")
        if not sent:
            print("connection broken...not sent")
        dir_recv() # receive dirs based on raliya's concept
    except Exception,e:
        error(e)


def ls_dir(command): # dir is the directory we want to list
    try:
        sent = cs.send(command)
        dir_recv()
    except Exception,e:
        error(e)


def dir_recv():
    try:
        msg = []
        while(True):
            data = cs.recv(buf)
            msg.append(data)
            if data[-4:] == "exit":
                break
        put_together = "".join(msg) #put everything together
        put_together = put_together[0:-4] # remove the 'exit' string at the end of message chunk
        seprate_msg = put_together.split("\r\a") #seprate the message by character "\r\a" for(raliya)
        for dir in seprate_msg:
            print(format(dir))
    except Exception,e:
        error(e)

def format(data): # format data in a fancy ascii way.
    try:
        if data != "":
            data = "\n+"+2*"-"+len(data)*"-"+2*"-"+"+\n"+"|"+2*" "+data+2*" "+"|\n"+"+--"+len(data)*"-"+"--+"
            return data
        else:
            return data
    except Exception, e:
        error(e)


def error(e):
    print("Error: "+str(e)+" exiting...")
    exit()


if __name__=="__main__":
    main()
