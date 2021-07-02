

# def removeDuplicateNumbers(numbers=None):
#     new_list = numbers
#     for i in range(len(numbers)):
#         for j in range(i+1, len(numbers)):
#             if numbers[i] == numbers[j]:
#                 new_list.remove(numbers[i])
#     return new_list


def isExist(num, list):
    for i in list:
        if i == num:
            return False
    return True


def removeDuplicateNumbers(numbers=None):
    new_list = []
    for num in numbers:
        # if num not in new_list:
        if isExist(num, new_list):
            new_list.append(num)
    return new_list


print(removeDuplicateNumbers([1, 2, 2, 3, 4]))
