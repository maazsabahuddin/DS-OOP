
def find_duplicate_numbers(arr):

    _dict = {}
    for value in arr:
        if _dict.get(value):
            _dict.update({value: _dict.get(value)+1})
        else:
            _dict.update({value: 1})

    return _dict


print(find_duplicate_numbers([1, 1, 2, 3, 4, 5, 3, 6]))
