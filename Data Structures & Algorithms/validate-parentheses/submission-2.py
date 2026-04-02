class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {"(" : ")", "{" : "}", "[" : "]"}
        stack = []
        for char in s:
            if char in hashmap.keys():
                stack.append(char)
            else:
                if not stack:
                    return False
                i = stack.pop()
                if char != hashmap[i]:
                    return False
        if not stack:
            return True
        return False
                
        