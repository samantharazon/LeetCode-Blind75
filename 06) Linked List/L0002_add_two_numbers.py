

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
def addTwoNumbers(l1, l2):
        dummy = ListNode()
        cur = dummy

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0 # missing nodes are treated as having a value of 0
            v2 = l2.val if l2 else 0

            # new digit     (any digit greater than 9 needs to be split into its carry and the current digit)
            val = v1 + v2 + carry
            carry = val // 10       # val//10 gives the tens digit (ex: if val is 24, carry will be set to 2)
            val = val % 10          # val%10 gives the single digit (e: if val is 24, val will be set to 4)
            cur.next = ListNode(val)

            # update pointers
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
###############################################################

values1 = [2,4,3]
values2 = [5,6,4]
list1 = createLinkedList(values1) 
list2 = createLinkedList(values2) 
print("\nlinked list 1:") 
printLinkedList(list1) 
print("\nlinked list 2:") 
printLinkedList(list2) 
newList = addTwoNumbers(list1, list2) 
print("\nNew linked list:") 
printLinkedList(newList)


values1 = [5,6,4]
values2 = [2, 4, 3, 3]
list1 = createLinkedList(values1) 
list2 = createLinkedList(values2) 
print("\n\nlinked list 1:") 
printLinkedList(list1) 
print("\nlinked list 2:") 
printLinkedList(list2) 
newList = addTwoNumbers(list1, list2) 
print("\nNew linked list:") 
printLinkedList(newList)

print("\n")