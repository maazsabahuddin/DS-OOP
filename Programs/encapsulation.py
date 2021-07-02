# Python program to
# demonstrate private members

# Creating a Base class
class Base:
    def __init__(self):
        self.a = "Maaz"
        self._a = "Maaz protected"
        self.__a = "Maaz private"

    def showPrivate(self):
        return self.__a


# Creating a derived class
class Derived(Base):
    def __init__(self):
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling private member of base class: ")
        # print(self.__a)
        print(self._Base__a)
        print("Calling protected member of base class: ")
        print(self._a)


# Driver code
# obj1 = Base()
# print(obj1.a)
# print(obj1._a)
# print(obj1._Base__a)
# print(dir(obj1))


obj2 = Derived()
