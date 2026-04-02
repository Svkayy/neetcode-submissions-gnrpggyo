class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = set(['+', '/', '*', '-'])
        tokens = tokens[::-1]
        calc = []
        while tokens:
            first = tokens.pop()
            if first not in ops:
                calc.append(int(first))
            else:
                b = calc.pop()
                a = calc.pop()
                if first == '+':
                    calc.append(a+b)
                elif first == '-':
                    calc.append(a-b)
                elif first == '*':
                    calc.append(a * b)
                else:
                    calc.append(int(a / b))
        return calc[0]
