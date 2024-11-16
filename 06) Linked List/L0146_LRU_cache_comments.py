# lru_cache_with_logs.py

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # Map key to node

        # Initializing the left (LRU) and right (MRU) pointers as dummy Nodes (LRU=leastRecentlUsed) (MRU=mostRecentlyUsed)
        self.left, self.right = Node(0, 0), Node(0, 0) 
        self.left.next, self.right.prev = self.right, self.left #left = leastrecent, right = mostrecent

    # Remove a node from the linked list
    def remove(self, node):
        print(f"Removing node with key:{node.key}, value:{node.val}")
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # Insert a node at the rightmost position before the right pointer
    def insert(self, node):
        print(f"Inserting node with key:{node.key}, value:{node.val}")
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    # Return the value of the node if the key exists, otherwise return -1
    def get(self, key: int) -> int:
        if key in self.cache:
            print(f"Get key:{key} found with value: {self.cache[key].val}")
            # Update the node to be the most recently used
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            self.print_cache()
            print("Returned Value:")
            return self.cache[key].val
        print(f"Get key:{key} not found")
        self.print_cache()
        return -1

    # Add a key-value pair to the cache
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            print(f"Update key:{key} with new value:{value}")
            # Remove the old node from the list
            self.remove(self.cache[key])
        else:
            print(f"Put key:{key}, value:{value}")
        # Insert the new node
        self.cache[key] = Node(key, value) # Insert into the hashmap 
        self.insert(self.cache[key]) # Insert into the doubly linked list
        # If cache exceeds capacity, remove the LRU (least recently used) item from the hashmap
        if len(self.cache) > self.cap:
            lru = self.left.next
            print(f"Cache is full. Removing least recently used key:{lru.key}")
            self.remove(lru)
            del self.cache[lru.key]
        self.print_cache()

    # Print the current state of the cache
    def print_cache(self):
        node = self.left.next
        cache_state = []
        while node != self.right:
            cache_state.append(f"({node.key}: {node.val})")
            node = node.next
        print("Cache state:", " -> ".join(cache_state))


lru = LRUCache(2)
print("\n(A)")
lru.put(1, 1)

print("\n(B)")
lru.put(2, 2)

print("\n(C)")
print(lru.get(1))  # should return 1

print("\n(D)")
lru.put(3, 3)      # evicts key 2

print("\n(E)")
print(lru.get(2))  # should return -1 (not found)

print("\n(F)")
lru.put(4, 4)      # evicts key 1

print("\n(G)")
print(lru.get(1))  # should return -1 (not found)

print("\n(H)")
print(lru.get(3))  # should return 3

print("\n(I)")
print(lru.get(4))  # should return 4

print("\n")