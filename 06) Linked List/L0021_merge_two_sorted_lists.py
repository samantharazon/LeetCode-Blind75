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

###############################################################
# Function to merge the lists
# Takes two lists which are sorted
# joins them to get a single sorted list
def mergeLists(l1, l2):
    dummy = Node()
    tail = dummy

    while l1 and l2:
        if l1.data < l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    if l1:
        tail.next = l1
    elif l2:
        tail.next = l2

    return dummy.next
###############################################################

# Create 2 lists
listA = LinkedList()
listB = LinkedList()
listC = LinkedList()

# Add elements to the list in sorted order
listA.addToList(5)
listA.addToList(10)
listA.addToList(15)
print("\nList A: ")
listA.printList()

listB.addToList(2)
listB.addToList(3)
listB.addToList(20)
print("\nList B: ")
listB.printList()

# Call the merge function
listC.head = mergeLists(listA.head, listB.head)
print("\nMerged Linked List is:")
listC.printList()

print("\n")
