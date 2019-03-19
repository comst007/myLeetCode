class Solution:
    def generate(self, numRows: int) -> list:
        if not numRows:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]

        res = [[1],[1,1]]
        for i in range(3, numRows + 1):
            new_arr = [1] * i
            for j in range(1, i - 1):
                new_arr[j] = res[-1][j] + res[-1][j - 1]
            res.append(new_arr)

        return res
