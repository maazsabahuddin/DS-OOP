
# def minimum_value_in_unsorted_array(list=None):
#
#     min = 0
#     for i in list:
#         if i < min:
#             min = i
#
#     print(min)
#
#
# minimum_value_in_unsorted_array([32, 1, 63, -22, 5])


def findSmallestDivisor(s, t):
    # Write your code here
    u = ''
    if t in s:
        range = len(s) // 2
        u = s[:range]
        if u*2 in s and t:
            range = range // 2
            u = s[:range]
            if u*4 in s and t:
                return range
            else:
                return range*2
        else:
            return range*2

    return -1


# print(findSmallestDivisor("lrbb", "lrbb"))
# print(findSmallestDivisor("rbrb", "rbrb"))
print(findSmallestDivisor("100100", "100"))
# print(findSmallestDivisor("bcdbcdbcdbcd", "bcdbcd"))
