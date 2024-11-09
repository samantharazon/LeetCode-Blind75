

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
        print(current.val, end="")
        current = current.next
        if current:
            print(" -> ", end="")

###############################################################
def removeNthFromEnd(head, n):
    dummy = ListNode(0, head)
    left = dummy
    right = head

    # Move the right pointer so it is n nodes ahead of the left pointer
    while n > 0:
        right = right.next
        n -= 1

    # Move both pointers until the right pointer reaches the end of the list
    # This ensures the left pointer is just before the node to be removed
    while right:
        left = left.next
        right = right.next

    # Remove the nth node from the end by skipping it
    left.next = left.next.next
    
    # Return the head of the updated list
    return dummy.next
###############################################################

values = [1, 2, 3, 4, 5] 
n = 2
head = createLinkedList(values) 
print("\nOriginal linked list:") 
printLinkedList(head) 
newList = removeNthFromEnd(head, 2) 
print("\nReordered linked list:") 
printLinkedList(newList)
# Output: [1,2,3,5] 
# We want to remove the nth node from the ***END*** of the list
# so we remove the value 4 because it is the second node from the end of the list 


print("\n")