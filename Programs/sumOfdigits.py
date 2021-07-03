

def sum_integer_digits(num):

    total = 0
    while num > 0:
        remainder = num % 10
        total += remainder
        num = num // 10

    return total


print(sum_integer_digits(128))


def is_palindrome(_num: int):

    string_num = str(_num)
    lower_index = 0
    upper_index = len(string_num) - 1
    flag = False

    while lower_index < upper_index:
        if string_num[lower_index] == string_num[upper_index]:
            lower_index += 1
            upper_index -= 1
        else:
            flag = True
            break

    if not flag:
        print("Palindrome")
    else:
        print("Not palindrome")


a = 121
is_palindrome(a)
