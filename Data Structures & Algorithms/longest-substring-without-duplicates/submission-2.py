class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

      charSet = set()
      longest_substring = 0
      l = 0

      for r in range(len(s)):
        while s[r] in charSet:
          charSet.remove(s[l])
          l+=1
        
        charSet.add(s[r])
        longest_substring = max(longest_substring, r+1-l)

      return longest_substring