class Solution:
    def dfs(self, arr:list, start:int, res_sub:list, res:list, sum:int):

        n = len(arr)
        if not n:
            return
        for i in range(start, n):
            if arr[i] < sum:
                res_sub.append(arr[i])
                self.dfs(arr,i,res_sub,res, sum - arr[i])
                res_sub.pop()
            elif arr[i] == sum:
                res_sub.append(arr[i])
                res.append(res_sub[:])
                res_sub.pop()
            else:
                continue

    def combinationSum(self, candidates: list, target: int):
        if not candidates:
            return []

        res = []
        self.dfs(candidates,0, [], res, target)
        return res



sl = Solution()

candidates1 = [2, 3, 6, 7]
target1 = 7

res = sl.combinationSum(candidates1, target1)
print(res)

candidates2 = [2, 3, 5]
target2 = 8

res2 = sl.combinationSum(candidates2, target2)
print(res2)

