class Solution:
    def __init__(self):
        codes = {}
        self.codes = codes
        codes["2"] = ["a", "b", "c"]
        codes["3"] = ["d", "e", "f"]
        codes["4"] = ["g", "h", "i"]
        codes["5"] = ["j", "k", "l"]
        codes["6"] = ["m", "n", "o"]
        codes["7"] = ["p", "q", "r", "s"]
        codes["8"] = ["t", "u", "v"]
        codes["9"] = ["w", "x", "y", "z"]

    def letterCombinations(self, digits: str):
        if not digits:
            return [""]
        ch = digits[0]
        code_arr = self.codes[ch]
        res = self.letterCombinations(digits[1:])
        output = []
        for x in code_arr:
            for substr in res:
                output.append(x + substr)

        return output

obj = Solution()

res = obj.letterCombinations("23")

print(res)
