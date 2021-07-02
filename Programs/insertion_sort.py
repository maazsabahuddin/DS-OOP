

list = [7, 8, 5, 2, 4, 6, 3, 2, 7]
sorted_list = [1, 2, 3, 4, 5, 6]


def insertion_sort(list=None):

    for index in range(1, len(list)):
        value = list[index]
        i = index - 1

        while i >= 0:

            if value < list[i]:
                list[i+1] = list[i]
                list[i] = value
                i -= 1
            else:
                break


insertion_sort(list)
print(list)
# print(sorted_list)
