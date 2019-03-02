class Solution:
    def findJudge(self, N: int, trust: list[list[int]]):
        if N == 0:
            return -1
        if N == 1:
            return 1
        dict_in = {}
        dict_out = {}
        for x in trust:
            cnt_out = dict_out.setdefault(x[0], 0)
            cnt_out += 1
            dict_out[x[0]] = cnt_out

            cnt_in = dict_in.setdefault(x[1], 0)
            cnt_in += 1
            dict_in[x[1]] = cnt_in

        for key, cnt  in dict_in.items():
            if cnt == N - 1 and key not in dict_out:
                return key

        return -1

