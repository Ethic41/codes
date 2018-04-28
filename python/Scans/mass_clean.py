import os

with open(os.getcwd()+"/webscan.dmd", "r") as f:
	lines = f.readlines()
with open(os.getcwd()+"/webhost.dmd", "a") as f:
	for line in lines:
		address = line.split(" ")[3]
		f.write(address+"\n")
print("Done.")