import collections
class Solution:
    def dfs(self, board:list, r:int, c:int, i:int, j:int, visit:dict, word:str, pos:int):
        if pos == len(word):
            return True
        # if i == r - 1 and j == c - 1:
        #     if pos < len(word) - 1:
        #         return False
        #     else:
        #         if word[-1] == board[-1][-1]:
        #             return True
        #         else:
        #             return False

        if board[i][j] != word[pos]:
            return False
        else:
            if pos == len(word) - 1:
                return True

        visit[(i,j)] = True

        direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        for di, dj in direction:
            next_i, next_j = i + di, j + dj
            if next_i >= 0 and next_i < r and next_j >= 0 and next_j < c and not visit[(next_i, next_j)]:
                visit[(next_i, next_j)] = True
                res = self.dfs(board, r, c, next_i, next_j, visit, word, pos + 1)
                if res:
                    visit[(next_i, next_j)] = False
                    return True

                visit[(next_i, next_j)] = False

        visit[(i, j)] = False
        return False

    def exist(self, board:list, word: str) -> bool:
        row = len(board)
        if not row:
            return False
        col = len(board[0])
        if not col:
            return False
        visited = collections.defaultdict(bool)

        for i in range(row):
            for j in range(col):
                # visited[(i, j)] = True
                ifexist = self.dfs(board, row, col, i, j, visited, word, 0)
                if ifexist:
                    # visited[(i,j)] = False
                    return True
                # visited[(i, j)] = False

        return False



board =[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

# sl = Solution()
# word = "ABCCED"
# res = sl.exist(board, word)
# print(res)
# sl = Solution()
# word = "SEE"
# res = sl.exist(board, word)
# print(res)
#
# sl = Solution()
# word = "ABCB"
# res = sl.exist(board, word)
# print(res)
#
# sl = Solution()
# board = [["a","a"]]
# word = "aaa"
# res = sl.exist(board, word)
# print(res)

sl = Solution()
board = [["a"]]
word = "a"
res = sl.exist(board, word)
print(res)