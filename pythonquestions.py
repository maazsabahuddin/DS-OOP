

class A:

    counter = 0

    def __init__(self, name):
        self.name = name
        A.counter += 1

    def __getstate__(self):
        print("Hi")


obj = A('Maaz')
obj2 = A('Sana')
obj3 = A('Maaz')
obj4 = A('Sana')
ob5 = A('Maaz')
obj6 = A('Sana')
print(A.counter)
# print(A.__class__().counter)
print(dir(A.__class__))


"""
from collections import Counter
print(Counter("Maaz"))
print(type(Counter("Maaz")))
print(Counter("Maaz").most_common())
print(type(Counter("Maaz").most_common()))
print(Counter("Maaz").elements())
print(type(Counter("Maaz").elements()))
"""
