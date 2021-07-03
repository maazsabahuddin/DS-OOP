# Print prime number upto n times
def primeNumber(n):
    prime_numbers = []
    for i in range(1, n+1):
        counter = 0
        for num in range(i, 0, -1):
            if i % num == 0:
                counter += 1
        if counter == 2:
            prime_numbers.append(i)

    return prime_numbers


print(primeNumber(11))


def primeNumberInBetween(lower=None, upper=None):
    prime_numbers = []
    for i in range(lower, upper + 1):
        flag = False
        if i > 1:
            for num in range(2, i):
                if (i % num) == 0:
                    flag = True
                    break
            if not flag:
                prime_numbers.append(i)
            # else:
            #     prime_numbers.append(i)
    return f"Prime numbers between {lower} and {upper} are: {prime_numbers}"


lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))
print(primeNumberInBetween(lower, upper))
