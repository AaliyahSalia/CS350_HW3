# Check whether there exists random pointer in doubly linked list or not and 
# correct it by a program.

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
        self.random = None


def has_random_pointer(head):
    curr = head
    while curr is not None:
        if curr.random is not None:
            return True
        curr = curr.next
    return False

def correct_random_pointer(head):
    if not has_random_pointer(head):
        return head

    mapping = {}
    curr = head
    while curr is not None:
        copy = Node(curr.val)
        mapping[curr] = copy
        curr = curr.next

    curr = head
    while curr is not None:
        copy = mapping[curr]
        if curr.random is not None:
            copy.random = mapping[curr.random]
        curr = curr.next

    return mapping[head]

head = Node(1)
head.next = Node(2)
head.next.prev = head
head.next.next = Node(3)
head.next.next.prev = head.next
head.random = head.next.next
head.next.random = head
head.next.next.random = head.next

curr = head
while curr is not None:
    print(f"Node({curr.val}) -> Node({curr.random.val if curr.random is not None else None})")
    curr = curr.next

print(f"Has random pointer? {has_random_pointer(head)}")

new_head = correct_random_pointer(head)

curr = new_head
while curr is not None:
    print(f"Node({curr.val}) -> Node({curr.random.val if curr.random is not None else None})")
    curr = curr.next
