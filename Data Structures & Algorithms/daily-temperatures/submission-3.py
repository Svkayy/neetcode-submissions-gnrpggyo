class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for _ in range(len(temperatures))]
        stack = []
        for index, temp in enumerate(temperatures):
            if not stack:
                stack.append(index)
                continue
            while stack and temp > temperatures[stack[-1]]:
                i = stack.pop()
                res[i] = index - i
            stack.append(index)
        
        return res
