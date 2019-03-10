class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1 = len(word1)
        l2 = len(word2)
        if not l1 and l2:
            return l2
        if l1 and not l2:
            return l1
        if not l1 and not l2:
            return 0
        res = [[0] * (l2 + 1) for _ in range(len(word1) + 1)]
        for i in range(1, l2 + 1):
            res[0][i] = i

        for i in range(1, l1 + 1):
            res[i][0] = i

        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    res[i][j] = res[i - 1][j - 1]
                else:
                    tmp_min = min(res[i - 1][j - 1], res[i - 1][j], res[i][j - 1])
                    res[i][j] = tmp_min + 1
        return res[-1][-1]


sl = Solution()
word1 = "horse"
word2 = "ros"

res = sl.minDistance(word1,word2)
print(res)

sl = Solution()
word1 = "intention"
word2 = "execution"

res = sl.minDistance(word1,word2)
print(res)



