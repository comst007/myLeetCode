class Solution:
    def grayCode(self, n: int):
        if n == 0:
            return [0]
        if n == 1:
            return [0,1]
        res = []
        for x in range(0, 1 << n):
            res.append(x ^ (x >> 1))

        return res


sl = Solution()
x = 5
y = x >> 1

z = 1 << 3

res = sl.grayCode(2)
print(res)