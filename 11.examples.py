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
