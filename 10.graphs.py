# Trees, linked lists are subclass of graphs.

# edges and vertices. vertices doesn't neccesarily need to have edge.

# directed graph: can go only in one direction
# undirected graph: 2 way 

# cyclic graph: loop

# Edge List: list of edge: [0,1] from 0 to 1.
# edges = [[1,2], [0,1], [2,3], [3,1]]

# adjacency matrix for vertices to see which vertices is connected to which one.
# this is lot of data, 
# this gives a another data structure which is better.
# adjacency list: {0:[1], 1:[2,3], 2:[3,1], 3:[1,2]}

# another way to store is class. class Node: node.value, node.neighbours = list of vertices.


# DFS: uses stack/recursion
# Time: O(E+V), SPACE: O(V+E)

# BFS: uses queue.
# Time: O(E+V), SPACE: O(V+E)

# tree: connected acyclic graph
# for a tree E = v-1


# Arr of edges: directed

n = 8
A = [[0,1],[1,2],[0,3],[3,4],[3,6],[3,7],[4,2],[4,5],[5,2]]


# convert arr of edges to adjacency matrix:

M = []

for i in range(n):
    M.append([0]*n)

print(M)

for u,v in A:
    M[u][v] = 1

    # uncomment below line if undirected graph
    # M[v][u] =1

print(M)


# convert arr of edges to adjacency list.

from collections import defaultdict

D = defaultdict(list)

for u,v in A:
    D[u].append(v)
    # UNCOMMENT BELOW LINE IF UNDIRECTED GRAPH
    # D[v].append(u)

print(D)


# DFS with recursion: O(v+e)

def dfs_recursive(node):
    print(node)
    for new_node in D[node]:
        if new_node not in seen:
            seen.add(new_node)
            dfs_recursive(new_node)
            


source = 0
seen = set()
seen.add(source)
dfs_recursive(source)


# Iterative DFS with stack: O(v+e)

def dfs_iterative(node):
    stk = [node]
    seen = [node]
    while stk:
        v = stk.pop()
        print(v)
        for item in D[v]:
            if item not in seen:
                seen.append(item)
                stk.append(item)

dfs_iterative(source)


# BFS: Queue - O(v+e)

from collections import deque

def bfs(node):
    seen = set()
    seen.add(node)
    q = deque()
    q.append(node)
    while q:
        vertice = q.popleft()
        print(vertice)
        for x in D[vertice]:
            if x not in seen:
                seen.add(x)
                q.append(x)

print('---bfs---')
bfs(source)


# class way:

class Node:
    def __init__(self, value):
        self.value = value
        self.nei = []

    def __str__(self):
        return f"Node({self.value})"
    
    def display(self):
        connections = [node.value for node in self.nei]
        return f"{self.value} is connected to {connections}."
    

A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')

A.nei.append(B)
B.nei.append(A)
C.nei.append(D)
D.nei.append(C)

print(A.display())