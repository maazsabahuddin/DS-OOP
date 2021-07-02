
def minimumValueInArray(list):
    smallest_value = -14520
    for i in range(len(list)-1):
        if list[i] < list[i+1]:
            smallest_value = list[i]
    return smallest_value


print(minimumValueInArray([32, 1, 63, -22, 5]))
