class Solution:
    def searchMatrix(self, matrix:list, target: int) -> bool:
        row = len(matrix)
        if not row:
            return False
        col = len(matrix[0])

        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False

        start = 0
        end = row - 1
        mid = 0
        while start <= end:
            mid = (start + end) // 2
            if matrix[mid][0] == target:
                return True
            elif target < matrix[mid][0]:
                end = mid - 1
            else:
                start = mid + 1

        i = start - 1
        if target < matrix[i][0] or target > matrix[i][-1]:
            return False
        start = 0
        end = col - 1
        mid = 0
        while start <= end:
            mid = (start + end) // 2
            if target == matrix[i][mid]:
                return True
            elif target < matrix[i][mid]:
                end = mid - 1
            else:
                start = mid + 1

        return False

sl = Solution()
t1 = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]

res = sl.searchMatrix(t1,3)

print(res)

sl = Solution()
t1 = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]

res = sl.searchMatrix(t1,13)
print(res)