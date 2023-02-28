# Assuming that there are two circular linked lists l & m with char type node value from 
# a-zA-Z in non-descending sequence, find a function/method to extract common node 
# values from both and generate a new circular list without duplicated one.

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

def find_common_nodes(l, m):
    common = set()
    head1 = l
    while True:
        head2 = m
        while True:
            if head1.val == head2.val:
                common.add(head1.val)
            head2 = head2.next
            if head2 == m:
                break
        head1 = head1.next
        if head1 == l:
            break
    
    if not common:
        return None

    new_head = Node()
    new_tail = new_head
    for val in sorted(common):
        new_tail.next = Node(val)
        new_tail = new_tail.next
    new_tail.next = new_head.next
    return new_head.next

def print_circular_list(head: Node):
    if head is None:
        return
    curr = head
    while True:
        print(curr.val, end=" ")
        curr = curr.next
        if curr == head:
            break
    print()

l1 = Node("a")
l1.next = Node("b")
l1.next.next = Node("c")
l1.next.next.next = l1

l2 = Node("b")
l2.next = Node("c")
l2.next.next = Node("g")
l2.next.next.next = l2

common_list = find_common_nodes(l1, l2)

print_circular_list(common_list)
