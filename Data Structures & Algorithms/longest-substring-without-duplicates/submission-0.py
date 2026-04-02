class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        seen = set()
        sList = list(s)
        L = 0
        length = 0
        for R in range(len(sList)):
            while sList[R] in seen:
                seen.remove(sList[L])
                L += 1
            seen.add(sList[R])
            length = max(length, R - L + 1)
        return length