class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1 = defaultdict(int)
        for char in s1:
            d1[char] += 1
        
        sor1 = sorted(s1)

        for R in range(len(s2)):
            if s2[R] not in d1:
                continue
            if R+len(s1)-1 < len(s2) and sorted(s2[R:R+len(s1)]) == sor1:
                return True
        
        return False
            