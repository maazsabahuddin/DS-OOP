
# Finding divisors of a number lets say 6
# its dividends are 1,2,3


def findDivisors(number):
    divisors = []
    for i in range(1, number):
        if number % i == 0:
            divisors.append(i)
    return divisors


print(findDivisors(600))
print(60 % 2)
print(2 % 60)


def primeNumber(n):
    prime_number = []
    for i in range(1, n+1):
        counter = 0
        for num in range(i, 0, -1):
            if i % num == 0:
                counter = counter + 1

        if counter == 2:
            prime_number.append(i)

    return prime_number


print(primeNumber(10))
