class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dt = defaultdict(int)
        ds = defaultdict(int)

        have = 0
        need = 0

        length = float('inf')
        res = ""

        for char in t:
            dt[char] += 1
        
        need = len(dt)
        
        L = 0
        for R in range(len(s)):
            ds[s[R]] += 1

            if s[R] in dt and ds[s[R]] == dt[s[R]]:
                have += 1
            
            while have == need:
                if R - L + 1 < length:
                    res = s[L:R+1]
                    length = R - L + 1
                
                if s[L] in dt and ds[s[L]] == dt[s[L]]:
                    have -= 1
                ds[s[L]] -= 1
                L += 1
        
        return res

            

        
