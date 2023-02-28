# In an open farmland where a hare (similar as rabbit) lives, it usually sleeps in any suitable 
# place, continually shifting from one place to another in total 10 nests labeled from 1 to 10.
# But a wolf lives in the same area, hunting to check 10 nests in the manner as follows: 
# - start to check from label 1 nest
# - then skip one nest (label 2) to check label 3
# - increase skipped checking number to 2 (skip label 4 and label 5) and look for it in 
# label 6
# - keep increasing skipped number to 3 to check label 10
# - go back to count from label 1 by increasing skipped number to 4 and so on
# Write a program to help this hare to make a decision which nests are safe to sleep, 
# maybe doesn't exist at all after the wolf checked n times
# Hint: create a circular linked list and traverse one by one circularly.


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def safe_nests(n, m):
    head = Node(1)
    prev = head
    if n == 0 and m == 0:
        return None
    for i in range(2, n + 1):
        prev.next = Node(i)
        prev = prev.next
    prev.next = head

    current_node = head
    while current_node.next != current_node:
        for i in range(m - 1):
            current_node = current_node.next
        next_node = current_node.next
        current_node.next = next_node.next
        next_node.next = None
        current_node = current_node.next
    return current_node.data


n = 5
m = 3
print("The hare can sleep safely in nest", safe_nests(n, m))
