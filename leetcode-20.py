class Solution:
    def counter_part(self, ch):
        if ch == "}":
            return "{"
        if ch == "]":
            return "["
        if ch == ")":
            return "("

    def isValid(self, s: str):
        if not s:
            return True
        st = []
        for x in s:
            if x == "{" or x == "(" or x == "[":
                st.append(x)
            elif x == "}" or x == ")" or x == "]":
                if not len(st):
                    return False
                else:
                    y = self.counter_part(x)
                    top = st.pop()
                    if top != y:
                        return False
                    else:

                        continue

        if len(st):
            return False

        return True




sl = Solution()

t1 = "()"
t2 = "()[]{}"
t3 = "(]"
t4 = "([)]"
t5 = "{[]}"

print(sl.isValid(t1))
print(sl.isValid(t2))
print(sl.isValid(t3))
print(sl.isValid(t4))
print(sl.isValid(t5))
