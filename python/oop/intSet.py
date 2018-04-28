
class IntSet(object):
    """An intSet is a set of integers"""
    def __init__(self):
        #create an empty set of integers
        self.vals = []
    def insert(self, e):
        #assumes 'e' is an integer and insert 'e' into the list
        if not e in self.vals:
            self.vals.append(e)
    def member(self, e):
        #Assumes e is an integer, Returns True if e in set, False otherwise
        return e in self.vals

    def remove(self, e):
        #Assumption: same as above and tries to remove e from list
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + "not found")
    def getMembers(self):
        return self.vals[:]

    def __str__(self):
        self.vals.sort()
        result = ""
        for val in self.vals:
            result += str(val) + ","
        return "{"+ result[:-1] + "}"

s = IntSet()
s.insert(3)
s.insert(4)
s.insert(12)
print s.getMembers()
s.remove(4)
print s.getMembers()
