

class A:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def string(self):
        return "Formatting string {} - {}".format(self._name, self._age)

    @property
    def name(self):
        return self._name


# obj = A("Maaz", "19")
# copy_obj = obj
# print(copy_obj.name)


class B:

    def __init__(self):
        self.__name = 'Babe'

    def getname(self):
        print("getname() function is called")
        return self.__name

    def setname(self, name):
        print("setname() function is called")
        self.__name = name

    @property
    def name(self):
        print("getname() function is called")
        return self.__name

    @name.setter
    def name(self, value):
        print("setname() function is called")
        self.__name = value

    def delname(self):
        print('delname() called')
        del self.__name

    # name = property(getname, setname, delname)


# obj = B()
# Do not call until necessary
# del B.name
# print(obj.name)


class Person:
    totalObjects = 0

    def __init__(self):
        self.classValue = 1
        Person.totalObjects = Person.totalObjects + 1

    @classmethod
    def showCounts(cls):
        return cls.totalObjects


def make_instance(cls):
    return cls()


obj = Person()
obj2 = Person()
# obj2 = make_instance(obj2)

# obj2 = obj2()
# print("{} - {}".format(obj.__dict__, obj2.__dict__))

# print(obj.classValue)
# obj2 = Person()
# print(obj.showCounts())


class C:
    classValue = None

    def __init__(self):
        self.value = 100

    @classmethod
    def getClassValue(cls):
        value = cls.classValue
        # return value
        return cls().value

    @staticmethod
    def getStaticValue():
        # return self.classValue
        return C().value


obj = C()
print(obj.getClassValue())
print(obj.getStaticValue())
