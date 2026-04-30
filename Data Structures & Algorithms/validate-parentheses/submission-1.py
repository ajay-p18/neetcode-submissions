

class Solution:
    
    def peek_stack(self, stack):
        if stack:
            return stack[-1]
        else:
            return None
    
    def isValid(self, s: str) -> bool:

        count = 0
        char_stack = []
        open_brackets = ["(", "{", "["]

        for char in s:
            if char in open_brackets:
                count+=1
                char_stack.append(char)
            else:
                top_element = self.peek_stack(char_stack)
                if top_element == '[':
                    if char == ']':
                        count -= 1
                        char_stack.pop()
                    else:
                        count+=1
                elif top_element == '(':
                    if char == ')':
                        count -= 1
                        char_stack.pop()
                    else:
                        count+=1
                elif top_element == '{':
                    if char == '}':
                        count -= 1
                        char_stack.pop()
                    else:
                        count+=1
                else:
                    count+=1
        

        if count == 0:
            return True

        return False

        