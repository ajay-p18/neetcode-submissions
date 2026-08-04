class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        s = list(s)
        # print(s)
        r = 0
        charSize = 0

        while (r < len(s)):
            # print(s[r])

            if s[r] not in charSet:
                charSet.add(s[r])
                charSize = max(charSize, r+1-l)
                r += 1
                
            else:
                charSet.remove(s[l])
                l+=1
            
            
        
        return charSize
