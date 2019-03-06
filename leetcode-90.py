class Solution:
    def dfs(self, nums:list, cur_pos:int, sub_res:list, total_res:list):
        n = len(nums)
        if cur_pos == n:
            total_res.append(sub_res[:])
            return
        total_res.append(sub_res[:])

        last_i = -1
        for i in range(cur_pos, n):
            if last_i != -1 and nums[last_i] == nums[i]:
                continue
            last_i = i
            sub_res.append(nums[i])
            self.dfs(nums, i + 1, sub_res, total_res)
            sub_res.pop()

    def subsetsWithDup(self, nums: list):
        n = len(nums)
        if not n:
            return [[]]
        if n == 1:
            return [[], [nums[i]]]

        nums.sort()

        res = []
        self.dfs(nums, 0, [], res)
        return res


sl = Solution()

t1 = [1,2,2]

res = sl.subsetsWithDup(t1)
print(res)