#Still trying to master oop ==> 16th-04-2018

class MyDataWithMethod:
    def printFoo(self):
        print("You invoked foo")


#myObj = myDataWithMethod()
#myObj.printFoo()

class AddrBookEntry:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        print("created instance for %s"%self.name)

    def getPhoneNumber(self):
        print(self.phone)

    def updatePhone(self, newphone):
        self.phone = newphone
        print("updated phone for %s"%self.name)


class AddrBookEntryWithEmail(AddrBookEntry):
    def __init__(self, name, phone, email):
        AddrBookEntry.__init__(self, name, phone)
        self.email = email

    def updateEmail(self, newEmail):
        self.email = newEmail
        print("updated email for %s"%self.name)

    def getEmail(self):
        print(self.email)
"""
john = AddrBookEntryWithEmail("Dahir Muhammad Dahir", "08175342877", "dahirmuhammad3@gmail.com")
john.getEmail()
john.getPhoneNumber()
john.updateEmail("dahirmuhammad@hostcrane.com")
john.updatePhone("08167260802")
john.getEmail()
john.getPhoneNumber()
"""
#useless class implementation
"""
class Parent():
    pass

class Child(Parent):
    pass

newChild = Child()


#print(Child.__bases__)
#print(newChild.__class__)
"""

#useful class implementation

class Parent:
    'this is the parent class implementation'
    def __init__(self):
        print("Created an instance of %s"%(self.__class__.__name__))
    def foo(self):
        print("i am P-foo()")

class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
        print("calling Child's constructor")
    def foo(self):
        print("I am C-foo()")
"""
newParent = Parent()
print(newParent.__doc__)
print(newParent.__class__)
print(newParent.__module__)
print(Parent.__bases__)
print(dir(Parent()))
"""

#newChild = Child()
"""
print(newChild.__class__)
print(Child.__bases__)
print(dir(Child()))
"""
#newChild.foo()
#Parent.foo(newChild)
"""
class Parent1:
    def foo(self):
        print("parent1 foo()")

class Parent2:
    def foo(self):
        print("parent2 foo()")
    def bar(self):
        print("parent2 bar()")

class Child1(Parent1, Parent2):
    pass

class Child2(Parent1, Parent2):
    def foo(self):
        print("child2 foo()")

    def bar(self):
        print("child2 bar()")

class grandChild(Child1, Child2):
    pass

newGrandChild = grandChild()
newGrandChild.foo()
newGrandChild.bar()
Child2.foo(newGrandChild)

"""
class oPair:
    def __init__(self, obj1, obj2):
        self.data = (obj1, obj2)

    def __str__(self):
        return str(self.data)

    __repr__=__str__

    def __add__(self, other):
        return self.__class__(self.data[0] + other.data[0], self.data[1] + other.data[1])


pair1 = oPair(-3, 4)
pair2 = oPair(-5, 2)

print(pair1 + pair2)
print(1+3)








#End of code
