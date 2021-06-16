

def bubble_sort(list=None):

    flag = False
    for i in range(len(list)):

        for j in range(0, len(list)-i-1):

            if list[j] > list[j+1]:
                temp = list[j+1]
                list[j+1] = list[j]
                list[j] = temp
                flag = True
            else:
                pass

        if not flag:
            break

    return list


print(bubble_sort([1, 2, 3, 4, 5]))


def countSwaps(a):
    flag = False
    temp = 0
    swaps = 0
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j] > a[j + 1]:
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp
                flag = True
                swaps += 1

        if not flag:
            break

    if not flag:
        print("Array is sorted in 0 swaps.")
        print("First element: {}".format(a[0]))
        print("Last element: {}".format(a[-1]))
    else:
        print("Array is sorted in {} swaps".format(swaps))
        print("First element: {}".format(a[0]))
        print("Last element: {}".format(a[-1]))


# countSwaps([1, 2, 3, 4, 5])
# countSwaps([3, 2, 1])