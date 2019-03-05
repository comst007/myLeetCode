class Solution:
    def trap(self, height: list):
        len_h = len(height)
        if not len_h:
            return 0
        if len_h == 1:
            return 0
        if len_h == 2:
            return 0
        max_l = [0] * len_h
        max_r = [0] * len_h
        cur_max = 0
        for i in range(len_h):
            if height[i] >= cur_max:
                cur_max = height[i]
                max_l[i] = cur_max
            else:
                max_l[i] = cur_max

        cur_max = 0
        for i in range(len_h -1, -1, -1):
            if height[i] >= cur_max:
                cur_max = height[i]
                max_r[i] = cur_max
            else:
                max_r[i] = cur_max

        res = 0
        for i in range(len_h):
            cur_sum = min(max_r[i], max_l[i]) - height[i]
            res += cur_sum

        return res 


sl = Solution()

arr = [0,1,0,2,1,0,1,3,2,1,2,1]
res = sl.trap(arr)

print(res)