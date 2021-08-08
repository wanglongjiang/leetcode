'''
有效的回旋镖
回旋镖定义为一组三个点，这些点各不相同且不在一条直线上。

给出平面上三个点组成的列表，判断这些点是否可以构成回旋镖。

 

示例 1：

输入：[[1,1],[2,3],[3,2]]
输出：true
示例 2：

输入：[[1,1],[2,2],[3,3]]
输出：false
 

提示：

points.length == 3
points[i].length == 2
0 <= points[i][j] <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-boomerang
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
'''
思路：几何
对比任意2个点形成的线与水平线的角的tan，如果不相同，则能构成三角形


时间复杂度：O(1)
空间复杂度：O(1)
'''


class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        a1, b1 = points[0][0] - points[1][0], points[0][1] - points[1][1]
        a2, b2 = points[0][0] - points[2][0], points[0][1] - points[2][1]
        if b1 == 0 and b2 == 0:
            return False
        if b1 == 0 or b2 == 0:
            return True
        return a1 / b1 != a2 / b2
