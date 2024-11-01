""" Python program to merge two
sorted linked lists """


# Linked List Node
class Node:
    def __init__(self, data=0):
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

###############################################################
# Function to reverse linked list (iterative)
def reverseLinkedList(head):
    prev = None
    tmp = head

    while tmp:
        next = tmp.next  # move next
        tmp.next = prev  # flip arrow
        prev = tmp  # move prev
        tmp = next  # move tmp
    return prev
###############################################################


# Create a linked list
list1 = LinkedList()

# Add elements to the list in sorted order
list1.addToList(1)
list1.addToList(2)
list1.addToList(3)
list1.addToList(4)
list1.addToList(5)
print("\nList 1: ")
list1.printList()

# Call the merge function
list1.head = reverseLinkedList(list1.head)
print("\nReverse Linked List is:")
list1.printList()

print("\n")
