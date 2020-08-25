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
#sol) 음의 정수 체크 -> str타입으로 변환 -> 뒤집기 -> 0으로 시작하는지 체크 -> 정수 오버플로우 체크 -> return
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

#28 ms	13.6 MB	
#sol2) str타입으로 변환하지 않고 뒤집기
class Solution:
    def reverse(self, x: int) -> int:
        sign = ''
        if x<0: #음의 정수 체크
            sign='-'
            x=abs(x)
            
        res = 0
        while x:
            res = res*10 #다음 자리 마련
            res += x%10 #낮은 자리 숫자 더하기 
            x = (x-x%10)//10 #x 갱신(이미 res에 더한 숫자 없애기)
        
        res = str(res)
        if int(sign+res) <-pow(2,31) or int(sign+res)>pow(2,31)-1: #integer overflow 체크
            return 0
        
        return sign+res