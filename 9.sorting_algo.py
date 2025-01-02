# sorting algorithms:

# bubble sort: swapping
# time: O(n^2), space: O(1)

A = [-5,3,2,1,-3,-3,7,2,2]

def bubble_sort(l:list):
    n = len(l)
    flag = True
    
    while flag:
        flag=False
        for i in range(n-1):
            if l[i]>l[i+1]:
                flag=True
                l[i], l[i+1] = l[i+1], l[i]
    return l


print(bubble_sort(A))


A = [-5,3,2,1,-3,-3,7,2,2]
# insertion sort: 2 sides sorted and unsorted.then insert
#  O(n^2), O(1)
def insertion_sort(l:list):
    n = len(l)
    for i in range(1,n):
        for j in range(i,0,-1):
            if l[j]<l[j-1]:
                l[j],l[j-1] = l[j-1],l[j]
            else:
                break
    return l

print(insertion_sort(A))


# selection sort: sorted and unsorted portion. swap minimum of 2 to sorted side.
# O(n^2), O(1)

A = [-5,3,2,1,-3,-3,7,2,2]

def selection_sort(l: list):
    n = len(l)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if l[min_index]>l[j]:
                min_index = j
        l[i],l[min_index] = l[min_index],l[i]
    return l

print(selection_sort(A))


# Merge Sort: divide and conqure method.
# O(nlogn), 
# O(n), can be done in O(logn) as well

A = [-5,3,2,1,-3,-3,7,2,2]

def merge_sort(l:list):
    n = len(l)

    if n == 1:
        return l
    
    m = n//2
    L = merge_sort(l[:m])
    R = merge_sort(l[m:])
    len_l, len_r = len(L), len(R)
    sorted_l = []
    l,r = 0,0
    while l<len_l and r<len_r:
        if L[l]<=R[r]:
            sorted_l.append(L[l])
            l+=1
        else:
            sorted_l.append(R[r])
            r+=1
    sorted_l += L[l:] + R[r:]
    return sorted_l


A = [-5,3,2,1,-3,-3,7,2,2]
print(merge_sort(A))


# Quick Sort: recursive
# pick a pivot(usually last element), 3 part - a pivot, right and left part
# good pivot - O(nlogn), bad pivot - O(n^2)
# space: O(n), O(logn) also possible.

def quicksort(arr: list):
    if len(arr)<2:
        return arr
    
    pivot = arr[-1]
    L = [x for x in arr[:-1] if x<=pivot]
    R = [x for x in arr[:-1] if x>pivot]

    L = quicksort(L)
    R = quicksort(R)

    return L + [pivot] + R

A = [-5,3,2,1,-3,-3,7,2,2]
print(quicksort(A))


# Counting sort: build counts arr by choosing max value and counting each elements.
# time complexity: O(k+n) , space: O(k), k = max_value
# better when max value is not high.

A = [5,3,2,1,3,3,7,2,2]


def countingsort(arr):
    k = max(arr)
    n = len(arr)
    counts = [0]*(k+1)

    for x in arr:
        counts[x] += 1

    i = 0

    for c in range(k+1):
        while counts[c]>0:
            counts[c]-=1
            arr[i] = c
            i+=1

    return arr

print(countingsort(A))



# in practise:
# python uses tim sort with O(nlogn) complexity.

A = [-5,3,2,1,-3,-3,7,2,2]

# not inplace - space - O(n)
B = sorted(A)
print(B,A)

# in place: - space - O(1)
A.sort()
print(A)

# sort an arr of tuples

t = [(-5,3), (2,1), (-3,-3),(7,2)]

sorted_t = sorted(t, key=lambda t: t[0])
print(sorted_t)

sorted_t = sorted(t, key=lambda t: t[1])
print(sorted_t)

sorted_t = sorted(t, key=lambda t: -t[1])
print(sorted_t)