"""
given a sorted array and target, search target index in array.
Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 
"""

def search(nums: list[int], target: int) -> int:
    n = len(nums)
    l = 0
    r = n-1
    while l<=r:
        m = (l+r)//2
        if nums[m] == target:
            return m
        elif nums[m]>target:
            r = m - 1
        else:
            l = m + 1
    return -1


"""
search insert position

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4

"""


def searchInsert(nums: List[int], target: int) -> int:
    l = 0
    r = len(nums)-1
    while l<=r:
        m = (l+r)//2
        if nums[m]== target:
            return m
        elif nums[m]>target:
            r = m-1
        else:
            l = m+1
    return max(l,m)


"""
First Bad Version:

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

 

Example 1:

Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.
Example 2:

Input: n = 1, bad = 1
Output: 1
"""

def firstBadVersion(n: int) -> int:
    l = 1
    r = n
    while l<r:
        m = (l+r)//2
        if isBadVersion(m):
            r = m
        else:
            l = m+1
    return l


"""
IsPerfectSquare(num:int)-> bool

Example 1:

Input: num = 16
Output: true
Explanation: We return true because 4 * 4 = 16 and 4 is an integer.
Example 2:

Input: num = 14
Output: false

"""

def isPerfectSquare(num: int) -> bool:
    l = 1
    r = num//2 + 1
    while l<=r:
        m = (l+r)//2
        res = m**2
        if  res == num:
            return True
        elif res>num:
            r = m-1
        else:
            l = m+1
    return False


"""
Search a 2D Matrix:

You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

"""

def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
    m = len(matrix)
    n = len(matrix[0])
    i = 0
    j = m-1
    while i<=j:
        mid = (i+j)//2
        if matrix[mid][0]==target:
            return True
        elif matrix[mid][0]>target:
            j = mid -1
        else:
            i = mid + 1
    row = min(j,i)
    i = 0
    j = n-1
    while i<=j:
        mid = (i+j)//2
        if matrix[row][mid]==target:
            return True
        elif matrix[row][mid]>target:
            j = mid -1
        else:
            i = mid + 1
    return False


"""
Find minimum in rotated sorted array:

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

 

Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times.
"""

def findMin(self, nums: List[int]) -> int:
    l = 0
    r = len(nums)-1
    while l<r:
        m = (l+r)//2
        tmp = nums[m]
        if tmp>nums[r]:
            l = m+1
        else:
            r = m
    return nums[r]


"""
Search in rotated sorted array -

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1

"""

def search(nums: list[int], target: int) -> int:
    l = 0
    r = len(nums)-1
    while l<r:
        m = (l+r)//2
        if nums[m]>nums[r]:
            l = m+1
        else: r = m
    p = r
    if target>nums[-1]:
        l = 0
        r = p-1
    else:
        l = p
        r = len(nums) -1
    while l<=r:
        m = (l+r)//2
        if nums[m]== target:
            return m
        elif nums[m]>target:
            r = m-1
        else: l = m+1
    return -1


"""
KOKO EATING BANANAS:

Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

 

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23

"""

import math
def minEatingSpeed(piles: list[int], h: int) -> int:
    def k_works(k):
        hours = 0
        for p in piles:
            hours += math.ceil(p/k)
        return hours<=h
    l = 1
    r = max(piles)
    while l<r:
        m = (l+r)//2
        if k_works(m):
            r = m
        else:
            l = m+1
    return l
