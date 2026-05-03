class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

     charSet = set()
     max_window = 0
     l = 0

     for r in range(len(s)):

      while s[r] in charSet:
        charSet.remove(s[l])
        l += 1
      charSet.add(s[r])
      curr_window = r+1-l
      max_window = max(max_window, curr_window)
     
     return max_window