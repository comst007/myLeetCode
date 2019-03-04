import pprint

class Solution:
    def __init__(self):
        self.depth = 0

    def dfs(self, board:list, cnt_row:int, cnt_col:int, r_dict:dict, c_dict:dict, s_dict:dict, start:int, cnt_dot:int):
        if cnt_dot == 0:
            return True
        # if start >= 60:
        #     return True
        print("--->", start)
        for k in range(start, cnt_row * cnt_col):
            cur_row = k // cnt_row
            cur_col = k % cnt_row
            if board[cur_row][cur_col] != '.':
                continue
            row_set = r_dict[cur_row]
            col_set = c_dict[cur_col]
            square_set = s_dict[(cur_row // 3) * 3 + cur_col // 3]

            for num in "123456789":
                if (num in row_set) or (num in col_set) or (num in square_set):
                    continue
                row_set.add(num)
                col_set.add(num)
                square_set.add(num)
                board[cur_row][cur_col] = num


                if self.dfs(board,cnt_row,cnt_col,r_dict,c_dict,s_dict,k + 1, cnt_dot - 1):
                    return True

                row_set.remove(num)
                col_set.remove(num)
                square_set.remove(num)
                board[cur_row][cur_col] = '.'
            return False

        return False
    def solveSudoku(self, board:list):
        row_dict = {}
        col_dict = {}
        cell_dict = {}

        row = len(board)
        col = len(board[0])
        cnt_d = 0
        for r in range(row):
            for c in range(col):
                r_set = row_dict.setdefault(r, set())
                c_set = col_dict.setdefault(c, set())
                cell_index = (r // 3) * 3 + c // 3
                cell_set = cell_dict.setdefault(cell_index, set())
                if board[r][c] == '.':
                    cnt_d += 1
                    continue


                r_set.add(board[r][c])


                c_set.add(board[r][c])




                cell_set.add(board[r][c])

        self.dfs(board, row, col, row_dict ,col_dict, cell_dict, 0, cnt_d)

sl = Solution()


s = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

s2 = [
      [".",".","9","7","4","8",".",".","."],
      ["7",".",".",".",".",".",".",".","."],
      [".","2",".","1",".","9",".",".","."],
      [".",".","7",".",".",".","2","4","."],
      [".","6","4",".","1",".","5","9","."],
      [".","9","8",".",".",".","3",".","."],
      [".",".",".","8",".","3",".","2","."],
      [".",".",".",".",".",".",".",".","6"],
      [".",".",".","2","7","5","9",".","."]
]

s3 = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
sl.solveSudoku(s3)

pprint.pprint(s3)
