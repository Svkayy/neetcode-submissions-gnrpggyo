class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        for char in tokens:
            if char not in '/*-+':
                stack.append(char)
            else:
                b = stack.pop()
                a = stack.pop()
                sol = float('inf')
                if char == "+":
                    sol = int(a) + int(b)
                elif char == "-":
                    sol = int(a) - int(b)
                elif char == "*":
                    sol = int(a) * int(b)
                else:
                    sol = int(int(a) / int(b))
                stack.append(str(sol))
        
        return int(stack.pop())
