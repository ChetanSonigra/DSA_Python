# HashTables: Hash sets and Hash maps

# example
# buckets: 0,1,2,3,4
# hash function - converting str to int 
# g= 7 , r=18, e=5
# greg = 7+18+5+7= 37%5 = 2
# gre = 30%5 = 0
# grg = 32%5 = 2 - collition with greg

# Solving collition: linear probing or seperate chaining with linkedlist

# Hash sets: collections of unique items:

# lookup for an element: *O(1)  - amortized due to collition
# adding element: O(1)
# deleting element: O(1)


# Hash maps: key, value pairs

# key should be hashable -immutable - str, int, tuples
# not hashable - list, dict
# stores as tuple: hashed_key - (key, value)
# lookup, addition, deletion - O(1)

# linear probing: 
# store greg in 2, store gre in 0, store grg in 3 since 2 already occupied.
# while deleting if next element exist add some sign -1 to check that there was an element.

s = set()
print(s)
s.add(3) # O(1)
s.add(2); s.add(6)
print(s)

if 2 in s:   # O(1)
    print(True) 

s.remove(2)  # O(1) s.discard() for not getting error.
print(s)

d = {1: 'a',2: 'b',3: 'c'}

if 2 in d:   # O(1)
    print(True)

print(d[3]) # O(1) ACCESSING

d[4] = 'd'  # O(1)
print(d)

del d[1] # O(1)
print(d)

# defaultdict 

from collections import defaultdict, Counter

d = defaultdict(int)
print(d[2])

a = "adsadasdfsa"
print(Counter(a))