'''
拼车
假设你是一位顺风车司机，车上最初有 capacity 个空座位可以用来载客。由于道路的限制，车 只能 向一个方向行驶
（也就是说，不允许掉头或改变方向，你可以将其想象为一个向量）。

这儿有一份乘客行程计划表 trips[][]，其中 trips[i] = [num_passengers, start_location, end_location] 包含了第 i 组乘客的行程信息：

必须接送的乘客数量；
乘客的上车地点；
以及乘客的下车地点。
这些给出的地点位置是从你的 初始 出发位置向前行驶到这些地点所需的距离（它们一定在你的行驶方向上）。

请你根据给出的行程计划表和车子的座位数，来判断你的车是否可以顺利完成接送所有乘客的任务
（当且仅当你可以在所有给定的行程中接送所有乘客时，返回 true，否则请返回 false）。

你可以假设乘客会自觉遵守 “先下后上” 的良好素质
trips.length <= 1000
trips[i].length == 3
1 <= trips[i][0] <= 100
0 <= trips[i][1] < trips[i][2] <= 1000
1 <= capacity <= 100000
'''
from typing import List
'''
思路：计数。
因为出发、下车站点索引<=1000，可以设置1个数组，
第1次遍历每个元素设置当前站点上、下车人数
第2次遍历将nums[i]设置为nums[i]+nums[i-1]-down[i]，如果某一元素>capacity，说明超载了
到了最后一个站点，如果没有超载说明可以成功
时间复杂度：O(n)，2次遍历数组
空间复杂度：O(n)
'''


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        up, down = [0] * 1001, [0] * 1001
        # 计算每个站点上下车人数
        for trip in trips:
            up[trip[1]] += trip[0]  # 上车人数
            if up[trip[1]] > capacity:  # 上车人数超过了容量，直接返回false
                return False
            down[trip[2]] = trip[0]  # 下车人数
        # 累计计算每个站点车上的人数
        for i in range(1, len(down)):
            up[i] += up[i - 1] - down[i]
            if up[i] > capacity:
                return False
        return True


s = Solution()
print(s.carPooling(trips=[[2, 1, 5], [3, 3, 7]], capacity=4))
print(s.carPooling(trips=[[2, 1, 5], [3, 3, 7]], capacity=5))
print(s.carPooling(trips=[[2, 1, 5], [3, 5, 7]], capacity=3))
print(s.carPooling(trips=[[3, 2, 7], [3, 7, 9], [8, 3, 9]], capacity=11))
