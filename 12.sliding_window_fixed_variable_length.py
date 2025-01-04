# 2 type of sliding window: fixed and variable.

# generally array/string is given and subarray/substring is mentioned in problem.

"""
Longest substring without repeating character

Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

"""

s = "abcabcbb"

def longest_substr(s):
    longest = 0
    l = 0
    n = len(s)
    seen = set()
    for r in range(n):
        
        while s[r] in seen:
            seen.remove(s[l])
            l += 1
        
        w = r-l + 1
        longest = max(longest, w)
        seen.add(s[r])

    return longest
    
    # O(n), O(n)

print(longest_substr("abcabcbb"))



"""
Maximum average subarray 1

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10^-5 will be accepted.

 

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000
 

Constraints:

n == nums.length
1 <= k <= n <= 105
-104 <= nums[i] <= 104
"""

def max_avg_subarr(l:list, k: int):
    n = len(l)
    cur_sum = 0
    for i in range(k):
        cur_sum += l[i]

    max_sum = cur_sum
    for i in range(k,n):
        cur_sum += l[i]
        cur_sum -= l[i-k]

        max_sum = max(max_sum,cur_sum)

    return max_sum/k

# O(n)

print(max_avg_subarr([1,12,-5,-6,50,3],4))