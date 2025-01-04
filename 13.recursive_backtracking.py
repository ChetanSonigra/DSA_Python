# generally used to get exhaustive/all solutions.
# make decision, recursion, base case, undo decision.

"""
Subsets:

Given an integer array nums of unique elements, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.

"""

def arr_subsets(l: list):
    n = len(l)
    result = []
    
    sol = []

    def backtrack(i):
        if i==n:
            result.append(sol[:])
            return
        
        # don't pick l[i]
        backtrack(i+1)

        # pick l[i]
        sol.append(l[i])
        backtrack(i+1)
        sol.pop()

    backtrack(0)
    return result

# time complexity: O(2^n), space: O(n)
print(arr_subsets([1,2,3]))