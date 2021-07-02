
import numpy as np

array = np.array([3, 6, 9, 12])
list = [3, 6, 9, 12]

division_array = array/3
# division_list = list/3

# print(division_array)
# print(type(division_array))
#
# print(division_list)
# print(type(division_list))

# print(len(array))


# print(12/2*3)


def primeNoInBetween(lower, upper):
    prime_number = []
    for i in range(lower, upper+1):
        flag = False
        if i>2:
            for num in range(2, i):
                if i % num == 0:
                    flag = True
                    break
            if not flag:
                prime_number.append(i)
    return prime_number


print(primeNoInBetween(5, 10))