'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
'''
#24 ms	13.9 MB
#sol) itertools 모듈을 활용하여 곱집합 구하기
from itertools import product
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) ==0 :
            return []
        alpha = ['','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        dic = {str(i):alpha[i-1] for i in range(1,10)}
        tmp = []
        for i in digits:
            tmp.append(dic[i])
        ans = []
        for p in list(product(*tmp)):
            ans.append(''.join(p))
        return ans
        