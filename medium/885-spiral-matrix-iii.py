from typing import List
'''
在 rows x cols 的网格上，你从单元格 (rStart, cStart) 面朝东面开始。网格的西北角位于第一行第一列，网格的东南角位于最后一行最后一列。

你需要以顺时针按螺旋状行走，访问此网格中的每个位置。每当移动到网格的边界之外时，需要继续在网格之外行走（但稍后可能会返回到网格边界）。

最终，我们到过网格的所有 rows x cols 个空间。

按照访问顺序返回表示网格位置的坐标列表。
'''
'''
思路：模拟

时间复杂度：O(rows*cols)
空间复杂度：O(1)
'''


class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 各个方向上前进一步，对坐标的影响
        dir = 0  # 目前前进的方向
        width = 1  # 该变量记录螺旋的边长
        step = 0  # 该变量记录当前方向上前进了几步
        widthChangeNum = 0  # 每改变2次方向，螺旋的边长度+1。该变量记录方向改变的次数
        maxCount = rows * cols  # 单元格数
        count = 0  # 已经走过的单元格数
        x, y = rStart, cStart  # 当前坐标
        ans = []
        while count < maxCount:
            if 0 <= x < rows and 0 <= y < cols:  # 如果是合法坐标，将其记录到答案中
                ans.append([x, y])
                count += 1
            if step == width:  # 如果前进的步数已经与螺旋边长相同，需要进行下面的步数清零等操作
                step = 0  # 步数清零
                dir = (dir + 1) % 4  # 改变方向
                widthChangeNum += 1  # 改变方向的次数+1
                if widthChangeNum % 2 == 0:  # 每改变2次方向，需要将螺旋边长+1
                    width += 1
            step += 1  # 前进一步
            x, y = dirs[dir][0] + x, dirs[dir][1] + y  # 改变当前坐标
        return ans


s = Solution()
print(s.spiralMatrixIII(rows=1, cols=4, rStart=0, cStart=0))
print(
    s.spiralMatrixIII(rows=5, cols=6, rStart=1, cStart=4) == [[1, 4], [1, 5], [2, 5], [2, 4], [2, 3], [1, 3], [0, 3], [0, 4], [0, 5], [3, 5], [3, 4], [3, 3],
                                                              [3, 2], [2, 2], [1, 2], [0, 2], [4, 5], [4, 4], [4, 3], [4, 2], [4, 1], [3, 1], [2, 1], [1, 1],
                                                              [0, 1], [4, 0], [3, 0], [2, 0], [1, 0], [0, 0]])
