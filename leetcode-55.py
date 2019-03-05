class Solution:
    def dfs(self, nums:list, cur_pos:int, pre_dict:dict):
        n = len(nums)

        if cur_pos == n - 1:
            pre_dict[cur_pos] = True
            return True
        if nums[cur_pos] == 0:
            pre_dict[cur_pos] = False
            return False

        if cur_pos + nums[cur_pos] >= n:
            pre_dict[cur_pos] = True
            return True


        for k in range(nums[cur_pos], 0, -1):
            if cur_pos + k in pre_dict and not pre_dict[cur_pos + k]:
                continue
            if cur_pos + k < n:
                if self.dfs(nums, cur_pos + k, pre_dict):
                    pre_dict[cur_pos] = True
                    return True

        pre_dict[cur_pos] = False
        return False

    def canJump(self, nums: list) -> bool:
        n = len(nums)
        if not n:
            return False
        if n == 1:
            return True
        info_dict = {}
        res = self.dfs(nums, 0, info_dict)
        return res

sl = Solution()

t1 = [2,3,1,1,4]

res = sl.canJump(t1)

print(res)

t2 = [3,2,1,0,4]
sl = Solution()


res = sl.canJump(t2)

print(res)

t3 = [2,0,6,9,8,4,5,0,8,9,1,2,
      9,6,8,8,0,6,3,1,2,2,1,2,
      6,5,3,1,2,2,6,4,2,4,3,0,
      0,0,3,8,2,4,0,1,2,0,1,4,
      6,5,8,0,7,9,3,4,6,6,5,8,
      9,3,4,3,7,0,4,9,0,9,8,4,
      3,0,7,7,1,9,1,9,4,9,0,1,
      9,5,7,7,1,5,8,2,8,2,6,8,
      2,2,7,5,1,7,9,6]

res = sl.canJump(t3)
print(res)