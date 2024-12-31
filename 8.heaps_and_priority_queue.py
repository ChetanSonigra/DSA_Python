# heap = priority queue
# type of binary tree -

# BT -  2i+1 and 2i+2 gives index position of node at ith position IN bfs.

# heap -min, max

# root node is min of all nodes. similarly any node is minimum of all its child node.

# heap pop: O(logn base 2) - extract min
# heap peek: O(1) - see min value.
# heap push: O(logn base 2) - insert element
# heap sort algorithm: O(nlogn) , O(1)

# heapify: function to make a tree a min/max heap - O(n), O(1)

# use tuples to store priority with data. (1,A)

import heapq

A = [-4,3,1,0, 2,5, 10, 8, 12, 9]

heapq.heapify(A)
print(A)


# heap push - insert - O(logn)
heapq.heappush(A,4)
print(A)

# heappop - extract min - O(logn)
minn = heapq.heappop(A)
print(A, minn)

# peek:
print(A[0])

# heap sort - time: O(n logn), space: O(n), O(1) also possible via swapping but complex.

def heap_sort(arr: list):
    heapq.heapify(arr) # O(n)
    n = len(arr)
    new_arr = [0]*n
    for i in range(n):             # O(nlogn)
        minn = heapq.heappop(arr)
        new_arr[i] = minn
    return new_arr

print(heap_sort(A))

# heap push pop - O(logn)

A = [-4,3,1,0, 2,5, 10, 8, 12, 9]

heapq.heapify(A)
print(A)
heapq.heappushpop(A, 89)
print(A)


# heapq doesn't support max heap, to make min heap to max heap, just change the sign of elements

for i in range(len(A)):
    A[i] = -A[i]

print(A)
heapq.heappop(A)
largest = -heapq.heappop(A)
print(largest)

