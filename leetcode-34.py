class Solution:
    def searchRange(self, nums, target: int):
        cnt = len(nums)
        if not cnt:
            return [-1, -1]
        if target > nums[-1] or target < nums[0]:
            return [-1, -1]
        start = 0
        end = cnt - 1
        mid = 0
        bound = [-1] * 2


        while start < end:
            mid = (start + end) // 2

            if nums[mid] == target:
                end = mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        if nums[start] != target:
            return bound
        bound[0] = start
        bound[1] = start
        end = cnt - 1
        while start < end:
            mid = (start + end) // 2 + 1
            if nums[mid] == target:
                start = mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1


        bound[1] = start

        return bound

arr = [5,7,7,8,8,10]
target = 8

sl = Solution()

res = sl.searchRange(arr, target)

print(res)