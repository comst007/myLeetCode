class Solution:
    def curentCode(self, val:str):

        n = len(val)
        if not n:
            return ""
        elif n == 1:
            return "{}{}".format(1, val)
        res = ""
        cur_ch = val[0]
        cnt_ch = 1
        for i in range(1, n):
            if val[i] == cur_ch:
                cnt_ch += 1
            else:
                res = "{}{}{}".format(res, cnt_ch, cur_ch)
                cur_ch = val[i]
                cnt_ch = 1

        res = "{}{}{}".format(res, cnt_ch, cur_ch)

        return res
    def countAndSay(self, n: int) -> str:
        val = "1"
        def gameCode(val:str):
            while True:
                last_val = val
                val = self.curentCode(val)
                yield last_val

        i = 0
        code = gameCode("1")
        res = None
        while i < n:
            res = next(code)
            i = i + 1

        return res


sl =Solution()

res = sl.countAndSay(6)

print(res)