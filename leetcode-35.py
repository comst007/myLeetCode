class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        cnt = len(nums)
        if not cnt:
            return 0
        if nums[-1] < target:
            return cnt
        start = 0
        end = cnt - 1
        mid = 0
        while start < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid

        return start