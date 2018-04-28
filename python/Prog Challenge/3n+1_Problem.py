#This is the 3n+1 problem solution

import time

i,j = map(int, raw_input().split())
i_time = time.time()
lst = []
def main():
	global v
	for n in range(i, j+1):
		algo(n)
		lst.append(v)
	ftime = time.time()-i_time
	print(str(i)+" "+str(j)+" "+str(max(lst)))
	print("Runtime:"+str(ftime)+"s")

def algo(n):
	global v
	v = 1
	while n != 1:
		if n%2 != 0:
			n = 3 * n + 1
			v += 1
		else:
			n = n/2
			v += 1
	if v != 0:
		return v
	else:
		v=v+1
		return v

if __name__ == main():
	main()
