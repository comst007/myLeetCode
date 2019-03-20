class Solution:
    def preHandle(self, prices: list):
        n = len(prices)
        res = [0] * n
        cur_max = prices[-1]
        for i in range(n - 1, -1, -1):
            if prices[i] > cur_max:
                cur_max = prices[i]
            res[i] = cur_max

        return res
    def maxProfit(self, prices: list) -> int:
        n = len(prices)
        if not n:
            return 0
        if n == 1:
            return 0

        right_max = self.preHandle(prices)
        res_max = None
        for i in range(n):
            cur_max = right_max[i] - prices[i]
            if res_max is None or cur_max > res_max:
                res_max = cur_max

        return res_max



t1 = [7,1,5,3,6,4]
sl = Solution()
res = sl.maxProfit(t1)
print(res)

t1 = [7,6,4,3,1]
sl = Solution()
res = sl.maxProfit(t1)
print(res)

