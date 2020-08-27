'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
'''
#32 ms	13.9 MB
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        if len(strs) <=1: #비교대상이 없는 경우
            if len(strs)==0:
                return prefix
            return strs[0]
        
        min_size = len(min(strs, key=len)) #가장 짧은 원소의 길이를 구하고 최대 거기까지만 본다.
        for i in range(min_size):
            target= strs[0][i] #기준
            cnt = len(list(filter(lambda x: x[i] != target,strs))) #target과 다른거 count
            if cnt >0: #다른게 있으면 stop
                return prefix
            prefix = f"{prefix}{target}" #모두 같다면 prefix에 추가
        return prefix