class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

      unique_chars = dict()
      max_window = 0
      maxFreq = 0
      l = 0

      for r in range(len(s)):
        window_size = r+1-l
        unique_chars[s[r]] = unique_chars.get(s[r],0) + 1
        maxFreq = max(maxFreq, max(unique_chars.values()))
        
        if window_size - maxFreq <= k:
          max_window +=1
        
        else:
          unique_chars[s[l]]-=1
          l+=1
          
      return max_window
      