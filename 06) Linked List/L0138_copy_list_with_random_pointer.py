class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

def printList(head):
    nodes = []
    cur = head
    while cur:
        nodes.append(f'Node({cur.val}, next={cur.next.val if cur.next else None}, random={cur.random.val if cur.random else None})')
        cur = cur.next
    print('\n -> '.join(nodes))

def createList(values, random_indices):
    nodes = [Node(val) for val in values]
    head = nodes[0] if nodes else None
    for i in range(1, len(nodes)):
        nodes[i-1].next = nodes[i]
    for node, rand_index in zip(nodes, random_indices):
        node.random = nodes[rand_index] if rand_index is not None else None
    return head

###############################################################
def copyRandomList(head):
    originalToCopy = {None: None}

    # Create a new node for each node in the original list and store the mapping
    original = head
    while original:
        copy = Node(original.val)
        originalToCopy[original] = copy
        original = original.next

    # Assign next and random Pointers
    original = head
    while original:
        copy = originalToCopy[original]
        copy.next = originalToCopy[original.next]
        copy.random = originalToCopy[original.random]
        original = original.next

    return originalToCopy[head]
###############################################################


values = [7, 13, 11, 10, 1]
random_indices = [None, 0, 4, 2, 0]
original_list = createList(values, random_indices)
print("\nOriginal list:")
printList(original_list)
copied_list = copyRandomList(original_list)
print("\nCopied list:")
printList(copied_list)

print("\n")
