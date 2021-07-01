

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


print(reverse_string("Maaz"))
reverse_string_recursion("Maaz")
