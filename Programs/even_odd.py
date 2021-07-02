
# print from 1 to n
def print_till_n_in_ascending_order(initial_value, n):
    if initial_value <= n:
        print(initial_value)
        return print_till_n_in_ascending_order(initial_value+1, n)


print_till_n_in_ascending_order(1, 10)


# using bitwise operator
def even_odd(n):
    if n & 1 == 0:
        print("Even")
    else:
        print("odd")


even_odd(9)


print(10/2)
