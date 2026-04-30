class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
      char_counts = {}
      freq_char, l, max_length = 0,0,0

      for r in range(len(s)):

        char_counts[s[r]] = char_counts.get(s[r],0) + 1
        freq_char = max(char_counts[s[r]], freq_char)

        if r+1-l - freq_char <= k:
          max_length = max(r+1-l, max_length)

        else:
          char_counts[s[l]] -= 1
          if char_counts[s[l]] == 0:
            char_counts.pop(s[l])
          l += 1

      return max_length