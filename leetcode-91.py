class Solution:
    def dfs(self, s:str, n:int, pos:int, visit:dict):
        if pos >= n:
            return 1
        if pos in visit:
            return visit[pos]
        if pos == n - 1:
            if s[-1] == '0':
                visit[pos] = 0
                return 0
            else:
                visit[pos] = 1
                return 1

        if s[pos] == "0":
            visit[pos] = 0
            return 0
        total = 0
        if int(s[pos]) > 2:
            total = self.dfs(s,n,pos + 1, visit)
            visit[pos] = total
            return total
        else:
            if s[pos + 1] == '0':
                total = self.dfs(s,n,pos + 2, visit)
                visit[pos] = total
                return total
            elif s[pos] == '2' and int(s[pos + 1]) > 6:
                total = self.dfs(s,n,pos + 1, visit)
                visit[pos] = total
                return total
            else:
                total = self.dfs(s,n,pos + 1, visit)
                total += self.dfs(s,n,pos + 2, visit)
                visit[pos] = total
                return total

    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 1:
            if s[0] == '0':
                return 0
            else:
                return 1
        if s[0] == '0':
            return 0
        res = self.dfs(s,n,0,{})
        return res

# sl = Solution()
# t1 = "12"
# res = sl.numDecodings(t1)
# print(res)
#
# sl = Solution()
# t1 = "226"
# res = sl.numDecodings(t1)
# print(res)
#
# sl = Solution()
# t1 = "00"
# res = sl.numDecodings(t1)
# print(res)

# sl = Solution()
# t1 = "100"
# res = sl.numDecodings(t1)
# print(res)

sl = Solution()
t1 = "17"
res = sl.numDecodings(t1)
print(res)