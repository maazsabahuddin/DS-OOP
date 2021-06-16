

def balancedParanthesis(str):

    stack = []
    for char in str:
        if char in ["(", "[", "{"]:
            stack.append(char)
        else:
            if not stack:
                return False

            pop_element = stack.pop()
            if pop_element == "(" and char != ")":
                return False

            if pop_element == "[" and char != "]":
                return False

            if pop_element == "{" and char != "}":
                return False

    if stack:
        return False
    return True


print(balancedParanthesis("([])"))
print(['a', 'b'].pop())
