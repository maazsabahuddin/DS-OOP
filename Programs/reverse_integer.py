

def absolute_method(integer):
    count = 0
    if integer > 0:
        return integer

    for i in range(0, integer, -1):
        count += 1

    return count


def abs_method(integer):
    return -integer if integer < 0 else integer


def reverse_integer(num):

    flag = False
    if num < 0:
        flag = True
        num = abs_method(num)

    rev = 0
    while num > 0:
        left = num % 10
        rev = (rev * 10) + left
        num = num//10

    if flag:
        return -rev
    return rev


def reverse_integer_by_string(num):
    string_num = str(num)
    string_list = []
    for value in string_num:
        string_list.append(value)

    reverse_string_list = []
    for i in range(len(string_list)):
        reverse_string_list.append(string_list.pop())

    return ''.join(reverse_string_list)


print(reverse_integer(-102))
print(reverse_integer_by_string(102))
