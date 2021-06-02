'''
车队
N  辆车沿着一条车道驶向位于 target 英里之外的共同目的地。

每辆车 i 以恒定的速度 speed[i] （英里/小时），从初始位置 position[i] （英里） 沿车道驶向目的地。

一辆车永远不会超过前面的另一辆车，但它可以追上去，并与前车以相同的速度紧接着行驶。

此时，我们会忽略这两辆车之间的距离，也就是说，它们被假定处于相同的位置。

车队 是一些由行驶在相同位置、具有相同速度的车组成的非空集合。注意，一辆车也可以是一个车队。

即便一辆车在目的地才赶上了一个车队，它们仍然会被视作是同一个车队。

 

会有多少车队到达目的地?

 

示例：

输入：target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
输出：3
解释：
从 10 和 8 开始的车会组成一个车队，它们在 12 处相遇。
从 0 处开始的车无法追上其它车，所以它自己就是一个车队。
从 5 和 3 开始的车会组成一个车队，它们在 6 处相遇。
请注意，在到达目的地之前没有其它车会遇到这些车队，所以答案是 3。

提示：

0 <= N <= 10 ^ 4
0 < target <= 10 ^ 6
0 < speed[i] <= 10 ^ 6
0 <= position[i] < target
所有车的初始位置各不相同。
'''
from typing import List
'''
思路：排序
把车辆按照位置进行排序，然后从距离最近的车辆开始计算理想情况下到达终点时间time=(target-position)/speed，
如果后面的到达时间小于等于前面的车的到达时间，这辆车可以与前面的车合并成同一个车队
如果大于前面的车的到达之间，则这辆车会构成新的车队，在这辆车后面的车再快也不会超过这辆车

时间复杂度：O(nlogn)
空间复杂度：O(n)
'''


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 按照距离终点位置排序，计算出各车如果独自行动的到达时间
        distance = map(lambda item: target - item, position)
        arrivalTimes = list(map(lambda item: item[0] / item[1], sorted(zip(distance, speed), key=lambda item: item[0])))
        ans, time = 0, 0
        for arrivalTime in arrivalTimes:
            if arrivalTime > time:  # 当前车辆无法追上前面的车，车队数+1
                ans += 1
                time = arrivalTime
        return ans


s = Solution()
print(s.carFleet(target=12, position=[10, 8, 0, 5, 3], speed=[2, 4, 1, 1, 3]))
print(s.carFleet(target=12, position=[], speed=[]))
