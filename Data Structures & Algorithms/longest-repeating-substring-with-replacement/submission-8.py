class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

      char_frequency = {}
      l = 0
      max_frequency, window_size, max_window = 0,0, 0

      for r in range(len(s)):
        char_frequency[s[r]] = char_frequency.get(s[r], 0) + 1
        window_size = (r+1) - l
        max_frequency = max(max_frequency, max(char_frequency.values()))

        if window_size - max_frequency <= k:
          max_window = max(max_window, window_size)
        
        else:
          left_value = s[l]
          l+=1
          char_frequency[left_value] -=1 
          if char_frequency[left_value] == 0:
            char_frequency.pop(left_value)

      return max_window


      
      