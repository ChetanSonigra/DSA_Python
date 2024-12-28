# stack: can use dynamic array/list or doubly linkedlist - LIFO
# methods: append, pop, peek(access last element), isempty() - O(1)

# Queue: FIFO
# methods: enqueue, dequeue
# implement as doubly linked list, bcz dequeue operation is O(n) for dynamic array.

stk = []
print(stk)

# append - O(1)
stk.append(4)
stk.append(2)
stk.append(5)
print(stk)

# pop from end - O(1)
stk.pop()
print(stk)

# if empty: - O(1)
if stk:
    print(True)

# error poping when stk is empty.


from collections import deque

d = deque()

print(d)
d.append(3)
d.append(2)  # O(1)
d.append(5)

print(d)

d.popleft()  # O(1)

print(d)

# peek - O(1)

print(d[0]) # from left
print(d[-1])  # from right