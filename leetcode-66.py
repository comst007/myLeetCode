class Solution:
    def plusOne(self, digits:list):
        res = []
        sum = 0
        c = 1
        for x in reversed(digits):
            sum = x + c
            if sum < 10:
                res.append(sum)
                c = 0
            else:
                res.append(sum % 10)
                c = sum // 10

        if c:
            res.append(c)

        return list(reversed(res))

sl = Solution()

t1 = [1,2,3]
res = sl.plusOne(t1)
print(res)

t2 = [4,3,2,1]
res = sl.plusOne(t2)
print(res)