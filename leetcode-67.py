class Solution:
    def addBinary(self, a: str, b: str) -> str:
        na = len(a)
        nb = len(b)
        arr1 = list(map(int, a))
        arr2 = list(map(int, b))

        res = []
        ia = na - 1
        ib = nb - 1
        c = 0
        while ia >= 0 and ib >= 0:
            sum = arr1[ia] + arr2[ib] + c
            if sum >= 2:
                c = 1
                sum = sum % 2
            else:
                c = 0
            res.append(str(sum))
            ia -= 1
            ib -= 1

        if ia < 0 and ib < 0:
            if c:
                res.append(str(c))
        elif ia < 0:
            while ib >= 0:
                sum = arr2[ib] + c
                if sum >= 2:
                    sum = sum % 2
                    c = 1

                else:
                    c = 0
                res.append(str(sum))
                ib -= 1

            if c:
                res.append(str(c))
        else:
            while ia >= 0:
                sum = arr1[ia] + c
                if sum >= 2:
                    sum = sum % 2
                    c = 1

                else:
                    c = 0
                res.append(str(sum))
                ia -= 1

            if c:
                res.append(str(c))

        return "".join(list(reversed(res)))


sl = Solution()

a = "11"
b = "1"
res = sl.addBinary(a,b)
print(res)

a = "1010"
b = "1011"

res = sl.addBinary(a,b)
print(res)

a = "100"
b = "110010"
res = sl.addBinary(a, b)
print(res)