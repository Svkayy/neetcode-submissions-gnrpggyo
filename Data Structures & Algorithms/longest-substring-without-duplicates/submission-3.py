class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = float('-inf')
        seen = set()
        L = 0
        for R in range(len(s)):
            while s[R] in seen:
                seen.remove(s[L])
                L += 1
            seen.add(s[R])
            length = max(length, R - L + 1)
        if length == float('-inf'):
            return 0
        return length
