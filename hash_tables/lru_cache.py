"""146. LRU Cache - https://leetcode.com/problems/lru-cache/"""

# In Python 3.6+ dictionaries are ordered.
# Time complexity get and put - O(1)

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
       
    def get(self, key: int) -> int:
        value = self.cache.pop(key, None)
        if value:
            self.cache[key] = value
            return value
        return -1
       
    def put(self, key: int, value: int) -> None:
        old_value = self.cache.pop(key, None)
        if old_value:
            self.cache[key] = value
        else:
            if len(self.cache.keys()) == self.capacity:
                self.cache.pop(next(iter(self.cache)))
            self.cache[key] = value


