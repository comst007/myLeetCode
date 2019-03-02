class Solution:
    def firstMissingPositive(self, nums: list) -> int:
        cnt = len(nums)
        if not cnt:
            return 0
        dict_visit = {}
        for x in nums:
            if x > 0 and x <= cnt:
                dict_visit.setdefault(x, 1)

        for x in range(1, cnt + 1):
            if x not in dict_visit:
                return x

        return cnt + 1