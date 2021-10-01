class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for i in s:
            if i == '(':
                stack.append(1)
            elif i == ')':
                if len(stack):
                    top = stack.pop()
                else:
                    return False
                if top != 1:
                    return False
            elif i == '{':
                stack.append(2)
            elif i == '}':
                if len(stack):
                    top = stack.pop()
                else:
                    return False
                if top != 2:
                    return False
                
            elif i == '[':
                stack.append(3)
            elif i == ']':
                if len(stack):
                    top = stack.pop()
                else:
                    return False
                if top != 3:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False