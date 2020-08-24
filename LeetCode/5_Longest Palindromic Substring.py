'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
'''
#5036 ms 13.9 MB
#sol1) for문으로 시작지점을 하나씩 지정하고 끝지점은 가장 끝(len(s))으로 초기화 -> while문에서 끝지점을 계속 옮겨가면서 palindrome 여부 체크(O(n*m*(문자열 뒤집는 연산)))
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ['',0]
        if len(s) == 1:
            return s
        for i in range(len(s)): #시작지점 O(n)
            end = len(s) #시작~어디까지 볼 것인지(끝지점)
            
            while end >= i: #O(m)
                if end-i <= ans[1]: #볼 필요 없는지 체크
                    break
                if s[i:end] == s[i:end][::-1]:#TLE가 발생한 이유: reverse + join연산을 했기 때문
                    ans = [s[i:end], end-i]
                    break
                end-=1
                
        return ans[0]

#896 ms	13.8 MB
#sol2) for문으로 middle(m)값 설정 및 left(l),right(r)의 초깃값을 설정해주고 중복 원소 체크 + palindrome 여부 체크 -> left,right가 가리키는 인덱스를 활용하므로 reverse 연산 필요X
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)<2:
            return s
        ans = ['',0]
        for m in range(len(s)):
            l,r = m,m
            while r<len(s)-1 and s[r] == s[r+1]: #중복 원소 체크 및 인덱스 갱신
                r+=1
            
            while l>0 and r<len(s)-1 and s[r+1] == s[l-1]: #각자 가리키는 인덱스의 값이 같은지 체크 및 인덱스 갱신(조건 충족하지 않으면 break)
                l-=1
                r+=1
            
            if r-l+1 >ans[1]:
                ans = [s[l:r+1], r-l+1]

        return ans[0]