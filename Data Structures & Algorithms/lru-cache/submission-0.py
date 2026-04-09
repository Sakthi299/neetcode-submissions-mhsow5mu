class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
        #self.cache.pop(node.key)

    def insert(self, node):
        prev, nxt_node = self.right.prev, self.right
        prev.next = nxt_node.prev = node
        node.prev = prev
        node.next = nxt_node

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # hashmap maps key to Node

        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            self.cache.pop(lru.key)
            # del self.cache[lru.key]
