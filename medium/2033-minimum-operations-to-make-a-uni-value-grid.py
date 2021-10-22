'''
2033. 获取单值网格的最小操作数
给你一个大小为 m x n 的二维整数网格 grid 和一个整数 x 。每一次操作，你可以对 grid 中的任一元素 加 x 或 减 x 。

单值网格 是全部元素都相等的网格。

返回使网格化为单值网格所需的 最小 操作数。如果不能，返回 -1 。



示例 1：



输入：grid = [[2,4],[6,8]], x = 2
输出：4
解释：可以执行下述操作使所有元素都等于 4 ：
- 2 加 x 一次。
- 6 减 x 一次。
- 8 减 x 两次。
共计 4 次操作。
示例 2：



输入：grid = [[1,5],[2,3]], x = 1
输出：5
解释：可以使所有元素都等于 3 。
示例 3：



输入：grid = [[1,2],[3,4]], x = 2
输出：-1
解释：无法使所有元素相等。


提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 10^5
1 <= m * n <= 10^5
1 <= x, grid[i][j] <= 10^4
'''
from typing import List
from collections import defaultdict
'''
思路：扫描线
首先遍历一次矩阵，求所有元素之和，最大值，最小值，每个值的计数。在这一次遍历过程中如果发现任意2个元素的差不是x的整数倍，则无法使所有元素相等。
然后，从最小值迭代到最大值，每次的增量是x，对于当前值a：
- 如果都变成a，需要将小于a的元素和与a*m*n的差除以x得到操作数，大于a的元素和a*m*n的差除以x得到操作数。前面2个操作数之和即为都变成a的操作数。
经过上面的扫描所有值，得到最小的操作数。
具体查看下面代码

时间复杂度：O(mn)
空间复杂度：O(mn)
'''


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        counter = defaultdict(int)
        ltCount, gtCount = 0, len(grid) * len(grid[0])  # 保存小于当前值的个数，大于当前值个数
        ltSum, gtSum = 0, 0  # 保存小于当前值之和，大于当前值之和
        minVal, maxVal, val = float('inf'), float('-inf'), grid[0][0]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                minVal = min(minVal, grid[i][j])
                maxVal = max(maxVal, grid[i][j])
                if (grid[i][j] - val) % x:  # 与基准值的差不是x的整数倍，无法得到该值
                    return -1
                gtSum += grid[i][j]  # 求和
                counter[grid[i][j]] += 1  # 计数
        ans = float('inf')
        for val in range(minVal, maxVal + 1, x):  # 扫描从minVal到maxVal的值，val作为矩阵的单值
            gtCount -= counter[val]  # 大于val的所有元素的个数
            gtSum -= val * counter[val]  # 大于val的所有元素的和
            ops = (ltCount * val - ltSum) // x  # 小于val的元素调整成val需要的操作数
            ops += (gtSum - gtCount * val) // x  # 大于val的元素调整成val需要的操作数
            ans = min(ans, ops)
            ltCount += counter[val]  # 小于val的所有元素的个数
            ltSum += val * counter[val]  # 小于val的所有元素的和
        return ans


s = Solution()
print(s.minOperations(grid=[[2, 4], [6, 8]], x=2))
print(s.minOperations(grid=[[1, 5], [2, 3]], x=1))
print(s.minOperations(grid=[[1, 2], [3, 4]], x=2))
