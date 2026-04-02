class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = {}
        window = {}

        for char in t:
            countT[char] = countT.get(char, 0) + 1
        
        m = float('inf')
        best = (-1, -1)


        need = sum(countT.values())
        have = 0

        L = 0
        for R in range(len(s)):
            if s[R] in countT and window.get(s[R], 0) < countT[s[R]]:
                have += 1
            window[s[R]] = window.get(s[R], 0) + 1
            
            while have == need:
                if m > R - L + 1:
                    m = R - L + 1
                    best = (L, R)
                window[s[L]] -= 1
                if s[L] in countT and window[s[L]] < countT[s[L]]:
                    have -= 1
                L += 1        
        
        return s[best[0]: best[1] + 1]