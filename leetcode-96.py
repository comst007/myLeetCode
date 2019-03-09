class Solution:
    def numTrees(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 1
        if n == 2:
            return 2

        res = [0] * (n + 1)
        res[0] = 1
        res[1] = 1
        res[2] = 2
        for i in range(3, n + 1):
            sum = 0
            for j in range(i):
                sum += res[j] * res[i - 1 - j]
            res[i] = sum

        return res[-1]





sl = Solution()

res = sl.numTrees(3)
print(res)