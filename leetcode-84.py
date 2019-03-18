class Solution:
    def largestRectangleArea(self, heights: list) -> int:
        n = len(heights)
        if not n:
            return 0
        if n == 1:
            return heights[0]

        st = [[0]]
        n_st = 1
        maxArea = -1
        for i in range(1, n):
            if n_st == 0 or heights[i] > heights[st[-1][0]]:
                st.append([i])
                n_st += 1
            elif heights[i] == heights[st[-1][0]]:
                st[-1].append(i)
            else:
                while n_st > 0 and heights[st[-1][0]] > heights[i]:
                    top = st.pop()
                    n_st -= 1
                    if n_st > 0:
                        cur_area = heights[top[0]] * (i - 1 - (st[-1][-1] + 1) + 1)
                    else:
                        cur_area = heights[top[0]] * (i - 1 - 0 + 1)
                    maxArea = max(maxArea, cur_area)

                if n_st == 0:
                    st.append([i])
                    n_st += 1
                elif heights[i] == heights[st[-1][0]]:
                    st[-1].append(i)
                else:
                    st.append([i])
                    n_st += 1

        if n_st > 0:
            while n_st > 0:
                top = st.pop()
                n_st -= 1
                if n_st > 0:
                    cur_area = heights[top[0]] * (n - 1 - (st[-1][-1] + 1) + 1)
                else:
                    cur_area = heights[top[0]] * n
                maxArea = max(maxArea, cur_area)


        return maxArea


# sl = Solution()
# t = [2,1,5,6,2,3]
#
# res = sl.largestRectangleArea(t)
# print(res)

sl = Solution()
t = [2,4]

res = sl.largestRectangleArea(t)
print(res)