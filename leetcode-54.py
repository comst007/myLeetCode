class Solution:
    def spiralOrder(self, matrix:list):
        row = len(matrix)
        if not row:
            return []
        col = len(matrix[0])

        res = []
        top = 0
        left = 0
        down = row - 1
        right = col - 1

        cur_i = 0
        cur_j = 0
        while left <= right and top <= down:
            cur_i = top
            cur_j = left
            #left ->right
            while cur_j <= right:
                res.append(matrix[top][cur_j])
                cur_j += 1


            #up -> down
            cur_i = top + 1
            while cur_i <= down:
                res.append(matrix[cur_i][right])
                cur_i += 1


            #right -> left
            cur_j  = right - 1

            while top != down and cur_j >= left:
                res.append(matrix[down][cur_j])
                cur_j -= 1


            #dow -> up
            cur_i = down - 1
            while left != right and cur_i > top:
                res.append(matrix[cur_i][left])
                cur_i -= 1

            top  += 1
            left += 1
            right -= 1
            down -= 1
        return res


sl = Solution()

t1 = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

res1 = sl.spiralOrder(t1)

t2 = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]

res2 = sl.spiralOrder(t2)

print(res2)
