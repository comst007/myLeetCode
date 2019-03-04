import pprint
class Solution:
    def uniqueKey(self, val:str):
        dict_ch = {}
        for x in val:
            cnt = dict_ch.setdefault(x, 0)
            cnt += 1
            dict_ch[x] = cnt
        res = ""
        for x in "abcdefghijklmnopqrstuvwxyz":
            if x in dict_ch:
                arr_x = x * dict_ch[x]
                res = res + arr_x

        return res

    def groupAnagrams(self, strs: list):
        dict_res = {}

        for x in strs:
            key_x = self.uniqueKey(x)
            arr_val = dict_res.setdefault(key_x, [])
            arr_val.append(x)

        arr_res = []
        for k in dict_res:
            arr_res.append(dict_res[k])

        return arr_res




sl = Solution()
p = ["eat", "tea", "tan", "ate", "nat", "bat"]

res = sl.groupAnagrams(p)

pprint.pprint(res)
