"""
Append 1 if the array element is Power of two else append 0
"""


def is_power_of_two(arr):

    _list = []
    for value in arr:

        count = 0
        flag = False
        while True:

            if 2**count == value:
                flag = True
                break

            elif 2 ** count > value:
                break

            else:
                count += 1

        if flag:
            _list.append(1)
        else:
            _list.append(0)

    return _list


print(is_power_of_two([1, 2, 3, 4]))
