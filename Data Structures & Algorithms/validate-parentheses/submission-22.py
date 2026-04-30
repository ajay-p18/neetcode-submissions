

class Solution:
    
    
    def isValid(self, s: str) -> bool:

        stack = []
        valid_brackets = {')':'(', ']':'[', '}':'{'}

        for curr in s:
            if curr not in valid_brackets.keys():
                stack.append(curr)
            else:
                if stack and stack[-1] == valid_brackets[curr]:
                    stack.pop()
                else:
                    return False
        
        print(stack)
        return len(stack) == 0