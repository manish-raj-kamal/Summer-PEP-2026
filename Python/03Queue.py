class arrayqueue:
    def __init__(self):
        self.items = []
        self.front = 0
        self._size = 0

    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.items[self.front]

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        answer = self.items[self.front]
        self.items[self.front] = None  # Help with garbage collection
        self.front = (self.front + 1) % len(self.items)
        self._size -= 1
        if self._size == 0:
            self.front = 0
        return answer
    
    def enqueue(self, item):
        if self._size == len(self.items):
            self.__resize(max(1, 2 * len(self.items)))
        avail = (self.front + self._size) % len(self.items)
        self.items[avail] = item
        self._size += 1

    def __resize(self, new_capacity):
        old_items = self.items
        self.items = [None] * new_capacity
        walk = self.front
        for k in range(self._size):
            self.items[k] = old_items[walk]
            walk = (1 + walk) % len(old_items)
        self.front = 0


