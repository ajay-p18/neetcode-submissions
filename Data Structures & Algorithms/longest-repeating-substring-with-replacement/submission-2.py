class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

      letter_map = dict()
      count = 0
      l = 0
      maxF = 0

      for r in range(len(s)):
        letter_map[s[r]] = letter_map.get(s[r], 0) + 1
        window_size = r+1-l
        maxF = max(maxF, max(letter_map.values()))

        if window_size - maxF <= k:
          count +=1
        else:
          letter_map[s[l]] -= 1
          l +=1

  
      return count

      