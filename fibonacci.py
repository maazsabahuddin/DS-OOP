

def fibonacci_series(n):
    n1 = 0
    n2 = 1
    count = 0
    while count < n:
        print(n1)
        sum = n1 + n2
        n1 = n2
        n2 = sum

        count += 1


# def recursion_fibonacci_series(n):

fibonacci_series(12)
