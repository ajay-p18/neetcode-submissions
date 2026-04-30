class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1_dict = {}
        s2_dict = {}
        l = 0

        for char in range(len(s1)):
            s1_dict[s1[char]] = s1_dict.get(s1[char],0) + 1
        
        for r in range(len(s2)):
            s2_dict[s2[r]] = s2_dict.get(s2[r],0) + 1   

            if r+1-l == len(s1):
                if s1_dict == s2_dict:
                    return True
                else:
                    s2_dict[s2[l]] -= 1
                    if s2_dict[s2[l]] == 0:
                        s2_dict.pop(s2[l]) 
                    l += 1

        return False
