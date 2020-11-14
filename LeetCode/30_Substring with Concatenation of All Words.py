'''
You are given a string s and an array of strings words of the same length. 
Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once, 
in any order, and without any intervening characters.

You can return the answer in any order.

Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine 
'''
#9992 ms 14.5 MB -->  효율성을 높일 방법에 대해 조금 더 생각해봐야한다.
from collections import Counter
import copy
class Solution:
    def findSubstring(self, s, words):
        
        if not s or not words:
            return []
        
        counter = Counter(words)
        target_len = len(words[0])
        total_len = target_len*len(words)
        res = []
        for i in range(len(s)-target_len+1):
            done = copy.deepcopy(counter)
            for j in range(i, len(s) ,target_len):
                sub_str = s[j: j + target_len]
                if sub_str in done and done[sub_str] > 0:
                    done[sub_str] -= 1
                else:
                    break
                    
            if sum(done.values()) == 0:
                res.append(i)
        return res