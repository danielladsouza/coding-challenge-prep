"""146. LRU Cache - https://leetcode.com/problems/lru-cache/

LRU Cache The idea is that everytime an element is accessed (either via a get or a put, it goes to the end of a sequence.
This ensures that the elements that were least recently accessed stay at the beginning of the sequence, making it easy to 
evict.)

Prior to Python 3.6, the dictionary did not maintain order. 
To ensure ordering, we use a dictionary and a linked list.

The cache will be a dictionary<key, LinkedListNode>
"""

# Let's implement the LinkedListNode
# This is a doubly linked list
class LinkedListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = self.next = None
        
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = LinkedListNode(0,0)
        self.tail = LinkedListNode(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
     
    def cut(self, node:LinkedListNode):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
        
    def insert(self, node:LinkedListNode):
        p = self.tail.prev
        p.next = node
        node.prev = p
        node.next = self.tail
        self.tail.prev = node
        
    def get(self, key: int) -> int:
        node = self.cache.get(key, None)
        if node:
            self.cut(node)
            self.insert(node)
            return node.value
        return -1
        
    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key, None)
        if node: # Upsert
            node.value = value
            self.cut(node)
            self.insert(node)
        else:
            # This should be done later, as we do not know if we are inserting a new entry or updating an existing one
            if len(self.cache.keys()) == self.capacity:
                evict_node = self.head.next
                self.cut(evict_node)
                del self.cache[evict_node.key]
            new_node = LinkedListNode(key, value)
            self.insert(new_node)
            self.cache[key] = new_node
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
