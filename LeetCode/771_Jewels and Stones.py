'''
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  
Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, 
so "a" is considered a different type of stone from "A".

Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3

Example 2:

Input: J = "z", S = "ZZ"
Output: 0
'''
#sol1: O(len(J)*len(S))
class Solution:#32 ms	14.1 MB
    def numJewelsInStones(self, J: str, S: str) -> int:
        sum =0 
        for j in J:
            sum += S.count(j)
        return sum

#sol2: O(len(J)*len(S))
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        sum =0 
        for s in S:
            if s in J: 
                sum+=1
        return sum

#sol3: O(len(J)+len(S))
class Solution: #20 ms	14.2 MB
    def numJewelsInStones(self, J: str, S: str) -> int:
        sum =0 
        map_J= {j:1 for j in J} #O(len(J))
        for s in S: #O(len(S))
            if s in map_J: #O(1)
                sum+=1
        return sum