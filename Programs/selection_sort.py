
list = [7, 8, 5, 2, 4, 6, 3]


def selection_sort(list=None):

    for i in range(len(list)-1):

        min_index = i

        for j in range(i+1, len(list)):

            if list[j] < list[min_index]:
                min_index = j

        if min_index != i:
            temp = list[min_index]
            list[min_index] = list[i]
            list[i] = temp


selection_sort(list)
print(list)
