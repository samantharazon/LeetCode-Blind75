""" Python program to merge two
sorted linked lists """


# Linked List Node
class Node:
    def __init__(self, data = 0):
        self.data = data
        self.next = None

# Create & Handle List operations
class LinkedList:
    def __init__(self):
        self.head = None        

    # Method to display the list
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

    # Method to add element to list
    def addToList(self, newData):
        newNode = Node(newData)     # create a new node
        if self.head is None:
            self.head = newNode
            return

        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = newNode

    def get_node(self, index):
        current = self.head
        for i in range(index):
            current = current.next
            if current is None:
                return None
        return current

###############################################################
# Function to determine if the linked list has a cycle in it.
def hasCycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    
    return False
###############################################################

# Create list
listA = LinkedList()

# Add elements to the list in sorted order
listA.addToList(5)
listA.addToList(2)
listA.addToList(0)
listA.addToList(4)


# print list
listA.printList()

# ===================
# Create the cycle
# ===================

# listA.head.next.next.next = listA.head
tail_index = 3
last_node = listA.get_node(tail_index)

pos_tail_next = 1
last_node.next = listA.get_node(pos_tail_next)

# ===========================
# Check if there is a cycle
# ===========================

# call the has cycle function
result = hasCycle(listA.head)

# print result
print("\nCycle:", result)

# print list
# listA.printList()
