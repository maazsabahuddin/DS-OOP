
''' MAAZ FIRST CLICK'''
def reverseWord(word=""):
    reversed = ""
    for i in range(len(word)-1, -1, -1):
        # print(word[i])
        reversed += word[i]
    return reversed


print(reverseWord("Maaz"))


# def reverseAWord(word):
#     reversed_word = ""