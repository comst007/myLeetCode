class Solution:
    def select(self, nums:list, res_cur:list, res_total:list):
        cnt_nums = len(nums)
        if not cnt_nums:
            res_total.append(res_cur[:])
        else:
            for i in range(cnt_nums):
                sub = nums[:]
                res_cur.append(nums[i])
                sub.pop(i)
                self.select(sub, res_cur, res_total)
                res_cur.pop()

    def permute(self, nums: list):
        res = []
        if not nums:
            return []
        self.select(nums, [], res)
        return res


arr = [1,2,3]
sl = Solution()
res = sl.permute(arr)
print(res)