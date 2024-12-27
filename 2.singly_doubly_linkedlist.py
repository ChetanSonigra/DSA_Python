# class Node object which points to next node in list.

# node.value, node.next
# last node.next = None
# first node = Head

# insertion, deletion, access, checking existence = O(n)
# to add/remove front element = O(1)

# Doubly linked list:
# node.value, node.next, node.prev


# 1. singly linked list:

class SinglyNode:
    def __init__(self,value, next_node=None):
        self.val = value
        self.next = next_node
    def __str__(self):
        return str(self.val)
    
Head = SinglyNode(1)
A = SinglyNode(3)
B = SinglyNode(5)
C = SinglyNode(8)
Head.next = A
A.next = B
B.next = C
C.next = None

print(Head)

# Traverse the linked list: O(N)

curr = Head
while curr:
    print(curr)
    curr = curr.next

# Display Linked List: O(N)
def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr))
        curr = curr.next
    print(' -> '.join(elements))

display(Head)

# Search for node value - O(N)

def search(head, val):
    curr = head
    while curr.next:
        if curr.val == val:
            return True
        curr = curr.next
    return False

print(search(Head,9), search(Head,5))


# Doubly Linked List

class DoublyNode:
    def __init__(self, value, next_node = None, prev_node = None):
        self.val = value
        self.next = next_node
        self.prev = prev_node

    def __str__(self):
        return str(self.val)
    
Head = Tail = DoublyNode(1)

print(Tail)

# display doubly linked list: O(n)

def display(head: DoublyNode):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next

    print(' <-> '.join(elements))

display(Head)

# Insert at beginning - O(1)

def insert_at_beginning(head, tail, value):
    new_node = DoublyNode(value,next_node=head)
    head.prev = new_node
    return new_node, tail

display(insert_at_beginning(Head, Tail, 2)[0])
