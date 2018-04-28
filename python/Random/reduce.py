def peek_sum(x, y):
	print "adding", x, "and", y
	return x+y

print(reduce(peek_sum, [1,2,3,4,5]))


def peek_max(x, y):
	print "picking max of ", x, "and", y
	return max(x,y)

print(reduce(peek_max, [1,2,3,4,5,6]))