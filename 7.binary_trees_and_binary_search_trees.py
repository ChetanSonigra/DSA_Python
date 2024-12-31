# Binary Trees:
# Root node, leaf node.
# parent, child node.
# self.val, self.left, self.right, - self.parent
# perfect tree: nothing is empty
# complete tree: all levels are filled exept last one. last one is filled from left to right.


# if represented in list: 
# left node of root node at - 2i position
# right node of root node at - 2i+1 position

# Height of tree: max number of nodes going from root to leaf node.

#   1
#  2     3
# 4 5  10

# DFS:  
# PREORDER: 1,2,4,5,3,10  - node,left, right
# INORDER: 4,2,5,1,10,3   - left, node, right
# POSTORDER: 4,5,2,10,3,1 - left, right, node

# BFS: Level order
# 1, 2, 3, 4, 5, 10

# DFS will be implemented with stack(recursion), while BFS will be implemented with queue.

# Time and Space complexity for BFS/DFS - O(n)

# Binary Search Tree: any node's left nodes are smaller and right nodes are bigger.
# Time Complexity: O(logn) - assuming heigh balanced tree.

# Inorder traversal will give sorted array.


# Binary Tree:

class Node:
    def __init__(self, val, left=None, right=None):
        self.val= val 
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.val)
    
A = Node(1)
B = Node(2)
C = Node(3)
D = Node(4)
E = Node(5)
F = Node(10)

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F

print(A)

# Recursive Preorder traversal: DFS: Time/Space = O(n)

def preorder_traversal(node):
    print(node)
    if node.left:
        preorder_traversal(node.left)
    if node.right:
        preorder_traversal(node.right)

preorder_traversal(A)

def inorder_traversal(node):
    if not node:
        return
    inorder_traversal(node.left)
    print(node)
    inorder_traversal(node.right)

inorder_traversal(A)

def postorder_traversal(node):
    if not node:
        return
    postorder_traversal(node.left)
    postorder_traversal(node.right)
    print(node)

postorder_traversal(A)

# iterative approach:

def preorder_iterative(node):
    stk = [node]

    while stk:
        node = stk.pop()
        print(node)
        if node.right: stk.append(node.right)
        if node.left: stk.append(node.left)

preorder_iterative(A)



# BFS: LEVEL ORDER TRAVERSAL

from collections import deque
def levelorder_traversal(node):
    q = deque()
    q.append(node)

    while q:
        node = q.popleft()
        print(node)
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)
    

levelorder_traversal(A)

# search for an element:

def search(node, target):
    if not node:
        return False
    if node.val == target:
        return True
    
    return search(node.left,target) or search(node.right, target)

print(search(A,5))
print(search(A,11))


# Binary Search Tree

A, B, C, D, E, F, G = Node(5), Node(-1), Node(1), Node(3),Node(8), Node(7), Node(9)

A.left, A.right = C, E
C.left, C.right = B, D
E.left, E.right = F, G

print(A)
inorder_traversal(A)

# time, space complexity: O(n)
def search_bst(node, target):
    if not node:
        return False
    
    if node.val== target:
        return True
    elif node.val>target:
        return search_bst(node.left, target)
    else:
        return search_bst(node.right, target)
    
print(search_bst(A,7))
print(search_bst(A,-1))
print(search_bst(A, 44))