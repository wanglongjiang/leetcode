'''
850. 矩形面积 II
我们给出了一个（轴对齐的）二维矩形列表 rectangles 。 对于 rectangle[i] = [x1, y1, x2, y2]，
其中（x1，y1）是矩形 i 左下角的坐标， (xi1, yi1) 是该矩形 左下角 的坐标， (xi2, yi2) 是该矩形 右上角 的坐标。

计算平面中所有 rectangles 所覆盖的 总面积 。任何被两个或多个矩形覆盖的区域应只计算 一次 。

返回 总面积 。因为答案可能太大，返回 109 + 7 的 模 。

 

示例 1：



输入：rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
输出：6
解释：如图所示，三个矩形覆盖了总面积为6的区域。
从(1,1)到(2,2)，绿色矩形和红色矩形重叠。
从(1,0)到(2,3)，三个矩形都重叠。
示例 2：

输入：rectangles = [[0,0,1000000000,1000000000]]
输出：49
解释：答案是 1018 对 (109 + 7) 取模的结果， 即 49 。
 

提示：

1 <= rectangles.length <= 200
rectanges[i].length = 4
0 <= xi1, yi1, xi2, yi2 <= 109
矩形叠加覆盖后的总面积不会超越 2^63 - 1 ，这意味着可以用一个 64 位有符号整数来保存面积结果。
'''
from bisect import bisect_left
from typing import List
'''
思路：离散化 + 扫描线 + 使用线段树实时维护
'''


class Segtree:
    def __init__(self):
        self.cover = 0
        self.length = 0
        self.max_length = 0


class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        hbound = set()
        for rect in rectangles:
            # 下边界
            hbound.add(rect[1])
            # 上边界
            hbound.add(rect[3])

        hbound = sorted(hbound)
        m = len(hbound)
        # 线段树有 m-1 个叶子节点，对应着 m-1 个会被完整覆盖的线段，需要开辟 ~4m 大小的空间
        tree = [Segtree() for _ in range(m * 4 + 1)]

        def init(idx: int, l: int, r: int) -> None:
            tree[idx].cover = tree[idx].length = 0
            if l == r:
                tree[idx].max_length = hbound[l] - hbound[l - 1]
                return

            mid = (l + r) // 2
            init(idx * 2, l, mid)
            init(idx * 2 + 1, mid + 1, r)
            tree[idx].max_length = tree[idx * 2].max_length + tree[idx * 2 + 1].max_length

        def update(idx: int, l: int, r: int, ul: int, ur: int, diff: int) -> None:
            if l > ur or r < ul:
                return
            if ul <= l and r <= ur:
                tree[idx].cover += diff
                pushup(idx, l, r)
                return

            mid = (l + r) // 2
            update(idx * 2, l, mid, ul, ur, diff)
            update(idx * 2 + 1, mid + 1, r, ul, ur, diff)
            pushup(idx, l, r)

        def pushup(idx: int, l: int, r: int) -> None:
            if tree[idx].cover > 0:
                tree[idx].length = tree[idx].max_length
            elif l == r:
                tree[idx].length = 0
            else:
                tree[idx].length = tree[idx * 2].length + tree[idx * 2 + 1].length

        init(1, 1, m - 1)

        sweep = list()
        for i, rect in enumerate(rectangles):
            # 左边界
            sweep.append((rect[0], i, 1))
            # 右边界
            sweep.append((rect[2], i, -1))
        sweep.sort()

        ans = i = 0
        while i < len(sweep):
            j = i
            while j + 1 < len(sweep) and sweep[i][0] == sweep[j + 1][0]:
                j += 1
            if j + 1 == len(sweep):
                break

            # 一次性地处理掉一批横坐标相同的左右边界
            for k in range(i, j + 1):
                _, idx, diff = sweep[k]
                # 使用二分查找得到完整覆盖的线段的编号范围
                left = bisect_left(hbound, rectangles[idx][1]) + 1
                right = bisect_left(hbound, rectangles[idx][3])
                update(1, 1, m - 1, left, right, diff)

            ans += tree[1].length * (sweep[j + 1][0] - sweep[j][0])
            i = j + 1

        return ans % (10**9 + 7)
