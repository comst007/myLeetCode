class Solution:
    def simplifyPath(self, path: str) -> str:

        path = path.strip()
        path.rstrip('/')
        n = len(path)
        if not n:
            return ""
        arr = path.split("/")
        arr = [x for x in arr if len(x) > 0]

        st = []
        for x in arr:
            if x == ".":
                continue
            elif x == "..":
                if len(st):
                    st.pop()
            else:
                st.append(x)

        res = '/'.join(st)
        return '/' + res

sl = Solution()

t1 = "/home/"
res = sl.simplifyPath(t1)
print(res)

t1 = "/../"
res = sl.simplifyPath(t1)
print(res)

t1 = "/home//foo/"
res = sl.simplifyPath(t1)
print(res)

t1 = "/a/./b/../../c/"
res = sl.simplifyPath(t1)
print(res)


t1 = "/a/../../b/../c//.//"
res = sl.simplifyPath(t1)
print(res)


t1 = "/a//b////c/d//././/.."
res = sl.simplifyPath(t1)
print(res)