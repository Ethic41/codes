from socket import *
from time import ctime
import os
import re

host = "" # any host
port = 4134 # mystery

addr = (host, port)
sc = socket(AF_INET, SOCK_STREAM)
buf = 20480
sc.bind(addr)
sc.listen(10)
print("listening for incoming connection...")
commands = ["os", "ls", "date", "ls [dir]"]
conn, addrs = sc.accept()

def main():
    sent = conn.send(str(commands))
    receive_check()

def receive_check():
    while(True):
        incoming_command = conn.recv(buf)
        if incoming_command == "date":
            date()
        elif incoming_command == "os":
            os_call()
        elif incoming_command == "ls":
            ls()
        elif re.match("ls .", incoming_command):
            ls_dir(incoming_command)
        else:
            sent = conn.send("exit")
            if not sent:
                print("connection broken...not sent...")


def date():
    try:
        curtime = ctime()
        sent = conn.send(curtime)
        if not sent:
            print("socket broken...not sent...")
    except Exception,e:
        error(e)


def os_call():
    try:
        os_name = os.name
        sent = conn.send(os_name)
        if not sent:
            print("socket broken...not sent...")
    except Exception,e:
        error(e)


def ls():
    try:
        dirs = os.listdir(os.getcwd())
        send_dirs(dirs)
    except Exception,e:
        error(e)


def ls_dir(command):
    try:
        dir = command[3:].strip(" ")
        dirs = os.listdir(os.getcwd()+"/"+dir)
        send_dirs(dirs)
    except Exception,e:
        error(e)

def send_dirs(dirs):
    try:
        for dir in dirs:
            dir = dir+"\r\a"
            sent = conn.send(dir)
        exit = conn.send("exit")
    except Exception,e:
        error(e)

def error(e):
    print("Error: "+str(e)+" exiting...")
    exit()



if __name__=="__main__":
    main()
