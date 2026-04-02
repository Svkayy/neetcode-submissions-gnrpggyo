class Solution:
    def validPalindrome(self, s: str) -> bool:
        seen = set()
        k = list(s)
        if len(s) <= 1:
            return True
        for i in range(len(s) - 1):
            tmp = k[i]
            k[i] = ""
            seen.add("".join(k))
            k[i] = tmp
        for word in seen:
            if word == word[::-1]:
                return True
        return False

        