'''
剑指 Offer II 107. 矩阵中的距离
给定一个由 0 和 1 组成的矩阵 mat ，请输出一个大小相同的矩阵，其中每一个格子是 mat 中对应位置元素到最近的 0 的距离。

两个相邻元素间的距离为 1 。

 

示例 1：



输入：mat = [[0,0,0],[0,1,0],[0,0,0]]
输出：[[0,0,0],[0,1,0],[0,0,0]]
示例 2：



输入：mat = [[0,0,0],[0,1,0],[1,1,1]]
输出：[[0,0,0],[0,1,0],[1,2,1]]
 

提示：

m == mat.length
n == mat[i].length
1 <= m, n <= 10^4
1 <= m * n <= 10^4
mat[i][j] is either 0 or 1.
mat 中至少有一个 0 
 

注意：本题与主站 542 题相同：https://leetcode-cn.com/problems/01-matrix/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/2bCMpM
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
'''
思路：BFS
从每个为0的节点出发，遍历周围为1的节点

时间复杂度：O(mn*mn)，实际应该远小于
空间复杂度：O(1)，除了返回值，不需要额外空间
'''


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        ans = [[float('inf')] * n for _ in range(m)]
        q, nextq = [], []
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:  # 将为0的单元格加入队列待遍历
                    ans[i][j] = 0  # 为0的单元格，其距离为0
                    q.append((i, j))
        while q:
            a, b = q.pop()
            for x, y in [(a + 1, b), (a - 1, b), (a, b + 1), (a, b - 1)]:
                if 0 <= x < m and 0 <= y < n and mat[x][y] and ans[x][y] > ans[a][b] + 1:  # 遍历距离小于当前距离的单元格
                    ans[x][y] = ans[a][b] + 1  # 更新距离
                    nextq.append((x, y))
            if not q:
                q, nextq = nextq, q
        return ans


s = Solution()
print(s.updateMatrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
