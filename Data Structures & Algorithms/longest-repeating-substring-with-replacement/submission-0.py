class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        sList = list(s)
        L = 0
        length = 0
        windowCount = defaultdict(int)
        for R in range(len(sList)):
            windowCount[sList[R]] += 1
            while (R - L + 1) - max(windowCount.values()) > k:
                windowCount[sList[L]] -= 1
                L += 1
            length = max(length, R - L + 1)
        return length