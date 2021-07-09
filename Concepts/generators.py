# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n
    yield n
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n


# a = my_gen()
# print(next(a))
# print(next(a))
# print(next(a))


a = (i for i in range(8))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
