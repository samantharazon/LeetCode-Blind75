class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        # Initialize dummy nodes
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # Remove a node from the doubly linked list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # Insert a node at the rightmost position (most recent)
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    # Return the value of the node if the key exists, otherwise return -1
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    # Add a key-value pair to the cache
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        # Remove the least recently used node if the cache exceeds capacity
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

lru = LRUCache(2)
lru.put(1, 1)
lru.put(2, 2)
print("\n(a)")
print(lru.get(1))  # should return 1
lru.put(3, 3)      # evicts key 2
print("\n(b)")
print(lru.get(2))  # should return -1 (not found)
lru.put(4, 4)      # evicts key 1
print("\n(c)")
print(lru.get(1))  # should return -1 (not found)
print("\n(d)")
print(lru.get(3))  # should return 3
print("\n(e)")
print(lru.get(4))  # should return 4

print("\n")