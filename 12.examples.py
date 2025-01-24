"""
1004. Max Consecutive Ones III

Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

"""

def longestOnes(nums: list[int], k: int) -> int:
    from collections import deque
    zero_que = deque()
    n = len(nums)
    l = 0
    max_w = 0
    for r in range(n):
        if nums[r] == 0 and len(zero_que)>k-1:
            if k>0:
                l = zero_que.popleft()+1
                zero_que.append(r)
            else:
                l = r + 1
        elif nums[r] == 0:
            zero_que.append(r)
        w = r-l+1
        max_w = max(max_w, w)
    return max_w


def longestOnes(nums: list[int], k: int) -> int:
    zero_counts = 0
    n = len(nums)
    l = 0
    max_w = 0
    for r in range(n):
        if nums[r] == 0:
            zero_counts += 1
        while zero_counts>k:
            if nums[l] == 0:
                zero_counts -= 1
            l += 1
        w = r-l+1
        max_w = max(max_w, w)
    return max_w



"""
424. Longest Repeating Character Replacement

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.

"""


def characterReplacement(s: str, k: int) -> int:
    longest = 0
    l = 0
    counts = [0]*26
    n = len(s)

    for r in range(n):
        counts[ord(s[r])-65] += 1
        while r-l+1 - max(counts)>k:
            counts[ord(s[l])-65] -= 1
            l += 1
        longest = max(longest, r-l+1)

    return longest



"""
MINIMUM SIZE SUBARRAY SUM

Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

"""

def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    l = 0
    min_arr_size = float('inf')
    n = len(nums)
    cur_sum = 0
    for r in range(n):
        cur_sum += nums[r]

        while cur_sum>=target:
            w = r -l + 1
            min_arr_size = min(min_arr_size, w)
            cur_sum -= nums[l]
            l += 1

    if min_arr_size != float('inf'): return min_arr_size
    else: return 0


"""
567. Permutation in String

Given two strings s1 and s2, return true if s2 contains a 
permutation
 of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false

"""

def checkInclusion(self, s1: str, s2: str) -> bool:
    n1 = len(s1)
    n2 = len(s2)

    if n1>n2: return False

    s1_counts = [0]*26
    s2_counts = [0]*26

    for i in range(n1):
        s1_counts[ord(s1[i])-97] += 1
        s2_counts[ord(s2[i])-97] += 1

    if s1_counts == s2_counts: return True
    for i in range(n1,n2):
        s2_counts[ord(s2[i])-97] += 1
        s2_counts[ord(s2[i-n1])-97] -= 1
        if s1_counts == s2_counts: return True

    return False