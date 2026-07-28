class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        CS,CT={},{}
        for i in range(len(s)):
            CS[s[i]]= 1 + CS.get(s[i],0)
            CT[t[i]]= 1 + CT.get(t[i],0)
        
        return CS==CT

