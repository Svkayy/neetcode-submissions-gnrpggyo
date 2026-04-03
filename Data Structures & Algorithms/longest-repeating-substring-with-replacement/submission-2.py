class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        maxcount = 0
        length = float('-inf')
        L = 0
        for R in range(len(s)):
            count[s[R]] += 1
            maxcount = max(count[s[R]], maxcount)
            while R - L + 1 - maxcount > k:
                count[s[L]] -= 1
                L += 1
            length = max(length, R - L + 1)
        if length == float('-inf'):
            return 0
        return length