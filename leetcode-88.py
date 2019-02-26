class Solution:
    def _find_upper(self, arr, cnt, key):
        start = 0
        end = cnt - 1
        while start < end:
            mid = (start + end) // 2
            if key < arr[mid]:
                end = mid
            elif key == arr[mid]:
                start = mid + 1
            else:
                start = mid + 1

        return start
    def _right_shift(self, arr, cnt, pos):
        i = cnt - 1
        while i >= pos:
            arr[i + 1] = arr[i]
            i = i - 1

    def merge(self, nums1, m, nums2, n):
        for x in nums2:
            if x >= nums1[m - 1]:
                nums1[m] = x
                m = m + 1
            else:
                pos = self._find_upper(nums1, m, x)
                self._right_shift(nums1, m, pos)
                nums1[pos] = x
                m = m + 1



sl = Solution()

arr1 = [1,2,3,0,0,0]
arr2 = [2,5,6]

res = sl.merge(arr1, 3, arr2, 3)

print(arr1)