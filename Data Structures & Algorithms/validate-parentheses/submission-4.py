class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {'(':')', '[':']', '{':'}'}
        for char in s:
            if char in d.keys():
                stack.append(char)
            else:
                if not stack:
                    return False
                tmp = stack.pop()
                if char != d[tmp]:
                    return False
        if stack:
            return False
        return True
            