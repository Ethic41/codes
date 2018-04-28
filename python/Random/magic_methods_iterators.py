#constructor

class Class:
	def __init__(self):
		self.someVar = 42

class Bird1(object):

	def __init__(self):
		self.hungry = 1

	def eat(self):
		if self.hungry:
			self.hungry = 0
			print "Aaahh!!"
		else:
			print "No thanks!"

class SongBird(Bird1):
	def __init__(self):
		super(SongBird, self).__init__()
		self.sound = "Wheeeyy!!Wheey!!Wheeeyy!!!"
		self.sang = 0

	def sing(self):
		print self.sound
		self.sang = 1
		self.hungry = 1

	def feed(self):
		if self.sang:
			self.eat()
		else:
			print "Not hungry. Didn't Sing today!"


class Bird():

	def __init__(self):
		self.hungry = 1

	def eat(self):
		if self.hungry:
			self.hungry = 0
			print "Aaahh!!"
		else:
			print "No thanks!"

class SongBird(Bird):
	def __init__(self):
		Bird.__init__(self)
		self.sound = "Wheeeyy!!Wheey!!Wheeeyy!!!"
		self.sang = 0

	def sing(self):
		print self.sound
		self.sang = 1
		self.hungry = 1

	def feed(self):
		if self.sang:
			self.eat()
		else:
			print "Not hungry. Didn't Sing today!"

class Rectangle(object):
	def __init__(self):
		self.width = 0
		self.height = 0

	def setSize(self, size):
		self.width, self.height = size

	def getSize(self):
		return self.width, self.height

	size = property(getSize, setSize)


class Fibs:
	def __init__(self):
		self.a = 0
		self.b = 1

	def next(self):
		self.a, self.b = self.b, self.a+self.b
		return self.a

	def __iter__(self):
		return self


fibs = Fibs()
for f in fibs:
	if f > 1000:
		print f
		break

class TestIterators:
	value = 0
	def next(self):
		self.value += 1
		if self.value > 10:raise StopIteration
		return self.value

	def __iter__(self):
		return self

#nested = [[1,2,3], [4,5,[7,8]], [9, 10, [11,12,13,[14,15]]],[16,17,[18,19,[20]]]]

def flatten(nested):
	for subls in nested:
		for element in subls:
			try:
				if str(type(element)) == "<type 'int'>":
					yield element
				for num in element:
					yield num
			except TypeError:
				pass

def flatten(nested):
	try:
		for element in nested:
			for subls in flatten(element):
				yield subls
	except TypeError:
		yield nested
