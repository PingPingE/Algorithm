'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''
#36 ms	14.1 MB
#sol) 음의 정수 체크 -> 뒤집기 -> 0으로 시작하는지 체크 -> 정수 오버플로우 체크 -> return
class Solution:
    def reverse(self, x: int) -> int:
        sign = ''
        if abs(x) != x:#음의 정수 체크
            sign = '-'
            x = abs(x)
            
        x = str(x)[::-1] #뒤집기
        
        if len(x) == 1:#한자리 수는 바로 return
            return sign+x
        
        while x.startswith('0'):#0으로 시작하지 않을 때 까지
            x= x[1:]
            
        if int(sign+x) <-pow(2,31) or int(sign+x)>pow(2,31)-1: #integer overflow 체크
            return 0
        
        return sign+x