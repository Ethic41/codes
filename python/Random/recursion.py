

#def recursion():
	#return recursion()

#def factorial(n):
#	rslt = n
#	for i in range(1, n):
#		rslt *= i
#	return rslt
"""
def factorial(n):
	if n == 1:
		return 1
	else:
		return n * factorial(n-1)
print(factorial(3))"""
"""
def pow(x, n):
	rslt = 1
	for i in range(n):
		rslt *= x
	return rslt
print(pow(3, 2))"""

def pow(x, n):
	if n == 0:
		return 1
	else:
		return x * pow(x, n-1)
print(pow(20, 9))

"""num = [2, 4, 6, 23, 65, 89, 43, 12]
print(map(lambda n: 2*n, num))
print(map(chr, num))
print(map(ord, "hello, World"))"""