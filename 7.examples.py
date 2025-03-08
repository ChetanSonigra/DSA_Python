"""
INVERT BINARY TREE

Given the root of a binary tree, invert the tree, and return its root.

 

Example 1:


Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Example 2:


Input: root = [2,1,3]
Output: [2,3,1]
Example 3:

Input: root = []
Output: []

"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return root
        curr = root
        curr.left, curr.right = curr.right, curr.left
        self.invertTree(curr.right)
        self.invertTree(curr.left)
        return curr
    


"""
MAXIMUM DEPTH OF BINARY TREE

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) +1



"""
Given a binary tree, determine if it is 
height-balanced.

height difference of every node's left and right is not more than 1.

Input: root = [3,9,20,null,null,15,7]
Output: true

Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true
"""


def isBalanced(self, root: Optional[TreeNode]) -> bool:
    balanced = [True]

    def height(root):
        if not root: return 0
        left_height = height(root.left)
        if not balanced[0]: return 0
        right_height = height(root.right)
        if abs(left_height-right_height)>1:
            balanced[0] = False
            return 0
        return max(left_height, right_height) + 1

    height(root)
    return balanced[0]



"""
DIAMETER OF BINARY TREE:

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
Example 2:

Input: root = [1,2]
Output: 1
 

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        largest_diameter = [0]
        def height(root):
            if root is None:
                return 0
            left_height = height(root.left)
            right_height = height(root.right)
            diameter = left_height + right_height
            largest_diameter[0] = max(largest_diameter[0], diameter)
            return max(left_height, right_height) + 1
        height(root)
        return largest_diameter[0]
    


"""
SAME TREE:

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Input: p = [1,2,3], q = [1,2,3]
Output: true

Input: p = [1,2], q = [1,null,2]
Output: false

Input: p = [1,2,1], q = [1,1,2]
Output: false
 
"""

def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

    from collections import deque
    p_list = []
    bfs_que = deque()
    bfs_que.append(p)
    while bfs_que:
        node = bfs_que.popleft()
        if node:
            p_list.append(node.val)
            bfs_que.append(node.left)
            bfs_que.append(node.right)
        else:
            p_list.append(None)

    q_list = []
    bfs_que = deque()
    bfs_que.append(q)
    while bfs_que:
        node = bfs_que.popleft()
        if node:
            q_list.append(node.val)
            bfs_que.append(node.left)
            bfs_que.append(node.right)
        else:
            q_list.append(None)

    if p_list != q_list: return False

    return True



"""
SYMMETRIC TREE

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Input: root = [1,2,2,3,4,4,3]
Output: true

Input: root = [1,2,2,null,3,null,3]
Output: false
 

"""

def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    def same(r1, r2):
        if not r1 and not r2: return True
        if not r1 or not r2: return False
        if r1.val != r2.val: return False
        return same(r1.left, r2.right) and same(r1.right,r2.left)

    return same(root, root)


"""
PATH SUM:

path sum from root to leaf node should be equal to targetsum given.
"""

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def has_sum(node, cur_sum):
            if not node: return False
            cur_sum += node.val
            if not node.left and not node.right:
                return cur_sum == targetSum
            return has_sum(node.left, cur_sum) or has_sum(node.right, cur_sum)

        return has_sum(root, 0)


"""
Binary Tree Level Order Traversal:

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []
"""

def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    from collections import defaultdict, deque
    d = defaultdict(list)
    def bfs(node):
        if not node:
            return []
        q = deque()
        q.append((node, 0))
        while q:
            n,i = q.popleft()
            d[i].append(n.val)
            if n.left: q.append((n.left, i+1))
            if n.right: q.append((n.right, i+1))
        
    bfs(root)
    return list(d.values())


def levelOrder(root: Optional[TreeNode]) -> list[list[int]]:
    from collections import deque
    q = deque()
    q.append(root)
    ans = []

    while q:
        level = []
        n = len(q)
        for i in range(n):
            node = q.popleft()
            level.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)

        ans.append(level)
    return ans


"""
Kth Smallest element in BST:

Input: root = [3,1,4,null,2], k = 1
Output: 1

Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
"""

def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    res = []
    def dfs(node):
        if not node: return 
        if node.left: dfs(node.left)
        res.append(node.val)
        if node.right: dfs(node.right)
    dfs(root)
    return res[k-1]

    
"""
ValidBST:

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Input: root = [2,1,3]
Output: true
Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

"""

def isValidBST(root: Optional[TreeNode]) -> bool:
    stk = [-float('inf')]
    res = [True]
    def inorder(node):
        if not node or not res[0]: return
        if node.left: inorder(node.left)
        if stk and node.val <= stk[-1]:
            res[0] = False
        stk[0] = node.val
        if node.right: inorder(node.right)
    inorder(root)
    return res[0]


"""
ISSUBTREE(ROOT, SUBROOT):
"""

def isSubtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    def sameTree(p,q):
        if not p and not q: return True
        if (not p and q) or (not q and p): return False
        if p.val != q.val: return False
        return sameTree(p.left,q.left) and sameTree(p.right, q.right)

    def has_subtree(node):
        if not node: return False
        if sameTree(node, subRoot):
            return True
        return has_subtree(node.left) or has_subtree(node.right)

    return has_subtree(root)


"""
Minimum Absolute Difference in BST:
Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

 
Example 1:
Input: root = [4,2,6,1,3]
Output: 1

Example 2:
Input: root = [1,0,48,null,null,12,49]
Output: 1
"""


def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
    min_diff = [float('inf')]
    stk = [None]
    def dfs(node):
        if not node: return
        if node.left: dfs(node.left)
        if stk[0] is not None:
            diff = node.val-stk[0]
            if diff<min_diff[0]:
                min_diff[0] = diff
        stk[0] = node.val
        if node.right: dfs(node.right)
    dfs(root)
        
    return min_diff[0]


"""
LOWEST COMMON ANCESTOR:

Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

Example 1:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [2,1], p = 2, q = 1
Output: 2
 
"""

def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    lca = [root]
    def search(root):
        if not root:
            return
        lca[0] = root
        if (root is p) or (root is q): return
        elif root.val>p.val and root.val>q.val: search(root.left)
        elif root.val<p.val and root.val<q.val: search(root.right)
        else: return
    search(root)
    return lca[0]
    

"""
Implement Trie: Prefix Tree

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
 

Example 1:

Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True

"""

class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        d = self.trie
        for c in word:
            if c not in d:
                d[c] = {}
            d = d[c]
        d['.'] = '.'

    def search(self, word: str) -> bool:
        d = self.trie
        for c in word:
            if c not in d:
                return False
            d = d[c]
        return '.' in d

    def startsWith(self, prefix: str) -> bool:
        d = self.trie
        for c in prefix:
            if c not in d:
                return False
            d = d[c]
        return True
