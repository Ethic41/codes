def conflict(state, nextX):
	nextY = len(state)
	for i in range(nextY):
		if abs(state[i]-nextX) in (0, nextY-i):
			return True
	return False


def queens(num=8, state=()):
	for pos in range(num):
		if not conflict(state, pos):
			if len(state) == num-1:
				yield (pos,)
			else:
				for result in queens(num, state + (pos,)):
					yield (pos,) + result

print len(list(queens(12)))