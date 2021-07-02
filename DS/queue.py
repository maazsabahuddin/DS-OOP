class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def enqueue_two_self_login(self, item):
        temp = []
        for i in range(len(self.items)):
            temp.append(self.items.pop())

        self.items.append(item)

        for value in temp:
            self.items.append(value)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


obj = Queue()
obj.enqueue(5)
obj.enqueue(10)
print(obj.items)
print(obj.isEmpty())
print(obj.size())
print(obj.dequeue())
