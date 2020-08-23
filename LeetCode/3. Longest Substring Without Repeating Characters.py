'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
#76 ms	14.1 MB	
#start,end에 현재 보고 있는 인덱스 범위를 저장하고, max_cnt는 현재까지의 가장 긴 substring길이(중복 요소 없는)를 저장한다.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set_s = set()
        max_cnt = 0
        start, end = 0,0
        while start<=end and end<len(s):
            if s[end] not in set_s:
                set_s.add(s[end])
                end+=1
            else:
                max_cnt= max(max_cnt, end-start)
                set_s.remove(s[start])
                start+=1
        return max(max_cnt,end-start)
    