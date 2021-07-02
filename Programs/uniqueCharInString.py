# Check if the string has all unique characters or not.
def uniqueCharInString(string="Maaz"):
    for i in range(len(string)):
        # print(word)
        for j in range(i+1, len(string)):
            if string[i] == string[j]:
                return False

    return True


# print(uniqueCharInString("Maz"))
