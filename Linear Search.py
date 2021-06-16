
def linear_search(list=None, key=5):

    # if key in list:
    #     return True
    # return False

    for i in list:
        if i == key:
            return True

    return False


print(linear_search([2, 66, 32, 5, 1], 5))
