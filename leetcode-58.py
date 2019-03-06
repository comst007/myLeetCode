class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        if not n:
            return 0
        h = 1
        while h <= n and s[-h] == " ":
            h += 1

        if h > n:
            return 0
        l = h
        while l <= n and s[-l] != ' ':
            l += 1
        return l - h
