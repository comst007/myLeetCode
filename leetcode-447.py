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

    def numberOfBoomerangs(self, points):
        self.cnt = 0
        self.select_k(points, [], 3)
        return self.cnt




l1 = [[0,0],[1,0],[2,0]]

l2 = [[5,0],[4,8],[7,1],[7,2],[2,6],[1,0],[6,1],[5,9],[4,9]]

sl = Solution()

res = sl.numberOfBoomerangs(l1)

res2 = sl.numberOfBoomerangs(l2)

print(res2)