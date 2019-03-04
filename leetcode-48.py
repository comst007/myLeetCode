import pprint
class Solution:
    def rotate(self, matrix:list) -> None:
        cnt_row = len(matrix)
        if not cnt_row:
            return
        cnt_col = len(matrix[0])
        if cnt_row != cnt_col:
            return
        if cnt_row == 1:
            return
        cnt_round = cnt_row // 2
        top_left = 0
        down_right = 0
        for round_index in range(cnt_round):
            top_left = round_index
            down_right = cnt_row - 1 - round_index
            for i in range(down_right - top_left):
                tmp = matrix[top_left][top_left + i]

                #left_down -> left_up
                matrix[top_left][top_left + i] = matrix[down_right - i][top_left]
                #right_down -> left_down
                matrix[down_right - i][top_left] = matrix[down_right][down_right - i]

                # right_top -> right_down
                matrix[down_right][down_right - i] = matrix[top_left + i][down_right]

                #left_top ->right_top
                matrix[top_left + i][down_right] = tmp









sl = Solution()

m1 = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
res1 = sl.rotate(m1)
pprint.pprint(m1)
m2 = [
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]

res2 = sl.rotate(m2)

pprint.pprint(m2)

