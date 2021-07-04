
def occurrence_of_string(string):

    _dict = {}
    for value in string:
        count = _dict.get(value)
        if count:
            _dict.update({value: count+1})
        else:
            _dict.update({value: 1})

    return _dict


def first_letter_occurrence(string):

    _dict = {}
    for value in string:
        count = _dict.get(value)
        if count:
            _dict.update({value: count+1})
        else:
            _dict.update({value: 1})

    for i in string:
        value = _dict.get(i)
        if value == 1:
            return i

    return "No value occurred twice"


print(occurrence_of_string("Maaz"))
print(first_letter_occurrence("Maaz"))
