def gradingStudents(grades):
    # Write your code here
    for grade in range(len(grades)):
        if grades[grade] < 38:
            pass
        elif grades[grade] % 5 == 4:
            grades[grade] = grades[grade] + 1

        elif grades[grade] % 5 == 3:
            grades[grade] = grades[grade] + 2

    return grades


# print(gradingStudents([4, 73, 67, 38, 33]))


# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_list = []
    orange_list = []

    for fruit in apples:
        apple_list.append(a + fruit)

    for fruit in oranges:
        orange_list.append(b + fruit)

    count = 0
    for apple in apple_list:
        if s <= apple <= t:
            count += 1
    print(count)

    countOrange = 0
    for orange in orange_list:
        if s <= orange <= t:
            countOrange += 1
    print(countOrange)


# countApplesAndOranges(7, 11, 5, 15, [-2, 2, 1], [5, -6])


# Kangaroo Problem
# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):

    flag = False
    while True:

        if (x1 > x2 and v1 >= v2) or (x2 > x1 and v2 >= v1):
            break

        elif x1 > x2:
            x1 += v1
            x2 += v2
            if x1 < x2:
                break
            elif x1 == x2:
                flag = True
                break

        elif x2 > x1:
            x1 += v1
            x2 += v2
            if x2 < x1:
                break
            elif x1 == x2:
                flag = True
                break

        elif x1 == x2:
            flag = True
            break

    if flag:
        return "YES"
    return "NO"


# kangaroo(0, 2, 5, 3)
# print(kangaroo(0, 3, 4, 2))
print(kangaroo(43, 2, 70, 2))
