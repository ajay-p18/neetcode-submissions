class Solution:
    def isValid(self, s: str) -> bool:
        open_close = {')': '(', ']':'[', '}':'{'}
        open = []

        for char in s:
            if char not in open_close.keys():
                open.append(char)

            else:
                if len(open) > 0 and open[-1] == open_close[char]:
                    open.pop()
                else:
                    return False
        
        return len(open) == 0
            