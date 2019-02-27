class Solution:
    def divide(self, dividend: int, divisor: int):
        if dividend == 0:
            return 0
        flag = 0
        if dividend > 0 and divisor > 0:
            flag = 1
        elif dividend > 0 and divisor < 0:
            flag = -1
        elif dividend < 0 and divisor > 0:
            flag = -1
        else:
            flag = 1
        left = abs(dividend)
        right = abs(divisor)

        if right == 1:
            if flag == 1:
                return min(2147483647, max(-2147483648, left))
            else:
                return min(2147483647, max(-2147483648, -left))

        cnt = 0
        tmp = 0
        times = 0
        while True:
            tmp = right
            times = 1
            while True:
                if left - tmp >= 0:
                    left = left - tmp
                    cnt += times
                    times += times
                    tmp += tmp
                else:
                    break
            if left < right:
                break



        if flag == -1:
            return min(2147483647, max(-2147483648, -cnt))
        else:
            return min(2147483647, max(-2147483648, cnt))






