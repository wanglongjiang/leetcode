'''
749. 隔离病毒
病毒扩散得很快，现在你的任务是尽可能地通过安装防火墙来隔离病毒。

假设世界由 m x n 的二维矩阵 isInfected 组成， isInfected[i][j] == 0 表示该区域未感染病毒，而  isInfected[i][j] == 1 表示该区域已感染病毒。
可以在任意 2 个相邻单元之间的共享边界上安装一个防火墙（并且只有一个防火墙）。

每天晚上，病毒会从被感染区域向相邻未感染区域扩散，除非被防火墙隔离。现由于资源有限，每天你只能安装一系列防火墙来隔离其中一个被病毒感染的区域（一个区域或连续的一片区域），
且该感染区域对未感染区域的威胁最大且 保证唯一 。

你需要努力使得最后有部分区域不被病毒感染，如果可以成功，那么返回需要使用的防火墙个数; 如果无法实现，则返回在世界被病毒全部感染时已安装的防火墙个数。

 

示例 1：



输入: isInfected = [[0,1,0,0,0,0,0,1],[0,1,0,0,0,0,0,1],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0]]
输出: 10
解释:一共有两块被病毒感染的区域。
在第一天，添加 5 墙隔离病毒区域的左侧。病毒传播后的状态是:

第二天，在右侧添加 5 个墙来隔离病毒区域。此时病毒已经被完全控制住了。

示例 2：



输入: isInfected = [[1,1,1],[1,0,1],[1,1,1]]
输出: 4
解释: 虽然只保存了一个小区域，但却有四面墙。
注意，防火墙只建立在两个不同区域的共享边界上。
示例 3:

输入: isInfected = [[1,1,1,0,0,0,0,0,0],[1,0,1,0,1,1,1,1,1],[1,1,1,0,0,0,0,0,0]]
输出: 13
解释: 在隔离右边感染区域后，隔离左边病毒区域只需要 2 个防火墙。
 

提示:

m == isInfected.length
n == isInfected[i].length
1 <= m, n <= 50
isInfected[i][j] is either 0 or 1
在整个描述的过程中，总有一个相邻的病毒区域，它将在下一轮 严格地感染更多未受污染的方块 
'''
from collections import deque
from typing import List
'''
思路：BFS模拟
模拟每一轮病毒向外扩张，找到扩张最多的一个区域进行隔离，直至所有病毒都被隔离。

时间复杂度：O(mn(m+n))
空间复杂度：O(mn)
'''


class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        m, n = len(isInfected), len(isInfected[0])
        ans = 0

        while True:
            neighbors, firewalls = list(), list()
            for i in range(m):
                for j in range(n):
                    if isInfected[i][j] == 1:
                        q = deque([(i, j)])
                        neighbor = set()
                        firewall, idx = 0, len(neighbors) + 1
                        isInfected[i][j] = -idx

                        while q:
                            x, y = q.popleft()
                            for d in range(4):
                                nx, ny = x + dirs[d][0], y + dirs[d][1]
                                if 0 <= nx < m and 0 <= ny < n:
                                    if isInfected[nx][ny] == 1:
                                        q.append((nx, ny))
                                        isInfected[nx][ny] = -idx
                                    elif isInfected[nx][ny] == 0:
                                        firewall += 1
                                        neighbor.add((nx, ny))

                        neighbors.append(neighbor)
                        firewalls.append(firewall)

            if not neighbors:
                break

            idx = 0
            for i in range(1, len(neighbors)):
                if len(neighbors[i]) > len(neighbors[idx]):
                    idx = i

            ans += firewalls[idx]
            for i in range(m):
                for j in range(n):
                    if isInfected[i][j] < 0:
                        if isInfected[i][j] != -idx - 1:
                            isInfected[i][j] = 1
                        else:
                            isInfected[i][j] = 2

            for i, neighbor in enumerate(neighbors):
                if i != idx:
                    for x, y in neighbor:
                        isInfected[x][y] = 1

            if len(neighbors) == 1:
                break

        return ans
