from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = OrderedDict()
        self.size = 0

    def get(self, key, default=None):
        return self.data.get(key, default)

    def put(self, key, value):
        self.data[key] = value
        self.size += 1
        if self.size > self.capacity:
            self.data.popitem(last=False)
            self.size -= 1

    def __len__(self):
        return self.size
