class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        substring_tracker = 0
        charset = set()

        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l+=1
            
            charset.add(s[r])
            substring_tracker = max(substring_tracker, (r+1)-l)

        return substring_tracker

        