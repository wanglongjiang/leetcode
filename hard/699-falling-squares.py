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
        treeList = SortedList(key=lambda r: r[0])
        ans = []
        maxHeight = 0
        for p in positions:
            bottomHeight = 0  # 与当前区间有交集的区间中最高高度
            left, right, height = p[0], p[0] + p[1] - 1, p[1]
            lefti = treeList.bisect_left([left, left])
            if lefti > 0:
                leftRange = treeList[lefti - 1]
                if leftRange[1] >= left and leftRange[1] <= right:  # 左边的区间与当前区间有交集，且其右边界没有超过当前区间的右边界
                    leftRange[1] = left - 1  # 裁剪左边区间的右边界
                    bottomHeight = leftRange[2]
                elif leftRange[1] > right:  # 左边的区间右边界已经超过了当前区间右边界，需要将左边的区间拆分成2部分，一部分在当前区间左边，另外一部分在右边
                    rightRange = [right + 1, leftRange[1], leftRange[2]]  # 在右边新添加一个区间
                    treeList.add(rightRange)
                    leftRange[1] = left - 1  # 裁剪原左边区间的右边界
                    bottomHeight = leftRange[2]
            righti = treeList.bisect_right([right, right])
            if righti - 1 > 0:
                rightRange = treeList[righti - 1]
                if rightRange[0] <= right <= rightRange[1] and rightRange[0] != rightRange[1]:  # 右边的区间与当前区间有交集，且右边区间没有完全被当前区间覆盖
                    rightRange[0] = right - 1  # 裁剪右边区间的左边界
                    bottomHeight = max(bottomHeight, rightRange[2])
                elif rightRange[0] <= right <= rightRange[1] and rightRange[0] == rightRange[1]:  # 右边的区间被当前区间完全覆盖，删除
                    del treeList[righti - 1]
                    bottomHeight = max(bottomHeight, rightRange[2])
            for i in range(lefti, righti - 1):  # 删除左右边界内的区间
                bottomHeight = max(bottomHeight, treeList[lefti][2])
                del treeList[lefti]
            treeList.add([left, right, height + bottomHeight])  # 当前方块加入集合
            maxHeight = max(maxHeight, height + bottomHeight)
            ans.append(maxHeight)

        return ans


s = Solution()
print(s.fallingSquares([[1, 2], [2, 3], [6, 1]]))
print(s.fallingSquares([[100, 100], [200, 100]]))
