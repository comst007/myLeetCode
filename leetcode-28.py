class Solution:
    def _kmp_next(self, line):
        next_j = [0] * len(line)
        next_j[0] = -1
        cnt = len(line)
        if cnt == 1:
            return next_j
        next_j[1] = 0
        i = 2

        k = 0
        while i < cnt:
            k = next_j[i - 1]
            while k != -1 and line[i - 1] != line[k]:
                k = next_j[k]
            if k == -1:
                next_j[i] = 0
            else:
                next_j[i] = k + 1
            i += 1

        return next_j


    def strStr(self, haystack: str, needle: str):
        if not haystack:
            if not needle:
                return 0
            else:
                return -1
        if not needle:
            return 0
        left_len = len(haystack)
        right_len = len(needle)

        if left_len < right_len:
            return -1
        next_pos = self._kmp_next(needle)

        i = 0
        j = 0
        while i < left_len and j < right_len:
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = next_pos[j]

        if j < right_len and i == left_len:
            return -1
        elif j == right_len and i < left_len:
            return i - right_len
        else:
            return i - right_len



text1 = "hello"
p1 = "ll"

text2 = "aaaaa"
p2 = "bba"

text3 = "mississippi"

p3 = "issip"

sl = Solution()

res1 = sl.strStr(text1, p1)
print(res1)
res2 = sl.strStr(text2, p2)
print(res2)

res3 = sl.strStr(text3, p3)
print(res3)