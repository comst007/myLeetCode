class Solution:
    def dfs(self, nums:list, n:int, pos:int, sub_res:list, total_res:list, left:int):
        if left == 0:
            total_res.append(sub_res[:])
            return
        # if pos == n - 1 and left > 0:
        #     return
        if pos >= n:
            return
        for i in range(pos, n):
            sub_res.append(nums[i])
            self.dfs(nums,n,i + 1,sub_res,total_res,left - 1)
            sub_res.pop()

    def combine(self, n: int, k: int) -> list:
        if not n:
            return []
        if n < k:
            return []
        if n == k:
            return [list(range(1, n + 1))]
        nums = list(range(1, n + 1))
        res = []
        self.dfs(nums, n, 0, [], res, k)
        return res


sl = Solution()

res = sl.combine(4,2)
print(res)
