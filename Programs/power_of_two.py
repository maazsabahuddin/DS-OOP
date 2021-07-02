

def is_power(arr):

    result = []
    for num in arr:
        temp = 0
        flag = False

        while True:
            if 2 ** temp > num:
                break
            elif 2 ** temp == num:
                flag = True
                break
            else:
                temp += 1

        if flag:
            result.append(1)
        else:
            result.append(0)

    return result


print(is_power([1, 3, 8, 12, 16]))
