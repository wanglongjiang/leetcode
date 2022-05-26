'''
掉落的方块
在无限长的数轴（即 x 轴）上，我们根据给定的顺序放置对应的正方形方块。

第 i 个掉落的方块（positions[i] = (left, side_length)）是正方形，其中 left 表示该方块最左边的点位置(positions[i][0])，side_length 表示该方块的边长(positions[i][1])。

每个方块的底部边缘平行于数轴（即 x 轴），并且从一个比目前所有的落地方块更高的高度掉落而下。在上一个方块结束掉落，并保持静止后，才开始掉落新方块。

方块的底边具有非常大的粘性，并将保持固定在它们所接触的任何长度表面上（无论是数轴还是其他方块）。邻接掉落的边不会过早地粘合在一起，因为只有底边才具有粘性。

 

返回一个堆叠高度列表 ans 。每一个堆叠高度 ans[i] 表示在通过 positions[0], positions[1], ..., positions[i] 表示的方块掉落结束后，目前所有已经落稳的方块堆叠的最高高度。

 

 

示例 1:

输入: [[1, 2], [2, 3], [6, 1]]
输出: [2, 5, 5]
解释:

第一个方块 positions[0] = [1, 2] 掉落：
_aa
_aa
-------
方块最大高度为 2 。

第二个方块 positions[1] = [2, 3] 掉落：
__aaa
__aaa
__aaa
_aa__
_aa__
--------------
方块最大高度为5。
大的方块保持在较小的方块的顶部，不论它的重心在哪里，因为方块的底部边缘有非常大的粘性。

第三个方块 positions[1] = [6, 1] 掉落：
__aaa
__aaa
__aaa
_aa
_aa___a
--------------
方块最大高度为5。

因此，我们返回结果[2, 5, 5]。
 

示例 2:

输入: [[100, 100], [200, 100]]
输出: [100, 100]
解释: 相邻的方块不会过早地卡住，只有它们的底部边缘才能粘在表面上。
 

注意:

1 <= positions.length <= 1000.
1 <= positions[i][0] <= 10^8.
1 <= positions[i][1] <= 10^6.
'''
from bisect import bisect_left, bisect_right
import sys
from typing import List
from sortedcontainers import SortedList
'''
思路：有序集合
设有序集合treeList，
遍历positions中的每个元素p[i]，
> 如果p[i]没有与其他方块相交，则在treeList中添加一个3元数组[left,right,height]，代表着左右边界和高度
> 如果p[i]的边界与其方块相交，则
>> 将右边相交的方块右边界改成p[i]的左边界-1，
>> 左边相交的方块左边界变成p[i]的右边界+1，
>> 完全被p[i]覆盖的模块删掉，将p[i]加入treeList，其高度为与p[i]相交的方块中最高的。
经过上面的操作后，地面上只会保留一层区间，不会有多层区间。

时间复杂度：O(nlogn)
空间复杂度：O(n)
'''


class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        ps, hs, res, maxtop = [-sys.maxsize, sys.maxsize], [0], [], 0
        for l, h in positions:
            r = l + h
            li, ri = bisect_right(ps, l), bisect_left(ps, r)
            top = (max(hs[li - 1:ri]) if li < ri else hs[li - 1]) + h
            ps = ps[:li] + [l, r] + ps[ri:]
            hs = hs[:li] + [top] + hs[ri - 1:]
            maxtop = max(maxtop, top)
            res.append(maxtop)
        return res


s = Solution()
print(s.fallingSquares([[1, 2], [1, 3]]))
print(s.fallingSquares([[1, 2], [2, 3], [6, 1]]))
print(s.fallingSquares([[100, 100], [200, 100]]))
