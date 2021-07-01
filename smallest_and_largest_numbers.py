
def smallest_and_largest_numbers(arr):

    smallest = arr[0]
    largest = arr[0]

    for value in arr:
        if value < smallest:
            smallest = value

        elif value > largest:
            largest = value

    return smallest, largest


print(smallest_and_largest_numbers([1, 2, 3, 100, -100, 21, 1123]))
