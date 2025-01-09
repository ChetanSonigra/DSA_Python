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


"""
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
 

Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
Example 2:

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
 

Constraints:

0 <= nums.length <= 20
-231 <= nums[i] <= 231 - 1
All the values of nums are unique.
"""

def summary_ranges(nums:list)-> list:
    end = None
    res = []
    n = len(nums)
    if n>0: start = nums[0]
    for i in range(n):
        if i<n-1 and nums[i] == nums[i+1] - 1:
            continue
        end = nums[i]
        if start != end:
            res.append(f"{start}->{end}")
        else:
            res.append(f"{start}")
        if i != n-1:
            start = nums[i+1]

    return res

print(summary_ranges([0,2,3,4,6,8,9]))
print(summary_ranges([]))



"""
1328. Break a Palindrome
Medium
Topics
Companies
Hint
Given a palindromic string of lowercase English letters palindrome, replace exactly one character with any lowercase English letter so that the resulting string is not a palindrome and that it is the lexicographically smallest one possible.

Return the resulting string. If there is no way to replace a character to make it not a palindrome, return an empty string.

A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ, a has a character strictly smaller than the corresponding character in b. For example, "abcc" is lexicographically smaller than "abcd" because the first position they differ is at the fourth character, and 'c' is smaller than 'd'.

 

Example 1:

Input: palindrome = "abccba"
Output: "aaccba"
Explanation: There are many ways to make "abccba" not a palindrome, such as "zbccba", "aaccba", and "abacba".
Of all the ways, "aaccba" is the lexicographically smallest.
Example 2:

Input: palindrome = "a"
Output: ""
Explanation: There is no way to replace a single character to make "a" not a palindrome, so return an empty string.
 

Constraints:

1 <= palindrome.length <= 1000
palindrome consists of only lowercase English letters.
"""


def breakPalindrome(palindrome: str) -> str:
    n = len(palindrome)//2
    i,j = 0,0
    ans = ""
    while i<n:
        if palindrome[i] != "a":
            ans = palindrome[:i] + "a" + palindrome[i+1:]
            break
        i+=1
    if not ans and n>0:
        ans = palindrome[:-1] + 'b'

    return ans

print(breakPalindrome("abccba"))
print(breakPalindrome('a'))
print(breakPalindrome('aa'))


"""
Remove all adjacent duplicates in string: 

You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

 

Example 1:

Input: s = "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
Example 2:

Input: s = "azxxzy"
Output: "ay"
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
"""

def remove_duplicates(s: str) -> str:
    n = len(s)
    res = []
    for x in s:
        if res and x == res[-1]:
            res.pop()
        else:
            res.append(x)
    return "".join(res)

print(remove_duplicates('azxxzy'))
print(remove_duplicates('abbaca'))


"""
Product of array except self:

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 
"""

# O(n)
def prod_except_self(nums: list)-> list:
    n = len(nums)
    L, R = [0]*n, [0]*n
    l,r = 1,1
    for i in range(n):
        j = -i-1
        L[i] = l 
        R[j] = r 
        l *= nums[i]
        r *= nums[j]

    return [x*y for x,y in zip(L,R)]


print(prod_except_self([1,2,3,4])) 
print(prod_except_self([-1,1,0,-3,3]))

"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104

"""

def merge_interval(intervals: list[list]) -> list[list]:
    intervals.sort(key = lambda x: x[0])
    merged = []

    for interval in intervals:
        if not merged or merged[-1][1]<interval[0]:
            merged.append(interval)
        else:
            merged[-1] = [merged[-1][0],max(merged[-1][1], interval[1])]

    return merged


print(merge_interval([[1,3],[2,6],[8,10],[15,18]]))
print(merge_interval([[1,4],[4,5]]))



"""
Spiral Matrix: 

Given an m x n matrix, return all elements of the matrix in spiral order.

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

# O(m*n)

def spiral_matrix(matrix: list[list[int]])-> list:
    m = len(matrix)
    n = len(matrix[0])
    i,j = 0, 0
    res = []
    k = m*n
    direction = 0
    up, right, down, left = 0, n, m, -1
    while len(res)<k:
        
        if direction == 0:
            while i<right:
                res.append(matrix[j][i])
                i += 1
            direction = 1
            right -= 1
            i -= 1
            j += 1

        elif direction == 1:
            while j<down:
                res.append(matrix[j][i])
                j += 1
            direction = 2
            down -= 1
            j -= 1
            i -= 1

        elif direction == 2:
            while i>left:
                res.append(matrix[j][i])
                i -= 1
            direction = 3
            left += 1
            i += 1
            j -= 1
        else:
            while j>up:
                res.append(matrix[j][i])
                j -= 1
            direction = 0
            up += 1
            j += 1
            i += 1
    return res

print(spiral_matrix([[1,2,3],[4,5,6],[7,8,9]]))
print(spiral_matrix([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))

"""
Transform matrix to 90 degree:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

"""

# O(n^2), O(1)
def transform_matrix(matrix: list[list[int]])-> list[list[int]]:
    i,j = 0, 0
    n = len(matrix)
    while j< n:
        while i<n:
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            i += 1
        j += 1
        i = j
    # print(matrix)
    for row in matrix:
        for i in range(n//2):
            row[i], row[n-1-i] = row[n-1-i], row[i]

    print(matrix)
            

transform_matrix([[1,2,3],[4,5,6],[7,8,9]])
transform_matrix([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])