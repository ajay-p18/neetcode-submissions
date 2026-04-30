

class Solution:
    
    
    def isValid(self, s: str) -> bool:

        open_close = {'(':')', '{':'}', '[':']'}
        brackets = list()

        for c in s:
            if c in open_close.keys():
                brackets.append(c)
            else:
                if brackets and c == open_close[brackets[len(brackets)-1]]:
                    brackets.remove(brackets[len(brackets)-1])
                else:
                    return False
            
        return len(brackets) == 0
