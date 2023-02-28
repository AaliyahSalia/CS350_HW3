# Given a circular linked list with int type value at each node, write a program to delete all  
# prime number nodes, such as m= Head->13->12->15->14->Head, after calling 
# delete_prime_CLL(m), you will get Head->12->15->14->Head

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def delete_prime_CLL(head: Node) -> Node:
    if head is None:
        return None
    curr = head
    prev = None
    while True:
        if is_prime(curr.val):
            if prev is None:
                head = curr.next
            else:
                prev.next = curr.next
            curr = curr.next
        else:
            prev = curr
            curr = curr.next
        if curr == head:
            break
    return head

# create the circular linked list
m = Node(13)
m.next = Node(12)
m.next.next = Node(15)
m.next.next.next = Node(14)
m.next.next.next.next = m

# delete the prime number nodes
m = delete_prime_CLL(m)

# print the modified circular list
curr = m
while True:
    print(curr.val, end=" ")
    curr = curr.next
    if curr == m:
        break
