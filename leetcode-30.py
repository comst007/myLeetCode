class Solution:

    def ifMatch(self, s:str, words:list):
        i = 0
        wd_len = len(words[0])
        s_len = len(s)
        while i <= s_len - wd_len:
            sub_s = s[i:i + wd_len]
            if sub_s in words:
                words.remove(sub_s)
                i += wd_len
            else:
                return False

        if not len(words):
            return True
        else:
            return False

    def findSubstring(self, s: str, words:list):
        s_len = len(s)
        if not s_len:
            return []

        words_len = len(words)
        res = []
        if not words_len:
            return []
        sub_len = words_len * len(words[0])
        s_len = len(s)
        i = 0
        while i <= s_len - sub_len:
            sub_s = s[i:i + sub_len]
            if self.ifMatch(sub_s, words[:]):
                res.append(i)
                i += 1
            else:
                i += 1


        return res

s1 = "barfoothefoobarman"

w1 = ["foo", "bar"]

s2 = "wordgoodgoodgoodbestword",
w2 = ["word", "good", "best", "word"]

s3 = "barfoofoobarthefoobarman"
w3 = ["bar","foo","the"]
sl = Solution()

res1 = sl.findSubstring(s1, w1)
print(res1)

res2 = sl.findSubstring(s2, w2)
print(res2)

res3 = sl.findSubstring(s3, w3)
print(res3)
# res4 = sl.findAll(s1, "foo")
# print(res4)
