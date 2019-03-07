class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 3

        res = [0] * n
        res[0] = 1
        res[1] = 2
        res[2] = 3
        for i in range(3, n):
            res[i] = res[i - 1] + res[i - 2]


        return res[-1]