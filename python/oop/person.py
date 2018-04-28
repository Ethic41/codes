import datetime
class Person(object):
    #create a person
    def __init__(self, name):
        self.name = name
        try:
            lastBlank = name.rindex(" ")
            self.lastName = name[lastBlank+1:]
        except:
            self.lastName = name
        self.birthday = None

    def getName(self):
        "Returns self's fullname"
        return self.name

    def getLastName(self):
        "Returns self's lastname"
        return self.lastName

    def setBirthday(self, birthdate):
        self.birthday = birthdate

    def getAge(self):
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days
    def __lt__(self, other):
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    def __str__(self):
        return self.name

me = Person("Dahir Muhammad")
me.setBirthday(datetime.date(1995, 12, 10))
print("%s is %s days old."%(me.getName(), me.getAge()))
