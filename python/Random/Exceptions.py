while 1:
	try:
		a = input("Enter First Integer:")
		b = input("Enter Second Integer:")
		print(a/b)
	except ZeroDivisionError, e:
		print e
		print "The Second Integer Should be greater than zero!"
	except SyntaxError, e:
		print e
		print "Please Only Integers No letters or whitespace"


"""try:
	a = input()
	b = input()
	print a/b
except(ZeroDivisionError, SyntaxError, TypeError):
	print "Please Check Ur input"
"""