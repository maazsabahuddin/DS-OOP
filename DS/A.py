from numpy import array
"""
class Enemy:

    def __init__(self):
        self.life = 3

    def attack(self):
        print("I'm attacked.")
        self.life -= 1

    def check_life(self):
        print(str(self.life) + " Life's left")


enemy1 = Enemy()
enemy1.attack()
enemy1.check_life()
"""

# inheritance

"""


class Parent():

    def last_name(self):
        print("Sabahuddin")


class Child(Parent):

    def first_name(self):
        print("Maaz")

    #method overloding..
    def last_name(self):
        print("Bhai")


use_it = Child()
use_it.first_name()
use_it.last_name()
"""


# inheritance by w3cschool
"""

class Base():

    def __init__(self, fname, lname):
        self.f = fname
        self.l = lname

    def print_name(self):
        print(self.f + " " + self.l)


class Student(Base):

    def __init__(self, fname, lname, year):
        Base.__init__(self, fname, lname)
        self.graduation_year = year

    def Welcome(self):
        print("Welcome", self.f, self.l, "to Symantec with graduation year:", self.graduation_year)


d = Student("Maaz", "Sabahuddin", 2019)
d.Welcome()
"""


""" TUPLE CONSTRUCTOR
thistuple = list(("apple", "banana", "cherry", "apple")) # note the double round-brackets
print(thistuple.count("apple"))
print(thistuple.index("apple"))
print(thistuple)
"""

# Changing the dictionary keyword
"""
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict["a"] = thisdict["year"]
del thisdict["year"]
print(thisdict)
"""

# dictionary keys and values
"""
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "brand" in thisdict.keys():
  print("Yes, in our dictionary.")

mydict = {
    "maaz": "sabahuddin"
}

thisdict.update(mydict)
print(thisdict)
"""

# if pass
"""
a = 33
b = 200

if b > a:
    pass

print("b is greater than a")
"""

# Multiple conditions within a single line
# a, b = 2, 3
# print("a") if a > b else print("=") if a == b else print("B")

# y = [3, 6, 9, 12]
# y/3.0
# print(y)

# x = array([3, 6, 9, 12])
# x = x/3
# print(x)
s = [1, 2]

def abc():
    return 10


for i in range(s[1], abc(), 2):
    print(i)