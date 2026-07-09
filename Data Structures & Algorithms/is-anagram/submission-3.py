class Solution:
     def isAnagram(self, s: str, t: str) -> bool:
        if len(s)==len(t):
            g=sorted(s)
            h=sorted(t)
            for i in range(len(s)):
                if g[i]!=h[i]:
                    return False
            return True
        return False