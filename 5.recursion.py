# fibonacci: 0,1,1,2,3,5,8, 13, 21,...
# f(n) = f(n-1) + f(n-2)

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)


print(fib(5))

# recursion uses stack for function calls.

# Time complexity: O(2^N)
# Space complexity: O(n)

print(fib(14))


# Reversing linkedlist:
class SinglyNode:
    def __init__(self, val, next=None):
        self.val = val 
        self.next = next
    def __str__(self):
        return str(self.val)
    
Head = SinglyNode(1)
A = SinglyNode(2)
B = SinglyNode(3)
C = SinglyNode(4)

Head.next = A
A.next = B
B.next = C

print(Head)

def reverse(head):
    if not head:
        return
    reverse(head.next)
    print(head)

reverse(Head)