

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
def reorderList(head):
    if not head:
        return 

    #find the middle node
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    #reverse the second part of the list
    prev, curr = None, slow
    while curr: 
        after = curr.next   # move after
        curr.next = prev    # reverse curr's arrow
        prev = curr         # move prev
        curr = after        # move curr

    # Merge the two halves
    firstHalf = head
    secondHalf = prev # prev points at head of reversed second list
    while secondHalf.next:
        # Store the next pointers temporarily
        tempFirstNext = firstHalf.next
        tempSecondNext = secondHalf.next
        
        # Reassign pointers to rearrange the links
        firstHalf.next = secondHalf
        firstHalf = tempFirstNext
        
        secondHalf.next = firstHalf
        secondHalf = tempSecondNext
###############################################################

values = [1, 2, 3, 4] 
head = createLinkedList(values) 
print("\nOriginal linked list:") 
printLinkedList(head) 
reorder_list = reorderList(head) 
print("\nReordered linked list:") 
printLinkedList(head) 
# Output: [1,4,2,3]

values = [1,2,3,4,5]
head = createLinkedList(values) 
print("\n\nOriginal linked list:") 
printLinkedList(head) 
reorder_list = reorderList(head) 
print("\nReordered linked list:") 
printLinkedList(head) 
# Output: [1,5,2,4,3]

print("\n")