a = [-5,-2,-1,3,5,8,11]

# Naive searching - O(n)

if 8 in a:
    print(True)


# Binary Search 
# Time Complexity - O(logn), Space Complexity - O(1)

def search(val,a_list):
    l = 0
    r = len(a) -1
    while l<=r:
        m = (l+r)//2
        if a_list[m]>val:
            r = m-1
        elif a_list[m]<val:
            l = m+1
        else:
            return m
    return False

print(search(8,a))


# condition based: [T,T,T,T,F,F,F]

a = [True, True, True, True, False, False, False]

def bs_condition(arr):
    l = 0
    r = len(arr)-1

    while l<r:
        m = (l+r)//2
        if arr[m]:
            l = m+1
        else:
            r = m
    return l

print(bs_condition(a))