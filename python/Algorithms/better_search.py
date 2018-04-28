a = raw_input()
a = list(a)
x = raw_input()

def main(a, x):
	ans = "Not found"
	for i in range(len(a)):
		if x==a[i]:
			ans = i
			return ans
			break
	return ans
print(main(a,x))
