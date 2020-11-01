'''
Given a non-negative integer num, return the number of steps to reduce it to zero. 
If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

Example 1:

Input: num = 14
Output: 6
Explanation: 
Step 1) 14 is even; divide by 2 and obtain 7. 
Step 2) 7 is odd; subtract 1 and obtain 6.
Step 3) 6 is even; divide by 2 and obtain 3. 
Step 4) 3 is odd; subtract 1 and obtain 2. 
Step 5) 2 is even; divide by 2 and obtain 1. 
Step 6) 1 is odd; subtract 1 and obtain 0.
'''
#sol1) resursion v1(변수 無)
class Solution:
    def numberOfSteps (self, num: int) -> int:
        if num == 0:
            return num
        if num%2 == 1:
            return self.numberOfSteps(num-1)+1
        else:
            return self.numberOfSteps(num//2)+1

#sol2) recursion v2(변수 有)
class Solution:
    def numberOfSteps (self, num: int) -> int:
        if num == 0:
            return num
        if num%2 == 1:
            res = self.numberOfSteps(num-1)
        else:
            res = self.numberOfSteps(num//2)
        return res+1

#sol3) bits 연산
class Solution:
    def numberOfSteps (self, num: int) -> int:
        cnt = 0
        if num == 0: return 0
        while num>1:
            #print("cnt:", cnt,num, bin(num))
            if bin(num)[-1]=='1':
                num-=1
                cnt +=2
            else:
                cnt+=1
            num = num>> 1
        return cnt+1
