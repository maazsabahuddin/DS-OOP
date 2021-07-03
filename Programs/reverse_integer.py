

def reverse_integer(num):

    rev = 0
    while num > 0:
        left = num % 10
        rev = (rev * 10) + left
        num = num//10

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


print(reverse_integer(102))
print(reverse_integer_by_string(102))
