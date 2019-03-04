class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1 = len(num1)
        n2 = len(num2)
        if not n1 or not n2:
            return ""
        if n1 == 1 and num1[0] == '0':
            return "0"
        if n2 == 1 and num2[0] == '0':
            return "0"
        # arr_num1 = list(reversed(num1))
        arr_num1 = list(map(lambda x: ord(x) - ord('0'), num1))
        arr_num1 = list(reversed(arr_num1))
        # arr_num2 = list(reversed(num2))
        arr_num2 = list(map(lambda x: ord(x) - ord('0'), num2))
        arr_num2 = list(reversed(arr_num2))
        arr_res = [0] * (n1 + n2)

        i = 0
        j = 0
        c = 0
        res = ""
        PRIME = 10
        for j in range(n2):
            for i in range(n1):
                sum = arr_num1[i] * arr_num2[j] + arr_res[i + j]
                c = sum // PRIME
                arr_res[i + j] = sum % PRIME
                if c != 0:
                    arr_res[i + j + 1] += c

        res1 = map(lambda x: str(x), reversed(arr_res))

        flag = 0
        res_str = ""
        for ch in res1:
            if flag == 0:
                if ch != "0":
                    flag = 1
                    res_str = ch
            else:
               res_str = res_str + ch

        return res_str



sl = Solution()
num1 = "2"
num2 = "3"

res1 = sl.multiply(num1, num2)
print(res1)
num1 = "123"
num2 = "456"

res2 = sl.multiply(num1, num2)
print(res2)