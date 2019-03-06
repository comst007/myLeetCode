from pprint import pprint

class Solution:
    def dfs(self, nums:list, cur_pos:int, res_sub:list, res_total:list):
        n = len(nums)
        if cur_pos == n:
            res_total.append(res_sub[:])
            return

        res_total.append(res_sub[:])

        for i in range(cur_pos, n):
            res_sub.append(nums[i])
            self.dfs(nums, i + 1, res_sub, res_total)
            res_sub.pop()


    def subsets(self, nums:list):
        n = len(nums)
        if not n:
            return [[]]
        if n == 1:
            return [[], [nums[0]]]

        res = []
        self.dfs(nums,0,[],res)
        return res


sl = Solution()

t1 = [1,2,3]

res = sl.subsets(t1)
pprint(res)
