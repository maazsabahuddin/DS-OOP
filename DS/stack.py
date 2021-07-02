class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]
        # return self.items[-1]


# obj = Stack()
# obj.push(5)
# obj.push(10)
# print(obj.isEmpty())
# print(obj.peek())
