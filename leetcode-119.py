class Solution:
    def generate(self, numRows: int) -> list:
        if not numRows:
            return [1]
        if numRows == 1:
            return [1,1]
        

        last = [1,1]
        for i in range(3, numRows + 1):
            new_arr = [1] * i
            for j in range(1, i - 1):
                new_arr[j] = last[j] + last[j - 1]
            last = new_arr

        return last

sl = Solution()

res = sl.generate(3)
print(res)
