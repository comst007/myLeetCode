class Solution:
    def __init__(self):
        self.cnt = 0
    def ifTrue(self, arr):
        delt_01_x = arr[1][0] - arr[0][0]
        delt_01_y = arr[1][1] - arr[0][1]
        dist01 = delt_01_x * delt_01_x + delt_01_y * delt_01_y

        delt_02_x = arr[2][0] - arr[0][0]
        delt_02_y = arr[2][1] - arr[0][1]

        dist02 = delt_02_x * delt_02_x + delt_02_y * delt_02_y

        if dist01 == dist02:
            return True
        else:
            return False
    def distance(self, point1, point2):
        delt_x = point1[0] - point2[0]
        delt_y = point1[1] - point2[1]
        dist01 = delt_x * delt_x + delt_y * delt_y
        return dist01
    def select_k(self, points:list, res:list, k:int):
        if k == 0:
            if self.ifTrue(res):
                self.cnt += 1


        cnt_p = len(points)
        if cnt_p < k:
            return
        for i in range(cnt_p):
            res.append(points[i])
            sub_arr = points[:]
            sub_arr.pop(i)
            self.select_k(sub_arr, res, k - 1)
            res.pop()
    def select_k_v2(self, points):
        cnt_p = len(points)
        if cnt_p < 3:
            self.cnt = 0
            return
        for i in range(cnt_p):
            dict_dist = {}
            for j in range(cnt_p):
                if i == j:
                    continue
                key_dist = self.distance(points[i], points[j])

                val_cnt = dict_dist.setdefault(key_dist, 0)
                dict_dist[key_dist ] = val_cnt + 1

            for k, v in dict_dist.items():
                if v >= 2:
                    self.cnt += v * (v - 1)


    def numberOfBoomerangs(self, points):
        self.cnt = 0
        self.select_k_v2(points)
        return self.cnt




l1 = [[0,0],[1,0],[2,0]]

l2 = [[5,0],[4,8],[7,1],[7,2],[2,6],[1,0],[6,1],[5,9],[4,9]]

sl = Solution()

res = sl.numberOfBoomerangs(l1)

res2 = sl.numberOfBoomerangs(l2)

print(res2)