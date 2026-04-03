class Solution:
    def isPalindrome(self, s: str) -> bool:
        k = ""
        for char in s:
            if char.isalnum():
                k += char.lower()
        l = 0
        r = len(k) - 1
        while l < r:
            if k[l] != k[r]:
                return False
            l += 1
            r -= 1
        return True