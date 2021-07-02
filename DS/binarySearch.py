# Iterative Binary Search Function
# It returns index of x in given array arr if present,
# else returns -1


# def binary_search(arr, x):
#     low = 0
#     high = len(arr) - 1
#     mid = 0
#
#     while low <= high:
#
#         mid = (high + low) // 2
#
#         # If x is greater, ignore left half
#         if arr[mid] < x:
#             low = mid + 1
#
#         # If x is smaller, ignore right half
#         elif arr[mid] > x:
#             high = mid - 1
#
#         # Check if x is present at mid
#         else:
#             return mid
#
#             # If we reach here, then the element was not present
#     return -1
#
#
# # Test array
# arr = [2, 3, 4, 10, 40]
# x = 10
#
# # Function call
# result = binary_search(arr, x)
# print(result)


# BINARY SEARCH USING RECURSION


# Python3 Program for recursive binary search.

# Returns index of x in arr if present, else -1
def binarySearch(arr, l, r, x):
    # Check base case
    if r >= l:

        mid = l + (r - l) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)

        # Else the element can only be present
        # in right subarray
        else:
            return binarySearch(arr, mid + 1, r, x)

    else:
        # Element is not present in the array
        return -1


# Driver Code
arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binarySearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")
