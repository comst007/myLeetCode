class Solution:
    def dfs(self, arr:list,start:int, res_sub:list, res:list, sum:int):

        n = len(arr)
        if not n:
            return
        if n - start == 1:
            if arr[start] == sum:
                res_sub.append(arr[start])
                res.append(res_sub[:])
                res_sub.pop()
                return
            else:
                return
        last_i = -1
        for i in range(start, n):
            if last_i == -1 or arr[i] != arr[last_i]:
                last_i = i
                if arr[i] < sum:
                    res_sub.append(arr[i])


                    self.dfs(arr, i + 1, res_sub,res, sum - arr[i])
                    res_sub.pop()
                elif arr[i] == sum:
                    res_sub.append(arr[i])
                    res.append(res_sub[:])
                    res_sub.pop()
                else:
                    continue


    def combinationSum2(self, candidates: list, target: int):
        if not candidates:
            return []
        candidates_sort = sorted(candidates)
        res = []
        self.dfs(candidates_sort,0, [], res, target)
        return res
        pass


sl = Solution()
candidates1 = [10, 1, 2, 7, 6, 1, 5]
target1 = 8

res = sl.combinationSum2(candidates1, target1)
print(res)


candidates2 = [2, 5, 2, 1, 2]
target2 = 5
res2 = sl.combinationSum2(candidates2, target2)
print(res2)
