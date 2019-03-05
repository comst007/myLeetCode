class Solution:
    def __init__(self):
        self.cnt = 0
        self.dict = {}
    def isAllStar(self, p:str):
        for x in p:
            if x != "*":
                return False
        return True
    def isMatch(self, s: str, p: str) -> bool:

        s_len = len(s)
        p_len = len(p)
        # print("--->", self.cnt, s_len, p_len)

        if (s_len, p_len) in self.dict:
            if self.dict[(s_len, p_len)]:
                return True
            else:
                return False

        if not p_len and not s_len:
            self.dict[(s_len, p_len)] = True
            return True

        if not p_len:
            self.dict[(s_len, p_len)] = False
            return False

        if not s_len and self.isAllStar(p):
            self.dict[(s_len, p_len)] = True
            return True
        elif not s_len and not self.isAllStar(p):
            self.dict[(s_len, p_len)] = False
            return False

        if p[-1] != "*" and p[-1] != "?":
            k = 1
            while k <= p_len and p[-k] != "*" and p[-k] != "?":
                k += 1

            if (k - 1, k - 1) in self.dict:
                if not self.dict[(k - 1, k - 1)]:
                    return False
            if s_len < k - 1:
                self.dict[(s_len, p_len)] = False
                return False
            else:
                i = 1
                while i < k:
                    if s[-i] != p[-i]:
                        self.dict[(s_len, p_len)] = False
                        return False
                    else:
                        self.dict[(i, i)] = True
                        i += 1




        i = 0
        j = 0
        while i < s_len and j < p_len:
            if p[j] == "*":
                if j == p_len - 1:
                    self.dict[(s_len, p_len)] = True
                    return True
                if p[j + 1] == "*":
                    j += 1
                    continue

                for k in range(i, s_len):
                    self.cnt += 1
                    if self.isMatch(s[k:], p[j + 1:]):
                        self.cnt -= 1
                        self.dict[(s_len, p_len)] = True
                        return True
                    self.cnt -= 1

                self.dict[(s_len, p_len)] = False
                return False
            elif p[j] == "?":
                i += 1
                j += 1
            else:
                if s[i] != p[j]:
                    self.dict[(s_len, p_len)] = False
                    return False
                else:
                    i += 1
                    j += 1
        if i == s_len and (j == p_len or self.isAllStar(p[i:])):
            self.dict[(s_len, p_len)] = True
            return True
        else:
            self.dict[(s_len, p_len)] = False
            return False


sl = Solution()

s = "aa"
p = "a"


res = sl.isMatch(s, p)
print(s, p, res)

sl = Solution()
s = "aa"
p = "*"

res = sl.isMatch(s, p)
print(s, p, res)

sl = Solution()
s = "cb"
p = "?a"

res = sl.isMatch(s, p)
print(s, p, res)

sl = Solution()
s = "adceb"
p = "*a*b"
res = sl.isMatch(s, p)
print(s, p, res)

sl = Solution()
s = "acdcb"
p = "a*c?b"
res = sl.isMatch(s, p)
print(s, p, res)

sl = Solution()
s = "abbabaaabbabbaababbabbbbbabbbabbbabaaaaababababbbabababaabbababaabbbbbbaaaabababbbaabbbbaabbbbababababbaabbaababaabbbababababbbbaaabbbbbabaaaabbababbbbaababaabbababbbbbababbbabaaaaaaaabbbbbaabaaababaaaabb"
p = "**aa*****ba*a*bb**aa*ab****a*aaaaaa***a*aaaa**bbabb*b*b**aaaaaaaaa*a********ba*bbb***a*ba*bb*bb**a*b*bb"

res = sl.isMatch(s, p)
print(res)



