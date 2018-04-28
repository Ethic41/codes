def checkIndex(key):
	if not isinstance(key, (int, long)):raise TypeError
	if key<0:raise IndexError

class ArithmeticSequence:
	def __init__(self, start=0, step=1):
		self.start = start
		self.step = step
		self.changed = {}

	def __getitem__(self, key):
		checkIndex(key)

		try:
			return self.changed[key]
		except KeyError:
			return self.start + key* self.step
	def __setitem__(self, key, value):
		checkIndex(key)
		self.changed[key]=value

s = ArithmeticSequence(4, 7)
print s[4]

s[9]=6
print s[9]
print s[10]
