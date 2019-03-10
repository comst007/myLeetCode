
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def insert(self, intervals: list, newInterval:Interval):
        n = len(intervals)
        if not n:
            return [newInterval]
        if newInterval.start > intervals[-1].end:
            intervals.append(newInterval)
            return intervals
        if newInterval.start >= intervals[-1].start:
            lastInternal = intervals.pop()
            mergedInternal = [min(lastInternal.start, newInterval.start), max(lastInternal.end, newInterval.end)]
            mergedInternal = Interval(*mergedInternal)
            intervals.append(mergedInternal)
            return intervals
        if newInterval.end < intervals[0].start:
            return [newInterval] + intervals
        if newInterval.end <= intervals[0].end:
            firstInternal = intervals.pop(0)
            mergedInternal = [min(newInterval.start, firstInternal.start), max(newInterval.end, firstInternal.end)]
            mergedInternal = Interval(*mergedInternal)
            return [mergedInternal] + intervals



        target_start = 0
        target_end = 0

        start_in = False
        end_in = False

        start = 0
        end = n - 1
        mid = 0
        while start <= end:
            mid = (start + end) // 2
            mid_start, mid_end = intervals[mid].start, intervals[mid].end
            if newInterval.start >= mid_start and newInterval.start <= mid_end:
                target_start = mid
                start_in = True
                break
            elif newInterval.start > mid_end:
                start = mid + 1
            else:
                end = mid - 1

        if start > end:
            target_start = start
            start_in = False
            start -= start

        end = n - 1

        while start <= end:
            mid = (start + end) // 2
            mid_start, mid_end = intervals[mid].start, intervals[mid].end
            if newInterval.end >= mid_start and newInterval.end <= mid_end:
                target_end = mid
                end_in = True
                break
            elif newInterval.end > mid_end:
                start = mid + 1
            else:
                end = mid - 1
        if start > end:
            target_end = start
            end_in = False

        left_part = intervals[:target_start]
        right_part = intervals[target_end + 1:]
        mid_part = intervals[target_start:target_end + 1]



        if start_in and end_in:
            mergedInternal = [intervals[target_start].start, intervals[target_end].end]
            mergedInternal = Interval(*mergedInternal)
            return left_part + [mergedInternal] + right_part
        elif not start_in and end_in:
            mergedInternal = [newInterval.start, intervals[target_end].end]
            mergedInternal = Interval(*mergedInternal)
            return left_part + [mergedInternal] + right_part
        elif start_in and not end_in:
            mergedInternal = [min(intervals[target_start].start, newInterval.start), newInterval.end]
            mergedInternal = Interval(*mergedInternal)
            if target_end >= n:
                return left_part + [mergedInternal] + right_part
            else:
                return left_part + [mergedInternal, intervals[target_end]] + right_part
        else:
            mergedInternal = newInterval
            if target_end < n:

                return left_part + [mergedInternal, intervals[target_end]] + right_part
            else:
                return left_part + [mergedInternal] + right_part



# sl = Solution()
# t1 = [[1,3],[6,9]]
# p1 = [2,5]
#
# t1 = [Interval(*x) for x in t1]
# p1 = Interval(*p1)
# res = sl.insert(t1,p1)
# print(res)
#
# sl = Solution()
# t1 = [[1,2],[3,5],[6,7],[8,10],[12,16]]
# p1 = [4,8]
#
# t1 = [Interval(*x) for x in t1]
# p1 = Interval(*p1)
#
# res = sl.insert(t1,p1)
# print(res)


# sl = Solution()
# t1 = [[1,5]]
# p1 = [0,6]
#
# t1 = [Interval(*x) for x in t1]
# p1 = Interval(*p1)
#
# res = sl.insert(t1,p1)
# print(res)

# sl = Solution()
# t1 = [[1,3],[6,9]]
# p1 = [2,5]
#
# t1 = [Interval(*x) for x in t1]
# p1 = Interval(*p1)
#
# res = sl.insert(t1,p1)
# print(res)

sl = Solution()
t1 = [[0,5],[8,9]]
p1 = [3,4]

t1 = [Interval(*x) for x in t1]
p1 = Interval(*p1)

res = sl.insert(t1,p1)
print(res)


