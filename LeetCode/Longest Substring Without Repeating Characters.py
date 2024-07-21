class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p_s,p_e = 0,1
        N = len(s)
        if N == 0: 
            return 0
        else:
            ret = 1
            while p_s<=p_e and p_e<=N:
                if p_e<N and s[p_e] not in s[p_s:p_e]:
                    ret = max(ret, p_e-p_s+1)
                    p_e += 1
                else:
                    p_s +=1
            return ret
