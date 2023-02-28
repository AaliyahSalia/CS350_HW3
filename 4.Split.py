# Find a program to split from first N nodes into new circular linked list with int type 
# nodes while preserving the old nodes. For instance, org = Head->2->3->4->5->6->7->8
# ->Head, two new circular linked lists should be Head->2->3->4->Head and 
# Head->5->6->7->8->Head from the outputs of function call split_CLL(org, 3)

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

def split_CLL(head, n):
    if head is None:
        return None, None
    
    curr = head
    while curr.next != head:
        curr = curr.next
    last = curr
    
    curr = head
    for i in range(n-1):
        curr = curr.next
    nth = curr
    
    last.next = nth
    new_head = head
    remaining_head = nth.next
    nth.next = new_head
    
    return new_head, remaining_head


head = Node(2)
head.next = Node(3)
head.next.next = Node(4)
head.next.next.next = Node(5)
head.next.next.next.next = Node(6)
head.next.next.next.next.next = Node(7)
head.next.next.next.next.next.next = Node(8)
head.next.next.next.next.next.next.next = head

new_head, remaining_head = split_CLL(head, 3)

curr = new_head
while True:
    print(curr.val, end=" ")
    curr = curr.next
    if curr == new_head:
        break
print()

curr = remaining_head
while True:
    print(curr.val, end=" ")
    curr = curr.next
    if curr == head:
        break
print()
