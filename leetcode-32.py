class Solution:
    def longestValidParentheses(self, s: str):
        if not len(s):
            return 0
        max = 0
        cur = 0
        st = []
        last = -1
        for pos, ch in enumerate(s):
            if ch == '(':
                st.append(pos)
            else:
                if len(st):
                    st.pop()
                    if len(st):
                        cur = pos - st[-1]
                    else:
                        cur = pos - last
                    if cur > max:
                        max = cur

                else:
                    last = pos

        return max


l1 = "(()"
l2 = ")()())"
l3 = "()()(()"
sl = Solution()
res1 = sl.longestValidParentheses(l1)
print(res1)
res2 = sl.longestValidParentheses(l2)
print(res2)

res3 = sl.longestValidParentheses(l3)
print(res3)