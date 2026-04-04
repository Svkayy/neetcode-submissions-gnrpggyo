class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1 = defaultdict(int)
        for char in s1:
            d1[char] += 1
        length = len(s1)
        L = 0

        d2 = defaultdict(int)

        for R in range(len(s2)):

            d2[s2[R]] += 1

            if R - L + 1 > length:
                d2[s2[L]] -= 1
                if d2[s2[L]] == 0:
                    del d2[s2[L]]
                L += 1
                
            if R - L + 1 == length and d1 == d2:
                return True
            
       
        return False
            