

def reverse_string(string):

    reverse_value = ""
    for i in range(len(string)-1, -1, -1):
        reverse_value += string[i]

    return reverse_value


def reverse_string_recursion(string):

    if len(string) == 0:
        return

    reverse_string_recursion(string[1:])
    print(string[0], end='')


def reverse_string_using_stack(string):

    arr = []
    for value in string:
        arr.append(value)

    reverse_value = ""
    for val in range(len(arr)):
        reverse_value += arr.pop()

    return reverse_value


print(reverse_string("Maaz"))
# reverse_string_recursion("Maaz")
# print(reverse_string_using_stack("Maaz"))
