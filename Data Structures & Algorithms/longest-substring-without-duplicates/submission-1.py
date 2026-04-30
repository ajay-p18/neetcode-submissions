class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        charSet = set()
        l = 0
        longest_subset = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1

            charSet.add(s[r])
            longest_subset = max(longest_subset, (r+1)-l)

        return longest_subset