


# arr = [1,4,3,2]
# for i in range(len(arr)-1, -1, -1):
#     print(arr[i])


# a = {1: 2, 2: 3}
# if a.get(4):
#     print(True)


# a = []
# try:
#     if a[0]:
#         print("exist")
# except IndexError:
#     print("No")

# if a[0]:
#     print(True)


def staircase(n):

    for stairs in range(1, n + 1):
        print(' ' * (n - stairs) + '#' * stairs)


def miniMaxSum(arr):

    sum = min = max = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < min:
            min = arr[i]
        if arr[i] > max:
            max = arr[i]
        sum += arr[i]

    print("{} {}".format(sum-max, sum-min))
    # max = 0
    # min = 1000
    # for i in range(len(arr)):
    #     sum = 0
    #     for j in range(len(arr)):
    #         if j == i:
    #             pass
    #         else:
    #             sum += arr[j]
    #
    #     if sum > max:
    #         max = sum
    #     if sum < min:
    #         min = sum
    #
    # print("{} {}".format(min, max))


# staircase(6)
# miniMaxSum([1, 2, 3, 4, 5])


# Complete the isBalanced function below.
def isBalanced(s):

    list = []
    for i in s:
        if not list:
            list.append(i)
        else:
            value = list[-1]
            if value == '[' and i == ']':
                list.pop()
            elif value == '{' and i == '}':
                list.pop()
            elif value == '(' and i == ')':
                list.pop()
            else:
                list.append(i)

    if not list:
        print("YES")
    else:
        print("NO")


# s = "[]{()}"
# isBalanced(s)


# def Lcm(arr1, arr2):
#
#     lcm = greater = max(arr1)
#     i = 0
#     while i < len(arr1):
#         if lcm % arr1[i] == 0 and lcm % arr1[i+1] == 0:
#             lcm = greater
#             break
#         greater += 1
#         i -= 1
#
#     for i in range(len(arr1)-1):
#         if lcm % arr1[i] == 0 and lcm % arr1[i+1] == 0:
#             lcm =


def myFunc():

    def say():
        print("Wrapper")
    return say


obj = myFunc()
obj()
