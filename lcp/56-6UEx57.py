'''
LCP 56. 信物传送
欢迎各位勇者来到力扣城，本次试炼主题为「信物传送」。

本次试炼场地设有若干传送带，matrix[i][j] 表示第 i 行 j 列的传送带运作方向，"^","v","<",">" 
这四种符号分别表示 上、下、左、右 四个方向。信物会随传送带的方向移动。
勇者每一次施法操作，可临时变更一处传送带的方向，在物品经过后传送带恢复原方向。
lcp (2).gif

通关信物初始位于坐标 start处，勇者需要将其移动到坐标 end 处，请返回勇者施法操作的最少次数。

注意：

start 和 end 的格式均为 [i,j]
示例 1:

输入：matrix = [">>v","v^<","<><"], start = [0,1], end = [2,0]

输出：1

解释：
如上图所示
当信物移动到 [1,1] 时，勇者施法一次将 [1,1] 的传送方向 ^ 从变更为 <
从而信物移动到 [1,0]，后续到达 end 位置
因此勇者最少需要施法操作 1 次

示例 2:

输入：matrix = [">>v",">>v","^<<"], start = [0,0], end = [1,1]

输出：0

解释：勇者无需施法，信物将自动传送至 end 位置

示例 3:

输入：matrix = [">^^>","<^v>","^v^<"], start = [0,0], end = [1,3]

输出：3

提示：

matrix 中仅包含 '^'、'v'、'<'、'>'
0 < matrix.length <= 100
0 < matrix[i].length <= 100
0 <= start[0],end[0] < matrix.length
0 <= start[1],end[1] < matrix[i].length
'''
import heapq
from typing import List
'''
思路：BFS 堆
从开始单元格开始，单元格原本前进方向上前进代价为0，其余方向上前进代价为1，将下一个单元格的代价和坐标加入堆。
如果下一个单元格已经遍历过，再次遍历时距离变短，也需要加入堆再次遍历，否则不再遍历。
直至找到end

时间复杂度：O(mn)
空间复杂度：O(mn)
'''


class Solution:
    def conveyorBelt(self, matrix: List[str], start: List[int], end: List[int]) -> int:
        h = [(0, (start[0], start[1]))]  # 初始节点加入堆
        m, n = len(matrix), len(matrix[0])
        end = (end[0], end[1])
        dists = {}
        dists[(start[0], start[1])] = 0
        while h:
            dis, node = heapq.heappop(h)
            if node == end:
                return dis
            x, y = node[0], node[1]
            if x > 0:
                newdist = dis if matrix[x][y] == '^' else dis + 1
                newpos = (x - 1, y)
                if newpos not in dists or dists[newpos] > newdist:
                    heapq.heappush(h, (newdist, newpos))
                    dists[newpos] = newdist
            if x < m - 1:
                newdist = dis if matrix[x][y] == 'v' else dis + 1
                newpos = (x + 1, y)
                if newpos not in dists or dists[newpos] > newdist:
                    heapq.heappush(h, (newdist, newpos))
                    dists[newpos] = newdist
            if y > 0:
                newdist = dis if matrix[x][y] == '<' else dis + 1
                newpos = (x, y - 1)
                if newpos not in dists or dists[newpos] > newdist:
                    heapq.heappush(h, (newdist, newpos))
                    dists[newpos] = newdist
            if y < n - 1:
                newdist = dis if matrix[x][y] == '>' else dis + 1
                newpos = (x, y + 1)
                if newpos not in dists or dists[newpos] > newdist:
                    heapq.heappush(h, (newdist, newpos))
                    dists[newpos] = newdist
        return -1


s = Solution()
print(s.conveyorBelt(matrix=[">>v", "v^<", "<><"], start=[0, 1], end=[2, 0]))
print(s.conveyorBelt(matrix=[">>v", ">>v", "^<<"], start=[0, 0], end=[1, 1]))
print(s.conveyorBelt(matrix=[">^^>", "<^v>", "^v^<"], start=[0, 0], end=[1, 3]))
