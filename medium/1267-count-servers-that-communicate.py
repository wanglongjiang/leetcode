'''
统计参与通信的服务器
这里有一幅服务器分布图，服务器的位置标识在 m * n 的整数矩阵网格 grid 中，1 表示单元格上有服务器，0 表示没有。

如果两台服务器位于同一行或者同一列，我们就认为它们之间可以进行通信。

请你统计并返回能够与至少一台其他服务器进行通信的服务器的数量。

 

示例 1：
输入：grid = [[1,0],[0,1]]
输出：0
解释：没有一台服务器能与其他服务器进行通信。

示例 2：
输入：grid = [[1,0],[1,1]]
输出：3
解释：所有这些服务器都至少可以与一台别的服务器进行通信。

示例 3：
输入：grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
输出：4
解释：第一行的两台服务器互相通信，第三列的两台服务器互相通信，但右下角的服务器无法与其他服务器通信。

提示：
m == grid.length
n == grid[i].length
1 <= m <= 250
1 <= n <= 250
grid[i][j] == 0 or 1
'''
from typing import List
'''
思路：数组+哈希
设2个长度分别为m和n的数组row,col，这2个数组分别存储出现在某一行，某一列的计算机坐标。
再设一个哈希set用于存储能与其他服务器通信的服务器坐标。
具体算法是：
1. 遍历矩阵所有单元格，如果该行有服务器，尝试将其存入row,col对应的坐标处，
> 如果原先值>=0，说明已经有服务器存在，将原坐标和当前服务器的坐标存入set
> 如果原先值为-1，说之前该行或该列还没有服务器，把当前服务器的坐标写入该坐标
2. 最后set的大小即为可以与其他服务器通信的数量

时间复杂度：O(mn)
空间复杂度：O(n)
'''


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row, col = [-1] * m, [-1] * n
        servers = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    pos = i * n + j
                    if row[i] < 0:  # 该行没有出现过服务器，将其加入
                        row[i] = pos
                    else:  # 该行出现过服务器，将当前服务器和原服务器保存到哈希集合中
                        servers.add(pos)
                        servers.add(row[i])
                    if col[j] < 0:  # 列，同上
                        col[j] = pos
                    else:  # 列，同上
                        servers.add(pos)
                        servers.add(col[j])
        return len(servers)


s = Solution()
print(s.countServers([[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]))
print(s.countServers([[1, 0], [0, 1]]))
print(s.countServers([[1, 0], [1, 1]]))
