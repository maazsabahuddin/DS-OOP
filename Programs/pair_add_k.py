

def pair_problem(arr, k):

    _dict = {}
    for value in arr:
        if _dict.get(k-value):
            return True
        else:
            _dict.update({value: value})

    return False


print(pair_problem(arr=[1, 2, 3, 4, 5], k=9))
