# issubsequence? 

def isSubsequence(s: str, t: str) -> bool:
    i = 0
    j = 0
    n = len(t)
    k = len(s)
    if k == 0: return True
    if k>n: return False

    while i<n and j<k:
        if s[j] == t[i]:
            j+= 1
        i += 1

    if j ==k:
        return True
    return False

print(isSubsequence('abc','ahbgdc'))
print(isSubsequence('axc','ahbgdc'))


"""
SQUARES OF SORTED ARRAY:

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

"""

def sorted_squares(nums: list)-> list:
    i = 0
    n = len(nums)
    j = n -1
    res = []
    while i<=j:
        if abs(nums[i])>abs(nums[j]):
            res.append(nums[i]**2)
            i += 1
        else: res.append(nums[j]**2); j -= 1
    res.reverse()
    return res



"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

"""
# O(n), O(1)
def rev_str(s: list):
    n = len(s)
    k = len(s)//2
    for i in range(k):
        s[i], s[n-1-i] = s[n-1-i], s[i]
    


"""
TWO SUM IN SORTED ARRAY: 

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

 

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

"""

def two_sum_sorted(numbers: list[int], target: int)-> list[int]:
    L = 0
    R = len(numbers) -1
    while L<R:
        tmp = numbers[L] + numbers[R]
        if tmp == target:
            return [L+1,R+1]
        if tmp> target:
            R -= 1
        else:
            L += 1


"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
"""

def ispalindrome(s: str)-> bool:
    n = len(s)
    s = s.lower()
    i = 0
    j = n-1
    while i<j:
        if not s[i].isalnum():
            i += 1
            continue
        if not s[j].isalnum():
            j -= 1
            continue
        if s[i]==s[j]:
            i+= 1
            j-=1
        else: return False
    return True


"""
3 SUM: 


Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
"""

def three_sum(nums: list[int])-> list[list[int]]:
    nums.sort()
    n = len(nums)
    result = []
    seen = set()
    if n<3: return []
    if n == 3 and sum(nums) != 0: return []
    i= 0
    for i in range(n-2):
        if nums[i]>0:
            break
        if nums[i] in seen:
            continue
        lo = i+1
        hi = n-1
        target = -nums[i]
        seen.add(-target)
        while lo<hi:
            res = nums[lo] + nums[hi] 
            if res == target:
                result.append([-target,nums[lo],nums[hi]])
                lo += 1
                hi -= 1
                while lo<hi and nums[lo] == nums[lo-1]:
                    lo += 1
                while lo<hi and nums[hi] == nums[hi+1]:
                    hi -= 1
            elif res>target:
                hi -= 1
            else:
                lo += 1

    return result


"""
Container with most water:

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1

"""

def maxArea(height: list[int]) -> int:
    max_area = 0
    n = len(height)
    l, r = 0, n-1
    while l<r:
        min_h = min(height[l], height[r])
        area = (r-l)*min_h
        max_area = max(area, max_area)
        if min_h == height[l]:
            l += 1
        else: r -= 1

    return max_area



"""
Traping rain water:
"""