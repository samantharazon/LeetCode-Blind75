
class ListNode: 
    def __init__(self, val=0, next=None): 
        self.val = val 
        self.next = next

# Helper function to create a linked list from a list of values 
def createLinkedList(values): 
    if not values: 
        return None 
    head = ListNode(values[0])
    current = head 
    for value in values[1:]: 
        current.next = ListNode(value) 
        current = current.next 
    return head

# Helper function to print the linked list 
def printLinkedList(head): 
    current = head 
    while current: 
        print(current.val, end=" -> ") 
        current = current.next 

###############################################################
def middleNode(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow
###############################################################

values = [1, 2, 3, 4, 5] 
head = createLinkedList(values) 
print("\nOriginal linked list:") 
printLinkedList(head) 
middle = middleNode(head) 
print("\nMiddle node value:", middle.val)
# Output: 3
# The middle node of the list is node 3.

values = [1, 2, 3, 4, 5, 6]
head = createLinkedList(values) 
print("\nOriginal linked list:") 
printLinkedList(head) 
middle = middleNode(head) 
print("\nMiddle node value:", middle.val)
# Output: 4
# xplanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 

print("\n")