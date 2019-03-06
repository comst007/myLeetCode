class Solution:
    def dfs(self,row_cnt:int, col_cnt:int, i:int, j:int, solve_dict:dict):

        if (i, j) in solve_dict:
            return solve_dict[(i,j)]
        right_cnt = 0
        down_cnt = 0
        #right
        if i + 1 < row_cnt:
            if (i + 1, j) in solve_dict:
                right_cnt = solve_dict[(i + 1, j)]
            else:
                right_cnt = self.dfs(row_cnt, col_cnt,i + 1, j,solve_dict)
        #left

        if j + 1 < col_cnt:
            if (i, j + 1) in solve_dict:
                down_cnt = solve_dict[(i, j + 1)]
            else:
                down_cnt = self.dfs(row_cnt, col_cnt, i, j + 1, solve_dict)

        res = right_cnt + down_cnt
        solve_dict[(i, j)] = res
        return res

    def uniquePaths(self, m: int, n: int):
        if not n or not m:
            return 0
        if n == 1:
            return 1
        if m == 1:
            return 1
        res = None
        res = self.dfs(m, n, 0, 0, {(m - 1, n - 1):1})
        return res

sl = Solution()

res = sl.uniquePaths(3, 2)
print(res)

sl = Solution()

res = sl.uniquePaths(7,3)

print(res)