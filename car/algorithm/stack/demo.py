class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

q = Stack()
q.push(1)
q.push(1)
q.push(2)
q.push(3)

while not q.isEmpty():
    data = q.top()
    print(data)
    q.pop()
