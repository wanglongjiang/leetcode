'''
地图分析
你现在手里有一份大小为 N x N 的 网格 grid，上面的每个 单元格 都用 0 和 1 标记好了。
其中 0 代表海洋，1 代表陆地，请你找出一个海洋单元格，这个海洋单元格到离它最近的陆地单元格的距离是最大的。

我们这里说的距离是「曼哈顿距离」（ Manhattan Distance）：(x0, y0) 和 (x1, y1) 这两个单元格之间的距离是 |x0 - x1| + |y0 - y1| 。

如果网格上只有陆地或者海洋，请返回 -1。

提示：
1 <= grid.length == grid[0].length <= 100
grid[i][j] 不是 0 就是 1
'''
from typing import List
'''
设矩阵长、宽都是n。
思路1，暴力查找法，每个海洋点计算与其他陆地点的距离，然后找出其中最大的。
时间复杂度：O(n^4)，根据输入，能达到10^8
思路2，暴力渲染法，从每个陆地开始，广度优先计算距离，如果遇到了其他陆地渲染的距离，对比双方距离，
如果本点开始的距离近采用本点，否则不再向该方向前进。
时间复杂度：最坏情况下也是O(n^4)

思路3，动态规划。可以看到，1个海洋点距离陆地的距离等于与其相邻的点（上下左右4个）最小距离陆地距离+1。
可以进行2次遍历。
第1次遍历，从上往下从左往右，每个陆地点距离是0，海洋点的距离是min(左边节点距离，上边节点距离)+1。第1次动态规划执行完之后，
只从距离左边、上边陆地的距离正确计算了，右边、下边的距离不对。
第2次遍历，从下往上，从右往左进行，这次遍历可以将距离右边、下边的距离修正。这次从中挑选出距离最大的值即可。
时间复杂度：O(n^2)
空间复杂度：O(n)
'''


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        distance = [[0] * n for _ in range(n)]
        hasLand, hasSea = False, False
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    distance[i][j] = 0
                    hasLand = True
                else:
                    hasSea = True
                    d = 2 * (n - 1)
                    if i > 0:
                        d = min(d, distance[i - 1][j])
                    if j > 0:
                        d = min(d, distance[i][j - 1])
                    distance[i][j] = d + 1
        if not (hasLand and hasSea):
            return -1
        ans = 0
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 0:
                    d = 2 * (n - 1)
                    if i < n - 1:
                        d = min(d, distance[i + 1][j])
                    if j < n - 1:
                        d = min(d, distance[i][j + 1])
                    d = min(d + 1, distance[i][j])
                    distance[i][j] = d
                    ans = max(ans, d)
        return ans


s = Solution()
print(s.maxDistance([[1, 0, 1], [0, 0, 0], [1, 0, 1]]))
print(s.maxDistance([[1, 0, 0], [0, 0, 0], [0, 0, 0]]))
