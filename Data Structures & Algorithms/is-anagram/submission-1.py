class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        s_map = dict()
        t_map = dict()
        word_length = len(s)

        for c in range(len(s)):
            s_map[s[c]] = s_map.get(s[c],0)+1
        
        for c in range(len(t)):
            t_map[t[c]] = t_map.get(t[c],0)+1
        
        for c in s:
            if c in s_map and c in t_map:
                if s_map.get(c, 0) == t_map.get(c,0):
                    word_length -= 1

        return word_length == 0