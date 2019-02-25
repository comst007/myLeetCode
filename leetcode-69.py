class Solution:
    def mySqrt(self, x: int):
        if  x == 0:
            return 0
        if x == 1:
            return 1
        cur = 1
        while True:
            if cur * cur > x :
                return cur - 1
            if cur * cur == x :
                return cur
            cur = cur + 1
