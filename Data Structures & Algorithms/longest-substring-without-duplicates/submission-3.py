class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        max_window_size = 0

        for r in range(len(s)):

            if s[r] in charSet:
                while s[r] in charSet:
                    charSet.remove(s[l])
                    l+=1


            charSet.add(s[r])
            max_window_size = max(max_window_size, r+1-l)
        
        return max_window_size
