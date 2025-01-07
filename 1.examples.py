"""
Given an integer array nums of size n, 
return the number with the value closest to 0 in nums. 
If there are multiple answers, return the number with the largest value.

 

Example 1:

Input: nums = [-4,-2,1,4,8]
Output: 1
Explanation:
The distance from -4 to 0 is |-4| = 4.
The distance from -2 to 0 is |-2| = 2.
The distance from 1 to 0 is |1| = 1.
The distance from 4 to 0 is |4| = 4.
The distance from 8 to 0 is |8| = 8.
Thus, the closest number to 0 in the array is 1.
Example 2:

Input: nums = [2,-1,1]
Output: 1
Explanation: 1 and -1 are both the closest numbers to 0, so 1 being larger is returned.
 

Constraints:

1 <= n <= 1000
-105 <= nums[i] <= 105
"""

def findClosestNumber(nums: list[int]) -> int:
    closest_num = abs(nums[0])
    for x in nums:
        if abs(x)< closest_num:
            closest_num = abs(x)
    return closest_num if closest_num in nums else 0-closest_num 

print(findClosestNumber([-4,-2,1,4,8]))


"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

 

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
 

Constraints:

1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.
"""

def mergeAlternately(word1: str, word2: str) -> str:
    result = ""
    l = len(word1)
    if len(word1)>len(word2):
        l = len(word2)

    for i in range(l):
        result += word1[i]+ word2[i]
    result += word1[i+1:] + word2[i+1:]

    return result

print(mergeAlternately('ab','pqrs'))



"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.
 

Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?
"""

def isSubsequence(s: str, t: str) -> bool:
    i = 0
    for x in s:
        if x not in t[i:]:
            return False
        i = t.find(x,i) + 1
    return True



"""

Best time to buy stock: 


You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104

"""

# brute force approach: O(n^2)

def maxProfit(prices: list[int]) -> int:
    k = len(prices)
    max_profit = 0
    for i in range(k):
        for j in range(i+1,k):
            if prices[j]-prices[i]>max_profit:
                max_profit = prices[j] - prices[i]
    return max_profit

print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))


# better 2 pointer approach. O(n)

def maxProfit(prices: list[int])->int:
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        
        profit = price - min_price
        if profit>max_profit:
            max_profit = profit
    return max_profit

print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))


"""
Longest common prefix:

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""

def longest_common_prefix(strs: list[str]) -> str:
    s = strs[0]
    n = len(s)
    i = 0
    lcp = ""
    for i in range(n):
        if all(s[i]==st[i] for st in strs):
            lcp += s[i]
        else: break
    return lcp

print(longest_common_prefix(["flower","flow","flight"]))
print(longest_common_prefix(["dog","racecar","car"]))

# this doesn't include edge cases like min length string outbound index.

# O(n*m)
def longest_common_prefix(strs: list[str])-> str:
    n = float('inf')

    for s in strs:
        if len(s)<n:
            n = len(s)
        
    i = 0
    while i<n:
        for s in strs:
            if s[i] != strs[0][i]:
                return s[:i]
        i+= 1

    return s[:i]

print(longest_common_prefix(["flower","flow","flight"]))
print(longest_common_prefix(["dog","racecar","car"]))
print(longest_common_prefix(["a"]))
print(longest_common_prefix([""]))