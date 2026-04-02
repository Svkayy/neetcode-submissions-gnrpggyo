class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        seen = set(s1)
        sList = list(s2)
        L = 0
        found = False
        for R in range(len(sList)):
            if sList[R] in seen:
                if sorted(sList[R:R+len(s1)]) == sorted(s1):
                    return True
            else:
                L = R
        return found

                

        
        