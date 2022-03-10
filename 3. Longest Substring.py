class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        k=set()
        l=0
        res=0
        for i in range(len(s)):
            while s[i] in k:
                k.remove(s[l])
                l+=1
            k.add(s[i])
            res = max(res, len(k))
        return res