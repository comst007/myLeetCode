import pprint
class Solution:
    def isSafe(self, queen_arr:list, cur_row:int, cur_col:int):

        for i in range(len(queen_arr)):
            if cur_col == queen_arr[i]:
                return False
            if cur_row - i == abs(cur_col - queen_arr[i]):
                return False
        return True

    def dfs(self, n:int, queens_arr:list, cur_row:int, res_arr:list):
        if cur_row == n:
            res_arr.append(queens_arr[:])
            return
        for c in range(n):
            if self.isSafe(queens_arr, cur_row, c):
                queens_arr.append(c)
                self.dfs(n, queens_arr, cur_row + 1, res_arr)
                queens_arr.pop()

    def solveNQueens(self, n: int):
        res = []
        self.dfs(n, [], 0, res)
        arr = [["." * y + 'Q' + "." * (n - y - 1) for y in x ] for x in res]
        return arr


sl = Solution()

res = sl.solveNQueens(4)

pprint.pprint(res)

