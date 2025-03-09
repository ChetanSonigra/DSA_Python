"""
LAST STONE WEIGHT:

You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.

 

Example 1:

Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.
Example 2:

Input: stones = [1]
Output: 1

"""

from typing import Optional, List

def lastStoneWeight(stones: list[int]) -> int:
    import heapq
    stones_heap = [-x for x in stones]
    heapq.heapify(stones_heap)
    n = len(stones_heap)
    if n == 1: return stones[0]
    while len(stones_heap)>1:
        p = heapq.heappop(stones_heap)
        q = heapq.heappop(stones_heap)
        if p !=q:
            heapq.heappush(stones_heap,p-q)
    return -stones_heap[0] if stones_heap else 0


"""
Kth Largest element in array:

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

"""

def findKthLargest(nums: list[int], k: int) -> int:
    import heapq
    min_heap = []
    for num in nums:
        if len(min_heap)<k:
            heapq.heappush(min_heap,num)
        else:
            heapq.heappushpop(min_heap,num)

    return min_heap[0]


"""
TOP K Frequent Elements:

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]

"""

# O(nlogk), O(n)
def topKFrequent(nums: list[int], k: int) -> list[int]:
    import heapq
    heap = []
    d = {}
    for num in nums:
        if num in d:
            d[num] += 1
        else:
            d[num] = 1
    
    for x,y in d.items():
        if len(heap)<k:
            heapq.heappush(heap,(y,x))
        else:
            heapq.heappushpop(heap,(y,x))

    return [h[1] for h in heap]


# O(n)
def topKFrequent(nums: list[int], k: int) -> list[int]:
    n = len(nums)
    from collections import Counter
    counter = Counter(nums)
    buckets = [0]*(n+1)

    for key,v in counter.items():
        if buckets[v] == 0:
            buckets[v] = [key]
        else:
            buckets[v].append(key)
    
    ret = []
    for i in range(n,-1,-1):
        if buckets[i] != 0:
            ret.extend(buckets[i])

        if len(ret) == k:
            break
        
    return ret



"""
K CLOSEST POINTS TO ORIGIN:

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

 Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.
 
"""

import heapq
def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
    def dist(x,y):
        return x**2 + y**2

    heap = []
    for x,y in points:
        d = dist(x,y)
        if len(heap)<k:
            heapq.heappush(heap,(-d,x,y))
        else:
            heapq.heappushpop(heap,(-d,x,y))

    return [(x,y) for d,x,y in heap]


"""
Merge K sorted linked-list into one:

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists: list[Optional[ListNode]]) -> Optional[ListNode]:
    import heapq
    heap = []
    for i,x in enumerate(lists):
        if x:
            heapq.heappush(heap,(x.val,i, x))
    res = ListNode()
    D = res
    while heap:
        val,i, node = heapq.heappop(heap)
        res.next = node
        res = res.next
        if node.next: heapq.heappush(heap,(node.next.val,i, node.next))

    return D.next