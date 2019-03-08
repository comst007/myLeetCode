class Solution:
    def dfs(self, s:str, n:int, pos:int, sub_res:list, total_res:list, left:int):
        if left == 0 and pos >= n:
            total_res.append(sub_res[:])
            return

        if left == 0 and pos < n:
            return
        if pos < n and s[pos] == '0':
            sub_res.append(s[pos])
            self.dfs(s,n,pos + 1, sub_res,total_res, left - 1)
            sub_res.pop()
            return

        for delt in range(3, 0, -1):
            if delt + pos > n:
                continue
            target = int(s[pos:delt + pos])
            if target > 255:
                continue
            sub_res.append(s[pos:delt + pos])
            self.dfs(s, n, pos + delt, sub_res, total_res, left - 1)
            sub_res.pop()

    def restoreIpAddresses(self, s: str):
        n = len(s)
        if n < 4:
            return []
        if n == 4:
            return [".".join(s)]
        res = []
        self.dfs(s, n, 0, [], res, 4)
        return [".".join(x) for x in res]


# sl = Solution()
# t1 = "25525511135"
# res = sl.restoreIpAddresses(t1)
# print(res)


sl = Solution()
t1 = "010010"
res = sl.restoreIpAddresses(t1)
print(res)

