class Solution:
    def __init__(self):
        self.step = {}
        self.sove = {}
    def dfs(self, grid:list,m:int, n:int, cur_row:int, cur_col:int, solve_dict:dict):
        if (cur_row, cur_col) in solve_dict:
            return solve_dict[(cur_row, cur_col)]
        if cur_row == m - 1 and cur_col == n - 1:
            return grid[-1][-1]
        right_min = None
        down_min = None
        next_row = 0
        next_col = 0
        cur_min = grid[cur_row][cur_col]
        if cur_row + 1 < m:
            if (cur_row + 1, cur_col) in solve_dict:
                down_min = solve_dict[(cur_row + 1, cur_col)]
            else:
                down_min = self.dfs(grid, m, n, cur_row + 1, cur_col, solve_dict)


        if cur_col + 1 < n:
            if (cur_row, cur_col + 1) in solve_dict:
                right_min = solve_dict[(cur_row, cur_col + 1)]
            else:
                right_min = self.dfs(grid, m, n, cur_row, cur_col + 1, solve_dict)


        if  right_min is None:
            cur_min += down_min
            next_row = cur_row + 1
            next_col = cur_col
        elif  down_min is None:
            cur_min += right_min
            next_row = cur_row
            next_col = cur_col + 1
        else:
            if right_min < down_min:
                cur_min += right_min
                next_row = cur_row
                next_col = cur_col + 1
            else:
                cur_min += down_min
                next_row = cur_row + 1
                next_col = cur_col

        solve_dict[(cur_row, cur_col)] = cur_min
        self.step[(cur_row, cur_col)] = (next_row, next_col)
        return cur_min

    def show_step(self):

        start = (0, 0)

        while self.step[start] is not None:
            print("-->", start)
            start = self.step[start]

    def minPathSum(self, grid:list) -> int:
        m = len(grid)
        if not m:
            return 0
        n = len(grid[0])
        if not n:
            return 0
        if m == 1 and n == 1:
            return grid[0][0]

        solve_dict = {(m - 1, n - 1): grid[m - 1][n - 1]}
        self.step[(m - 1, n - 1)] = None
        res1 = self.dfs(grid, m, n, 0, 0, solve_dict)
        self.sove = solve_dict
        return res1

sl = Solution()

# t1 = [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
#
# res = sl.minPathSum(t1)
# for x in t1:
#     print(x)
# print(res)
# sl.show_step()

t2 = [[0,0],[0,0]]
sl = Solution()
res = sl.minPathSum(t2)
print(res)