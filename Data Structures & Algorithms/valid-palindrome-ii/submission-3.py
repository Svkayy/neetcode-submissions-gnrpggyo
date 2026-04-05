class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(k, i, j):
            while i < j:
                if k[i] != k[j]:
                    return False
                i += 1
                j -= 1
            return True

        L = 0
        R = len(s) - 1
        while L < R:
            if s[L] != s[R]:
                return isPalindrome(s, L+1, R) or isPalindrome(s, L, R-1)
            
            L += 1
            R -= 1
        return True