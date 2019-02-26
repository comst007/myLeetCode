class Solution:
    def _revert(self, arr, start, end):
        while start < end:
            tmp = arr[start]
            arr[start] = arr[end]
            arr[end] = tmp
            start = start + 1
            end = end - 1

    def rotate(self, nums: list[int], k: int):
        if not nums:
            return
        cnt = len(nums)
        if cnt == 1:
            return

        k = k % cnt
        if k == 0:
            return
        self._revert(nums, 0, cnt - 1)
        self._revert(nums, 0, k -1)
        self._revert(nums, k, cnt - 1)

