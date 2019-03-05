import pprint
class Solution:
    def generateMatrix(self, n: int):
        if n == 0:
            return []
        if n == 1:
            return [[1]]

        mat = []
        for i in range(n):
            mat.append([0] * n)

        count = 1
        r = 0
        c = 0
        top_left = 0
        down_right = n - 1
        while count <= n * n:
            r = top_left
            c = top_left

            #left -> right
            while c <= down_right:
                mat[r][c] = count
                count += 1
                c += 1

            #up -> down
            c = down_right
            r = top_left + 1
            while r <= down_right:
                mat[r][c] = count
                count += 1
                r += 1


            #right ->left
            r = down_right
            c = down_right - 1
            while top_left != down_right and c >= top_left:
                mat[r][c] = count
                count += 1
                c -= 1

            #down ->up
            r = down_right - 1
            c = top_left
            while top_left != down_right and r >= top_left + 1:
                mat[r][c] = count
                count += 1
                r -= 1
            top_left  += 1
            down_right -= 1

        return mat


sl = Solution()

res = sl.generateMatrix(3)
pprint.pprint(res)

sl = Solution()

res = sl.generateMatrix(4)
print(res)