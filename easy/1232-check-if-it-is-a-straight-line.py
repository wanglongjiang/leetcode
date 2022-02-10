'''
1232. 缀点成线
给定一个数组 coordinates ，其中 coordinates[i] = [x, y] ， [x, y] 表示横坐标为 x、纵坐标为 y 的点。
请你来判断，这些点是否在该坐标系中属于同一条直线上。

 

示例 1：



输入：coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
输出：true
示例 2：



输入：coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
输出：false
 

提示：

2 <= coordinates.length <= 1000
coordinates[i].length == 2
-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
coordinates 中不含重复的点
'''

from typing import List
'''
思路：数学
如果2个坐标处于同一直线，那么任意2个相邻坐标的tan相同

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        t = float('inf')
        if coordinates[1][0] - coordinates[0][0] != 0:
            t = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])
        for i in range(1, len(coordinates)):
            t2 = float('inf')
            if coordinates[i][0] - coordinates[i - 1][0] != 0:
                t2 = (coordinates[i][1] - coordinates[i - 1][1]) / (coordinates[i][0] - coordinates[i - 1][0])
            if t != t2:
                return False
        return True
