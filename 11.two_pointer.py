# 2 pointer means 2 indices.
# squeeze

# problem: squares of sorted array:
"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
 

Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?
"""

arr = [-7,-3, 2, 3, 11]
arr = [-4,-1,0,3,10]
i = 0
j = len(arr) - 1

sorted_squares = []
while i<=j:
    i_square = arr[i]**2
    j_square = arr[j]**2

    if i_square>j_square:
        sorted_squares.append(i_square)
        i += 1
    else:
        sorted_squares.append(j_square)
        j-=1

sorted_squares.reverse()
print(sorted_squares)
