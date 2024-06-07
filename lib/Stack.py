class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit
    pass

    def isEmpty(self):
        return self.items == []
    pass

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
        pass

    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop()
        pass

    def peek(self):
        if self.isEmpty():
            return None
        return self.items[-1]  
        pass
    
    def size(self):
        length = len(self.items)
        return length
        pass

    def full(self):
        return len(self.items) == self.limit

    pass

    def search(self, target):
        for i in range(len(self.items) - 1, -1, -1):
            if self.items[i] == target:
                return len(self.items) - i - 1
        return -1
        pass
