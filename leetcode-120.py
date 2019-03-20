class Solution:
    def dfs(self, triangle:list, n:int, k:int, j:int, visit:dict):
        if k == n - 1:
            visit[(k, j)] = triangle[k][j]
            return visit[(k, j)]
        if (k, j) in visit:
            return visit[(k, j)]
        left_min = None
        right_min = None

        left_min = self.dfs(triangle, n, k + 1, j, visit)
        right_min = self.dfs(triangle, n, k + 1, j + 1, visit)

        res_min = min(left_min, right_min)

        visit[(k, j)] = res_min + triangle[k][j]

        return visit[(k,j)]
    def minimumTotal(self, triangle: list) -> int:
        n = len(triangle)
        if not n:
            return 0
        if n == 1:
            return max(triangle[0])
        dict_visit = {}
        res_min = self.dfs(triangle, n, 0, 0, dict_visit)
        return res_min



t1 = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

sl = Solution()

res = sl.minimumTotal(t1)
print(res)