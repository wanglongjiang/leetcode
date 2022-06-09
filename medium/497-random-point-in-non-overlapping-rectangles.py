'''
497. 非重叠矩形中的随机点
给定一个由非重叠的轴对齐矩形的数组 rects ，其中 rects[i] = [ai, bi, xi, yi] 表示 (ai, bi) 是第 i 个矩形的左下角点，(xi, yi) 是第 i 个矩形的右上角角点。
设计一个算法来随机挑选一个被某一矩形覆盖的整数点。矩形周长上的点也算做是被矩形覆盖。所有满足要求的点必须等概率被返回。

在一个给定的矩形覆盖的空间内任何整数点都有可能被返回。

请注意 ，整数点是具有整数坐标的点。

实现 Solution 类:

Solution(int[][] rects) 用给定的矩形数组 rects 初始化对象。
int[] pick() 返回一个随机的整数点 [u, v] 在给定的矩形所覆盖的空间内。
 

示例 1：



输入: 
["Solution","pick","pick","pick","pick","pick"]
[[[[-2,-2,-1,-1],[1,0,3,0]]],[],[],[],[],[]]
输出: 
[null,[-1,-2],[2,0],[-2,-1],[3,0],[-2,-2]

解释：
Solution solution = new Solution([[-2, -2, 1, 1], [2, 2, 4, 6]]);
solution.pick(); // 返回 [1, -2]
solution.pick(); // 返回 [1, -1]
solution.pick(); // 返回 [-1, -2]
solution.pick(); // 返回 [-2, -2]
solution.pick(); // 返回 [0, 0]
 

提示：

1 <= rects.length <= 100
rects[i].length == 4
-109 <= ai < xi <= 109
-109 <= bi < yi <= 109
xi - ai <= 2000
yi - bi <= 2000
所有的矩形不重叠。
pick 最多被调用 104 次。
'''

import bisect
import random
from typing import List
'''
思路：随机化
将每个矩形的面积计算出一个数字，保存到前缀和数组里面
然后出个[1..所有面积和]的随机数，二分查找确定是哪个矩形，在矩形里面随机选择一点。

时间复杂度：O(logn)
'''


class Solution:
    def __init__(self, rects: List[List[int]]):
        self.recs = rects
        self.arr = [0]
        for x1, y1, x2, y2 in rects:
            self.arr.append(self.arr[-1] + (x2 - x1 + 1) * (y2 - y1 + 1))

    def pick(self) -> List[int]:
        w = random.randint(1, self.arr[-1])
        idx = bisect.bisect_left(self.arr, w) - 1
        x, y = self.recs[idx][2] - self.recs[idx][0], self.recs[idx][3] - self.recs[idx][1]
        return [self.recs[idx][0] + random.randint(0, x), self.recs[idx][1] + random.randint(0, y)]
