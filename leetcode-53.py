class Solution:
    def maxSubArray(self, nums:list):
        n = len(nums)
        if not n:
            return None
        if n == 1:
            return nums[0]

        cur_max = nums[0]
        tmp_max = nums[0]
        for i in range(1, n):
            if tmp_max > 0:
                tmp_max += nums[i]
            else:
                tmp_max = nums[i]

            if tmp_max > cur_max:
                cur_max = tmp_max

        return cur_max


sl = Solution()

t1 = [-2,1,-3,4,-1,2,1,-5,4]

res = sl.maxSubArray(t1)

print(res)
