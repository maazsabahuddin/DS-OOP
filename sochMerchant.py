
def sockMerchant(n, arr):

    count = 1
    matching_pairs = 0
    pair = {}
    for i in range(n-1):
        for j in range(i+1, n):
            if arr[i] == arr[j]:
                count += 1

        if count % 2 == 0:
            if not pair.get(arr[i]):
                pair.update({arr[i]: count/2})
                matching_pairs += count/2
            count = 1
        elif count % 2 == 1:
            if count != 1:
                if not pair.get(arr[i]):
                    pair.update({arr[i]: (count-1)/2})
                    matching_pairs += (count-1)/2
                count = 1

        print(pair)
    return matching_pairs


def sumArray(arr):

    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    print(sum)


# Complete the compareTriplets function below.
# Complete the compareTriplets function below.
def compareTriplets(a, b):
    points = [0, 0]

    if len(a) == len(b):
        for i in range(len(a)):
            if a[i] < b[i]:
                points[1] += 1

            elif a[i] > b[i]:
                points[0] += 1
            else:
                pass

        return points


def diagonalDifference(arr):

    right_to_left_sum = 0
    left_to_right_sum = 0

    # Write your code here
    for i in range(len(arr)):

        for j in range(len(list)):

            if i == j:
                left_to_right_sum += arr[i][j]
            if i == len(arr)-j-1:
                right_to_left_sum += arr[i][j]

    return abs(left_to_right_sum - right_to_left_sum)


# Complete the plusMinus function below.
def plusMinus(arr):
    list = [0, 0, 0]
    for i in arr:
        if i > 0:
            list[0] += 1
        elif i < 0:
            list[1] += 1
        else:
            list[2] += 1

    for i in list:
        print(round(i / len(arr), 6))


if __name__ == '__main__':
    # arr = [1, 2, 1, 2, 1, 3, 2, 1]
    # n = len(arr)

    # print(sockMerchant(n, arr))
    # sumArray([1, 2, 3, 4, 10, 11])

    # print(compareTriplets([5, 6, 7], [3, 6, 10]))
    # print(compareTriplets([5, 9, 7], [3, 8, 10]))

    # list = [
    #     [1, 2, 3],
    #     [4, 5, 6],
    #     [9, 8, 9]
    # ]
    # print(diagonalDifference(list))

    plusMinus([-4, 3, -9, 0, 4, 1])
