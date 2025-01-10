"""
Roman to Integer: 

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
"""

import time

def roman_to_int(s:str) -> int:
    n = len(s)
    res = 0
    i = 0

    romans = {'I':1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    start = time.perf_counter()
    while i< n:
        if i != n-1 and romans[s[i]]<romans[s[i+1]]:
            res += romans[s[i+1]] - romans[s[i]]
            i+=2
        else:
            res += romans[s[i]]
            i+=1
    duration = (time.perf_counter() - start)*1000000
    return res, duration, "micro seconds"

print(roman_to_int('III'))
print(roman_to_int("MCMXCIV"))
print(roman_to_int("MMCMCMCCXCXCIV"))

def roman_to_int(s:str) -> int:
    n = len(s)
    res = 0
    i = 0

    romans = {'I':1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 
              'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900
              }
    start = time.perf_counter()
    while i< n:
        if s[i:i+2] in romans:
            res += romans[s[i:i+2]]
            i+=2
        else:
            res += romans[s[i]]
            i+=1
    duration = (time.perf_counter() - start)*1000000
    return res, duration, "micro seconds"

print(roman_to_int('III'))
print(roman_to_int("MCMXCIV"))
print(roman_to_int("MMCMCMCCXCXCIV"))


""""
You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".

 

Example 1:

Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
Example 2:

Input: jewels = "z", stones = "ZZ"
Output: 0
 

Constraints:

1 <= jewels.length, stones.length <= 50
jewels and stones consist of only English letters.
All the characters of jewels are unique.
"""
# O(n+m), space; O(n)
def jweles(jewels: str, stones: str) -> int:
    c = 0
    js = set(jewels)
    for s in stones:
        if s in js:
            c += 1
    return c

print(jweles('aA', 'aAAbbb'))
print(jweles('z', 'ZZ'))


"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
"""

# using defaultdict/counter is fast instead of manual.

def ransom_soln(ransomeNote: str, magazine: str)-> bool:
    from collections import Counter
    c = Counter(magazine)
    for s in ransomeNote:
        if c.get(s,0)>0:
            c[s] -= 1
        else:
            return False
    return True

print(ransom_soln('a', 'b'))
print(ransom_soln('aa', 'ab'))
print(ransom_soln('ab', 'aab'))

"""
VALID ANAGRAM::

Given two strings s and t, return true if t is an 
anagram
 of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false
"""

def anagram(s: str, t: str) -> bool:
    from collections import Counter
    s,t = Counter(s), Counter(t)
    return s == t

print(anagram('anagram', 'nagaram'))
print(anagram('rat', 'car'))


"""
TWO SUM: 

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 
"""

def two_sum(nums: list, target: int)-> list:
    n = len(nums)
    h = {}
    for i in range(n):
        h[nums[i]] = i

    for i in range(n):
        y = target- nums[i]
        if y in h and h[y] != i:
            return [i, h[y]]
        
print(two_sum([2,7,11,15], 9))
print(two_sum([3,2,4], 6))
print(two_sum([3,3],6))


"""
GROUP ANAGRAM:

Given an array of strings strs, group the 
anagrams
 together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]
"""
from collections import defaultdict
def group_anagrams(strs: list)-> list[list]:
    if len(strs)<2:
        return [strs]
    d = defaultdict(list)
    for s in strs:
        count = [0]*26
        for c in s:
            count[ord(c)-ord('a')] += 1
        
        key = tuple(count)
        d[key].append(s)
    return list(d.values())



"""
Longest consecutive sequence:

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

"""
# O(n)
def lcs(nums: list)-> int:
    s = set(nums)
    lcs = 0 
    for x in s:
        if x-1 not in s:
            next_x = x+1
            i = 1
            while next_x in s:
                i += 1
                next_x += 1
            lcs = max(lcs,i)
    return lcs

" Majority element problem "