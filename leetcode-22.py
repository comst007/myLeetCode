import pprint
class Solution:
    def _generate(self, res, cur, n, l, r):
        if l + r == 2 * n:
            res.append("".join(cur))
            return
        if l == n:
            new_res = cur + [")"] * (n - r)
            res.append("".join(new_res))
            return
        cur.append("(")
        self._generate(res, cur, n, l + 1, r)
        cur.pop()
        if r < l:
            cur.append(")")
            self._generate(res, cur, n, l, r + 1)
            cur.pop()

    def generateParenthesis(self, n: int):
        if n == 0:
            return [""]
        if n == 1:
            return ["()"]
        res = []
        self._generate(res,[],n,0,0)
        return res

sl = Solution()
res = sl.generateParenthesis(3)

pprint.pprint(res)