
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)
        if not n:
            return ""
        if not m:
            return ""
        dic_t = {}
        t_kind = 0
        for i in range(m):
            cnt = dic_t.setdefault(t[i], 0)
            cnt += 1
            dic_t[t[i]] = cnt
        t_kind = len(dic_t.keys())
        cur_kind = 0
        dic_s = {}
        start = 0
        last_start = 0
        end = 0
        min_start = None
        min_end = None

        while start < n:
            if s[start] not in dic_t:
                start += 1
            else:
                cnt = dic_s.setdefault(s[start], 0)
                cnt += 1
                dic_s[s[start]] = cnt
                if cnt == dic_t[s[start]]:
                    cur_kind += 1
                    if cur_kind == t_kind:
                        end = start
                        if min_start is None:
                            min_start = last_start
                            min_end = end
                        while last_start <= start:
                            if s[last_start] not in dic_t:
                                last_start += 1
                            else:
                                if dic_s[s[last_start]] > dic_t[s[last_start]]:
                                    cnt = dic_s[s[last_start]]
                                    cnt -= 1
                                    dic_s[s[last_start]] = cnt
                                    last_start += 1
                                else:
                                    if end - last_start < min_end - min_start:
                                        min_start = last_start
                                        min_end = end
                                    cnt = dic_s[s[last_start]]
                                    cnt -= 1
                                    dic_s[s[last_start]] = cnt
                                    cur_kind -= 1
                                    last_start += 1
                                    start += 1
                                    break


                    else:
                        start += 1

                else:
                    start += 1

        if min_end is None:
            return ' '
        else:
            return s[min_start:min_end + 1]



sl = Solution()
S = "ADOBECODEBANC"
T = "ABC"
res = sl.minWindow(S, T)
print(res)