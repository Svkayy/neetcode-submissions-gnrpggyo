class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowered = ""
        for char in s.lower():
            if char.isalnum():
                lowered += char
        if not lowered:
            return True
        a = 0
        b = len(lowered) - 1
        while a < b:
            if lowered[a] != lowered[b]:
                return False
            a += 1
            b -= 1
        return True
