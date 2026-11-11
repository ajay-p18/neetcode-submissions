class Solution:
    def isValid(self, s: str) -> bool:
        
        tracker = []
        opp = {')':'(', '}':'{', ']':'['}
        s_len = len(s)

        # if len(s) == 1 or s[0] in opp.keys():
        #     return False

        for c in s:
            # print(f'c: {c}')
            if c not in opp.keys():
                tracker.append(c)
                print(tracker)
            else:
                
                if tracker == []:
                    return False

                else:
                    if tracker[-1] == opp[c]:
                        tracker.pop()
                    else: return False
        

        if len(tracker) > 0:
            return False
        
        return True





