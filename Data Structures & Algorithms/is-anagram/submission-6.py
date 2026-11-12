class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_tracker = dict()
        t_tracker = dict()

        flag = False

        for c in s:
            if c not in s_tracker:
                s_tracker[c] = 0
            s_tracker[c]= s_tracker.get(c,0) + 1

        for c in t:
            if c not in t_tracker:
                t_tracker[c] = 0
            t_tracker[c] += 1

        print(s_tracker)
        print(t_tracker)

        if len(s_tracker) == len(t_tracker):

            for i in s_tracker.keys():
                
                if i in t_tracker and s_tracker[i] == t_tracker[i]:
                    flag = True
                else:
                    return False
        
        return flag


        