class Solution:
    def maxProfit1(self, prices: list) -> int:

        n = len(prices)
        if not n:
            return 0
        if n == 1:
            return 0
        f_arr = [0] * n
        f_max = [0] * (n + 1)

        f_arr[-1] = - prices[-1]

        res_max = 0
        max_price = 0
        flag = True
        for i in range(n - 2, -1, -1):
            if flag and prices[i] >= prices[i + 1]:
                continue
            else:
                flag = False
            tmp_max = None
            for j in range(i + 1, n):
                max_j = prices[j] - prices[i] + f_max[j + 1]
                if tmp_max is None or max_j > tmp_max:
                    tmp_max = max_j
            f_arr[i] = tmp_max
            if tmp_max > res_max:
                res_max = tmp_max
            f_max[i] = res_max

        return res_max

    def maxProfit(self, prices: list) -> int:
        n = len(prices)
        if not n:
            return 0
        if n == 1:
            return 0
        max_res = 0
        i = 0
        while i < n:
            while i + 1 < n and prices[i] > prices[i + 1]:
                i += 1

            valley = prices[i]
            while i + 1 < n and prices[i] < prices[i + 1]:
                i += 1

            peak = prices[i]

            max_res += peak - valley
            i += 1

        return max_res

sl = Solution()
t1 = [7,1,5,3,6,4]
res = sl.maxProfit(t1)
print(res)

sl = Solution()
t1 = [1,2,3,4,5]
res = sl.maxProfit(t1)
print(res)

sl = Solution()
t1 = list(range(1000, -1, -1))
res = sl.maxProfit(t1)
print(res)


