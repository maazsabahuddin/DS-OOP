# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        pass


# obj = Solution()
# obj.addTwoNumbers(obj, [2, 4, 3], [5, 6, 4])


def addTwoListsData(l1, l2):
    sumList = []
    for i in range(len(l1)):
        sum = l1[i] + l2[i]
        sumList.append(sum)

    return sumList


print(addTwoListsData([1, 2, 3], [1, 2, 3]))
