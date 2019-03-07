class Solution:
    def zero_row(self, matrix:list, r:int, c:int, i:int):
        for k in range(c):
            matrix[i][k] = 0

    def zero_col(self,  matrix:list, r:int, c:int, j:int):
        for k in range(r):
            matrix[k][j] = 0

    def setZeroes(self, matrix: list) -> None:

        row = len(matrix)
        if not row:
            return
        col = len(matrix[0])

        row_set = set({})
        col_set = set({})

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    row_set.add(i)
                    col_set.add(j)

        for x in row_set:
            self.zero_row(matrix, row, col, x)

        for y in col_set:
            self.zero_col(matrix, row, col, y)


sl = Solution()

t1 = [
  [1,1,1],
  [1,0,1],
  [1,1,1]
]

sl.setZeroes(t1)

for x in t1:
    print(x)

t1 = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]

sl.setZeroes(t1)

for x in t1:
    print(x)
