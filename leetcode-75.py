class Solution:
    def sortColors(self, nums: list) -> None:
        n = len(nums)
        if not n:
            return
        if n == 1:
            return

        last_red = -1
        last_blue = n
        i = 0
        while i < last_blue:
            if nums[i] == 1:
                i += 1
                continue
            elif nums[i] == 0:
                if i - 1 == last_red:
                    i += 1
                    continue
                tmp = nums[last_red + 1]
                nums[last_red + 1] = nums[i]
                nums[i] = tmp
                last_red += 1
            else:

                tmp = nums[last_blue - 1]
                nums[last_blue - 1] = nums[i]
                nums[i] = tmp
                last_blue -= 1


sl = Solution()

t1 = [2,0,2,1,1,0]

sl.sortColors(t1)

print(t1)