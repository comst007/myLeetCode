class Solution:
    def dfs(self,row_cnt:int, col_cnt:int, i:int, j:int, obs_arr:list, solve_dict:dict):

        if (i, j) in solve_dict:
            return solve_dict[(i,j)]
        right_cnt = 0
        down_cnt = 0
        #right
        if i + 1 < row_cnt and not obs_arr[i + 1][j]:
            if (i + 1, j) in solve_dict:
                right_cnt = solve_dict[(i + 1, j)]
            else:
                right_cnt = self.dfs(row_cnt, col_cnt,i + 1, j,obs_arr,solve_dict)
        #left

        if j + 1 < col_cnt and not obs_arr[i][j + 1]:
            if (i, j + 1) in solve_dict:
                down_cnt = solve_dict[(i, j + 1)]
            else:
                down_cnt = self.dfs(row_cnt, col_cnt, i, j + 1,obs_arr, solve_dict)

        res = right_cnt + down_cnt
        solve_dict[(i, j)] = res
        return res

    def uniquePathsWithObstacles(self, obstacleGrid: list) -> int:
        row = len(obstacleGrid)
        if not row:
            return 0
        col = len(obstacleGrid[0])
        if not col:
            return 0
        if obstacleGrid[row - 1][col - 1]:
            return 0
        if obstacleGrid[0][0]:
            return 0
        res = self.dfs(row,col,0,0,obstacleGrid, {(row-1, col - 1):1})

        return res

t1 = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]

sl = Solution()

res = sl.uniquePathsWithObstacles(t1)
print(res)