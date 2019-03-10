class Solution:
    def fullJustify(self, words:list, maxWidth: int):
        n = len(words)
        if not n:
            return []
        if n == 1:
            space_n = maxWidth - n
            return [words[0] + ' ' * space_n]
        res = []
        sub_res = [words[0]]
        cnt_sub = 1
        len_sub = len(words[0])
        i = 1
        while i < n:
            len_wd = len(words[i])
            if len_sub + len_wd + cnt_sub <= maxWidth:
                sub_res.append(words[i])
                i += 1
                cnt_sub += 1
                len_sub += len_wd
            else:
                if cnt_sub > 1:
                    cnt_space_must = (maxWidth - len_sub) // (cnt_sub - 1)
                    cnt_space_mod = (maxWidth - len_sub) % (cnt_sub - 1)
                    tmp_sub = sub_res[0]
                    for j in range(1, cnt_sub):
                        tmp_sub = tmp_sub + ' ' * cnt_space_must
                        if cnt_space_mod:
                            tmp_sub = tmp_sub + ' '
                            cnt_space_mod -= 1
                        tmp_sub = tmp_sub + sub_res[j]
                    res.append(tmp_sub)
                else:
                    cnt_space_must = maxWidth - len(sub_res[0])
                    tmp_sub = sub_res[0] + ' ' * cnt_space_must
                    res.append(tmp_sub)


                sub_res = [words[i]]
                cnt_sub = 1
                len_sub = len(words[i])
                i += 1

        space_n = maxWidth - (len_sub + cnt_sub - 1)
        tmp_sub = sub_res[0]
        for j in range(1, cnt_sub):
            tmp_sub = tmp_sub + ' ' + sub_res[j]

        tmp_sub = tmp_sub + ' ' * space_n

        res.append(tmp_sub)
        return res






# sl = Solution()
# words = ["This", "is", "an", "example", "of", "text", "justification."]
# maxWidth = 16
#
# res = sl.fullJustify(words,maxWidth)
#
# for x in res:
#     print(x)

# sl = Solution()
# words = ["What","must","be","acknowledgment","shall","be"]
# maxWidth = 16
#
# res = sl.fullJustify(words,maxWidth)
#
# for x in res:
#     print(x)

sl = Solution()
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20

res = sl.fullJustify(words,maxWidth)

for x in res:
    print(x)