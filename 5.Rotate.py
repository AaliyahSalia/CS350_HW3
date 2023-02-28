# Generate a function in clockwise rotation for each node (either char type or int type) in 
# doubly linked list by N places, e.g. given 
#     list = None<-Head<=>c<=>i<=>v<=>i>=>c->None, from function call 
#     rotate_DLL(list, 3), the output will be like this 
#     None<-Head<=>v<=>i<=>c<=>c>=>i->None

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

def rotate_DLL(head, N):
    if head is None or head.next is None:
        return head
    
    curr = head
    length = 0
    while curr is not None:
        length += 1
        curr = curr.next
    
    N = N % length
    
    if N == 0:
        return head
    
    curr = head
    for i in range(length-N):
        curr = curr.next
    new_head = curr
    
    curr = head
    while curr.next is not None:
        curr = curr.next
    
    curr.next = head
    head.prev = curr
    curr = new_head.prev
    curr.next = None
    new_head.prev = None
    
    return new_head

head = Node('c')
head.next = Node('i')
head.next.prev = head
head.next.next = Node('v')
head.next.next.prev = head.next
head.next.next.next = Node('i')
head.next.next.next.prev = head.next.next
head.next.next.next.next = Node('c')
head.next.next.next.next.prev = head.next.next.next
head.next.next.next.next.next = None

new_head = rotate_DLL(head, 3)

curr = new_head
while curr is not None:
    print(curr.val, end='<=>')
    curr = curr.next
print('None')
