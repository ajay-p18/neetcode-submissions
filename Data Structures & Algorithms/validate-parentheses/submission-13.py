

class Solution:
    
    
    def isValid(self, s: str) -> bool:
        stack = []
        paren_list = {')': '(', ']':'[', '}':'{'}

        for current in s:
            if current in paren_list.values():
                stack.append(current)
            else:
                if stack and paren_list[current] == stack[-1]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0

