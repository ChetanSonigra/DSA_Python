# 1. NAIVE RECURSIVE: O(2^N)
# 2. TOP-DOWN: DP-MEMOIZATION: 
# 3. BOTTOM-UP: DP-TABULAR: 
# 4. BOTTOM-UP WITH CONSTANT SPACE

# EX: 1 FIBONACCI NUMBER


# naive recursive approach
def fib(n: int):
    if n == 0:
        return 0
    elif n==1:
        return 1
    return fib(n-1) + fib(n-2)

# fib(6): will call f(4) 2 times. so, overlapping subproblem.
# O(2^n)


# top-down memoization/cache: using dictionary to store data for function calls.
# O(n), O(n)

def fib(n: int) -> int:
    memo = {0:0, 1: 1}

    def f(x):
        if x in memo:
            return memo[x]
        memo[x] = f(x-1) + f(x-2)
        return memo[x]
    
    return f(n)


print(fib(500))

import sys
print(sys.getrecursionlimit())


# bottom-up: tabulation: removes recursion

# O(n), O(n)

def fib(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    dp = [0]*(n+1)
    dp[0], dp[1] = 0, 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]

print(fib(10000)) # top-bottom can't do this due to recursion limit.


# above with constant space:

def fib(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    prev, cur = 0, 1
    for i in range(2, n+1):
        prev, cur = cur, prev+cur
    
    return cur

print(fib(10000)) # O(n), O(1)


# fastest approach: O(logn)

def fib(n):
    golden_ration = (1+(5**0.5))/2
    return int(round(golden_ration**n/(5**0.5)))

fib(1000)