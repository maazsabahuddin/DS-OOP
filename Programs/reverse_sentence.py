

def reverse_sentence(word):

    arr = word.split(" ")
    reverse_sentence_value = []
    for value in arr:
        reverse_sentence_value.insert(0, value)
    print(' '.join(reverse_sentence_value))
    reverse_sentence_string = ""
    for val in reverse_sentence_value:
        reverse_sentence_string += " " + val

    return reverse_sentence_string


print(reverse_sentence("Hello World"))
