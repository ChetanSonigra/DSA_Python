# static array = fixed size array. can't change length of array
# but can change an element of array.
# contigious block of elements

a = [1,3,4,6,7]

# check if element inside an array:
print(5 in a)   # O(n) = worst case

# static array insertion = O(n) - worst case

# static array element deletion = O(n) = worst case

# We don't have static array in python
# Dynamic Array: can change length = list in python

# can append more element: 
# under the hood list uses static array. creates new static array with double length(4,8,16...)
# append: O(n)/O(1) = copy + add the element / add in free space. 
# average append = O(1)
# insertion: O(n)
# deletion: O(n)
# random access = O(1)
# modifying element = O(1)
# append/pop at end: O(1)
# check element exist: O(n)


# String: 'abc' = CONTIGIOUS BLOCK OF MEMORY.
# immutable

# append: O(n)
# insert,deletion: O(n)
# access: O(1)

# len(a) - O(1)  # python stores this as property.