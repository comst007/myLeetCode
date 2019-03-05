import pprint
class Interval:
     def __init__(self, s=0, e=0):
         self.start = s
         self.end = e

class Solution:
    def merge(self, intervals: list):
        res = []
        n = len(intervals)
        if not n:
            return []
        if n == 1:
            return intervals
        intervals.sort(key = lambda x: x.start)
        cur_inerval = intervals[0]
        for i in range(1, n):
            if cur_inerval.end < intervals[i].start:
                res.append(cur_inerval)
                cur_inerval = intervals[i]
            else:
                s = min(cur_inerval.start, intervals[i].start)
                e = max(cur_inerval.end, intervals[i].end)
                cur_inerval = Interval(s, e)
        res.append(cur_inerval)
        return res


sl = Solution()

t1 = [[1,3],[2,6],[8,10],[15,18]]
t1 = [Interval(*x) for x in t1]

res = sl.merge(t1)
pprint.pprint(res)

sl = Solution()
t2 = [[1,4],[4,5]]
t2 = [Interval(*x) for x in t2]
res = sl.merge(t2)

print(res)
