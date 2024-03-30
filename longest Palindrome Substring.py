class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]: return s

        c = len(s)-1
        cenLeft, cenRght = 0, 0
        pal = s[0]

        while cenRght < c:
            while cenRght < c:
                if s[cenRght] != s[cenRght + 1]: break
                cenRght = cenRght + 1
            i, j = cenLeft, cenRght

            while i > 0 and j < c:
                if s[i - 1] != s[j + 1]: break
                i -= 1; j += 1

            if len(pal) < j + 1 - i:
                pal = s[i:j+1]

            cenRght = cenRght +1
            cenLeft = cenRght

        return pal
        
        
