'''
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
'''
#sol1) 문자열로 바꾼 후 뒤집기
#60 ms	13.9 MB
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x= str(x)
        return True if x==x[::-1] else False

#sol2) 문자열로 바꾸지 않고 계산으로 구하기
#56 ms	13.8 MB
class Solution:
    def isPalindrome(self, x: int) -> bool:
        origin = x
        ans = 0
        
        if x<0:#음수면 -기호 때문에 항상 False
            return False
        
        while x:
            ans *= 10 #자리 늘리기
            ans += x%10 #낮은 자리 수부터 더하기
            x //=10 
            
        return True if ans == origin else False
        
        
        