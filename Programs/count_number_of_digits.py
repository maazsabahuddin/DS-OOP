

def count_digits(num):

    count = 0
    while num > 0:
        num = num // 10
        count += 1

    return count


print(count_digits(56454645))


def prime_number_or_not(num):

    counter = 0
    if num < 1:
        print("Not PN")

    for val in range(num, 0, -1):
        if num % val == 0:
            counter += 1
    if counter == 2:
        print("Yes prime number")
    else:
        print("Not PM")


prime_number_or_not(3)
