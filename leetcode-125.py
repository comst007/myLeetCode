class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        if not n:
            return True

        s = s.strip()
        s = list(filter(lambda x: x.isalnum(), s))
        s = list(map(lambda x: x.lower(), s))
        n = len(s)
        if not n:
            return True
        i = 0
        j = n -1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1

        return True

sl = Solution()
t1 = "A man, a plan, a canal: Panama"
res = sl.isPalindrome(t1)
print(res)

sl = Solution()
t1 = "race a car"
res = sl.isPalindrome(t1)
print(res)


sl = Solution()
t1 = " "
res = sl.isPalindrome(t1)
print(res)