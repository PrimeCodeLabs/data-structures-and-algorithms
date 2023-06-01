from collections import OrderedDict

# Efficient version
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)  # move the accessed item to the end
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # remove the least recently used item

# Inefficient version
class LRUCacheInefficient:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.order = []

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.order.remove(key)  # costly operation
        self.order.append(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.order.remove(key)  # costly operation
        else:
            if len(self.cache) == self.capacity:
                lru_key = self.order.pop(0)  # costly operation
                del self.cache[lru_key]
        self.order.append(key)
        self.cache[key] = value

'''
Time and Space Complexity
For the efficient version:

The get and put operations have a time complexity of O(1) due to the use of an OrderedDict, which allows constant time insertions, deletions, and lookups.
The space complexity is O(capacity) because the cache will at most store "capacity" number of elements.
For the inefficient version:

The get and put operations have a time complexity of O(n) because in the worst-case scenario, we may need to look through all the elements in the order list.
The space complexity is also O(capacity) because the cache will at most store "capacity" number of elements. However, it also maintains an additional list of the same size, so it uses more space compared to the efficient version.

'''