class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {'(':')', '[':']', '{':'}'}
        for char in s:
            if char in d.keys():
                stack.append(char)
            else:
                if not stack or d[stack.pop()] != char:
                    return False
        
        return not stack
            