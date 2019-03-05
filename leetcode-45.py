class Solution:
    def dfs(self, nums:list, cur_pos:int, min_dict:dict):

        if cur_pos >= len(nums):
            return None
        n = len(nums)
        if cur_pos == n - 1:
            min_dict[cur_pos] = 0
            return 0
        if cur_pos in min_dict:
            return min_dict[cur_pos]

        cur_min = None
        tmp_min = None
        tmp_res = None
        theory_min = None
        if cur_pos + nums[cur_pos] >= n - 1:
            theory_min = 1
        else:
            theory_min = 2
        for i in range(nums[cur_pos], 0, -1):
            if cur_pos + i < n:

                if cur_pos + i in min_dict and min_dict[cur_pos + i]:
                    tmp_res = min_dict[cur_pos + i]
                else:
                    tmp_res = self.dfs(nums, cur_pos + i, min_dict)

                if tmp_res is None:
                    continue
                tmp_min = tmp_res + 1
                if tmp_min == theory_min:
                    cur_min = tmp_min
                    min_dict[cur_pos] = cur_min
                    return cur_min
                if not cur_min or tmp_min < cur_min:
                    cur_min = tmp_min
        min_dict[cur_pos] = cur_min
        return cur_min


    def jump(self, nums:list):
        if not nums:
            return 0
        min_step = {}
        self.dfs(nums, 0, min_step)
        return min_step[0]


sl = Solution()

t1 = [2,3,1,1,4]

res = sl.jump(t1)

print(res)

sl = Solution()
t2 = [8,2,4,4,4,9,5,2,5,8,8,0,8,6,9,
      1,1,6,3,5,1,2,6,6,0,4,8,6,0,3,
      2,8,7,6,5,1,7,0,3,4,8,3,5,9,0,
      4,0,1,0,5,9,2,0,7,0,2,1,0,8,2,
      5,1,2,3,9,7,4,7,0,0,1,8,5,6,7,
      5,1,9,9,3,5,0,7,5]

res = sl.jump(t2)
print(res)
