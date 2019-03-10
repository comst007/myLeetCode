class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        cnt_e = 0
        cnt_flag_e = 0
        cnt_dot = 0
        cnt_flag_begin = 0
        cnt_digit = 0

        n = len(s)
        if not n:
            return False
        for i in range(n):
            if s[i].isalpha() and s[i] != 'e':
                return False
            elif s[i] == '+' or s[i] == '-':
                if i == 0 and i + 1 < n and s[i + 1] != 'e':
                    cnt_flag_begin = 1
                else:
                    if s[i - 1] == 'e' and cnt_flag_e == 0 and i + 1 < n:
                        cnt_flag_e = 1
                    else:
                        return False
            elif s[i].isdigit():
                cnt_digit += 1
            elif s[i] == 'e':
                if cnt_e != 0 or i == n - 1 or i == 0:
                    return False
                else:
                    cnt_e += 1
            elif s[i] == '.':
                if cnt_dot or cnt_e:
                    return False
                else:
                    if i == n - 1 and cnt_digit == 0:
                        return False
                    if i == 0 and i + 1 < n and s[i + 1] == 'e':
                        return False
                    # elif i < n - 1 and not s[i + 1].isdigit():
                    #     return False

                    cnt_dot += 1
            else:
                return False

        return True

sl = Solution()
t1 = ["0","0.1","abc","1 a","2e10","-90e3","1e","e3","6e-1","99e2.5","53.5e93","--6","-+3","95a54e53", '.']
for x in t1:
    print(x, sl.isNumber(x))


