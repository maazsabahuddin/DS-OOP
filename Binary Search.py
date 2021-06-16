

list = [1, 5, 21, 33, 65, 81, 90]


def binary_search(key):

    lower_bound = 0
    upper_bound = len(list) - 1
    mid = int((lower_bound + upper_bound) / 2)

    while lower_bound <= upper_bound:
        if list[mid] == key:
            return True
        elif list[mid] < key:
            lower_bound = mid + 1
            mid = int(lower_bound + (upper_bound - lower_bound) / 2)
        else:
            upper_bound = mid - 1
            mid = int(lower_bound + (upper_bound - lower_bound) / 2)

    return False


def binary_search_recursion(list, key, lower_bound, upper_bound):

    mid = int((lower_bound + upper_bound) / 2)
    if list[mid] == key:
        return True
    elif lower_bound == upper_bound:
        return False
    elif list[mid] < key:
        return binary_search_recursion(list, key, mid + 1, upper_bound)
    elif list[mid] > key:
        return binary_search_recursion(list, key, lower_bound, mid - 1)


print(binary_search(50))
# print(binary_search_recursion(list, 90, 0, len(list)-1))
