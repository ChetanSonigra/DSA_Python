"""
You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.

You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:

An integer x.
Record a new score of x.
'+'.
Record a new score that is the sum of the previous two scores.
'D'.
Record a new score that is the double of the previous score.
'C'.
Invalidate the previous score, removing it from the record.
Return the sum of all the scores on the record after applying all the operations.

The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.

 

Example 1:

Input: ops = ["5","2","C","D","+"]
Output: 30
Explanation:
"5" - Add 5 to the record, record is now [5].
"2" - Add 2 to the record, record is now [5, 2].
"C" - Invalidate and remove the previous score, record is now [5].
"D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
"+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
The total sum is 5 + 10 + 15 = 30.
Example 2:

Input: ops = ["5","-2","4","C","D","9","+","+"]
Output: 27
Explanation:
"5" - Add 5 to the record, record is now [5].
"-2" - Add -2 to the record, record is now [5, -2].
"4" - Add 4 to the record, record is now [5, -2, 4].
"C" - Invalidate and remove the previous score, record is now [5, -2].
"D" - Add 2 * -2 = -4 to the record, record is now [5, -2, -4].
"9" - Add 9 to the record, record is now [5, -2, -4, 9].
"+" - Add -4 + 9 = 5 to the record, record is now [5, -2, -4, 9, 5].
"+" - Add 9 + 5 = 14 to the record, record is now [5, -2, -4, 9, 5, 14].
The total sum is 5 + -2 + -4 + 9 + 5 + 14 = 27.
Example 3:

Input: ops = ["1","C"]
Output: 0
"""

def calPoints(operations: list[str]) -> int:
    s = {'C','D', '+'}
    rec = []
    for op in operations:
        if op == 'C':
            rec.pop()
        elif op == 'D':
            rec.append(rec[-1]*2)
        elif op == '+':
            rec.append(rec[-1] + rec[-2])
        else:
            rec.append(int(op))

    return sum(rec)


"""
Parenthesis check

True: '()', '(){}[]', '({})', 
False: ']', '[', '(]'
"""

def isValid(self, s: str) -> bool:
    stk = []
    d = {'(':')', '{': '}', '[': ']'}
    for x in s:
        if x in d:
            stk.append(x)
        elif stk and d[stk[-1]] == x:
            stk.pop()
        else:
            return False
    if stk: return False
    return True


"""
Daily Temperatues:

Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
 
"""

def dailyTemperatures(temperatures: list[int]) -> list[int]:
    
    n = len(temperatures)
    res = [0]*n
    stk = []
    i = 1
    for i, t in enumerate(temperatures):
        while stk and stk[-1][0]<t:
            tmp = stk.pop()
            res[tmp[1]] = i - tmp[1]
        stk.append((t,i))
            

    return res


"""
Evaluate Reverse Polish Notation:

You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
 

Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22

"""


def evalRPN(tokens: list[str]) -> int:
    stk = []
    s = {'/','+','-','*'}
    for x in tokens:
        if x not in s:
            stk.append(int(x))
        else:
            a = stk.pop()
            b = stk.pop()
            if x == '+': stk.append(a+b)
            elif x == '-': stk.append(b-a)
            elif x == '*': stk.append(b*a)
            else: stk.append(int(b/a))
    return stk[0]


"""
Implement push, pop, top, getmin in Minstack:
with complexity of O(1)
"""

class MinStack:

    def __init__(self):
        self.minstk = []
        self.stk = []

    def push(self, val: int) -> None:
        if self.minstk:
            self.minstk.append(min(self.minstk[-1],val))
        else: 
            self.minstk.append(val)
        self.stk.append(val)
        

    def pop(self) -> None:
        self.stk.pop()
        self.minstk.pop()        

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.minstk[-1]
        
