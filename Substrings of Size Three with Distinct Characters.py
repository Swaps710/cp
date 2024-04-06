class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        c=0
        n=len(s)
        for i in range(n-2):
            t=set(s[i:i+3])
            if len(t)==3:
                c+=1
        return c        
