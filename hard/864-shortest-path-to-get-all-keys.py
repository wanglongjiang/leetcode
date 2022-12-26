'''
864. 获取所有钥匙的最短路径
困难
182
相关企业
给定一个二维网格 grid ，其中：

'.' 代表一个空房间
'#' 代表一堵
'@' 是起点
小写字母代表钥匙
大写字母代表锁
我们从起点开始出发，一次移动是指向四个基本方向之一行走一个单位空间。我们不能在网格外面行走，也无法穿过一堵墙。
如果途经一个钥匙，我们就把它捡起来。除非我们手里有对应的钥匙，否则无法通过锁。

假设 k 为 钥匙/锁 的个数，且满足 1 <= k <= 6，字母表中的前 k 个字母在网格中都有自己对应的一个小写和一个大写字母。
换言之，每个锁有唯一对应的钥匙，每个钥匙也有唯一对应的锁。另外，代表钥匙和锁的字母互为大小写并按字母顺序排列。

返回获取所有钥匙所需要的移动的最少次数。如果无法获取所有钥匙，返回 -1 。

 

示例 1：



输入：grid = ["@.a.#","###.#","b.A.B"]
输出：8
解释：目标是获得所有钥匙，而不是打开所有锁。
示例 2：



输入：grid = ["@..aA","..B#.","....b"]
输出：6
示例 3:


输入: grid = ["@Aa"]
输出: -1
 

提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 30
grid[i][j] 只含有 '.', '#', '@', 'a'-'f' 以及 'A'-'F'
钥匙的数目范围是 [1, 6] 
每个钥匙都对应一个 不同 的字母
每个钥匙正好打开一个对应的锁
'''
from collections import deque
from functools import lru_cache
from math import inf
from typing import List
'''
[TOC]

# 思路
BFS+回溯

# 解题方法
> 初始持有的钥匙为空
> 从起点出发，用BFS遍历矩阵，
>> 如果遇到一个钥匙，更新目前持有的钥匙，如果所有钥匙都已经获取完毕，返回截止目前的路径；如果钥匙没有获取完，将目前钥匙状态和路程记住，启动一个新的BFS过程。
>> 如果遇到锁，且持有钥匙，就开锁继续前进
>> 如果所有路径都遍历完，全部钥匙没有拿到手，返回-1

# 复杂度
- 时间复杂度: 
>  $O(mn*6^k)$，一次BFS时间复杂度为O(mn)，每遇到一个钥匙会产生一次递归，共需要6^k次BFS

- 空间复杂度: 
> $O(mn)$
'''


class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        # 查找起点和所有的钥匙
        startX, startY, allKeys = 0, 0, 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    startX, startY = i, j
                elif 'a' <= grid[i][j] <= 'f':  # 是钥匙
                    allKeys |= 1 << (ord(grid[i][j]) - ord('a'))  # 所有钥匙记录到allKeys上
        ans = inf

        # BFS，x,y为出发位置，dis为从该位置出发的初始距离，keys为目前持有的钥匙
        @lru_cache
        def bfs(x, y, dis, keys):
            queue = deque()
            queue.append((x, y))
            marked = set()
            marked.add((x, y))
            nonlocal ans
            while queue:
                size = len(queue)
                for _ in range(size):
                    x, y = queue.popleft()
                    for nextx, nexty in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                        if 0 <= nextx < m and 0 <= nexty < n and (nextx, nexty) not in marked and grid[nextx][nexty] != '#':
                            if grid[nextx][nexty] == '.' or grid[nextx][nexty] == '@':  # 空房间，加入队列
                                queue.append((nextx, nexty))
                                marked.add((nextx, nexty))
                            elif 'A' <= grid[nextx][nexty] <= 'F':  # 锁，需要判断是否有钥匙
                                if (1 << (ord(grid[nextx][nexty]) - ord('A'))) & keys:  # 如果持有钥匙，单元格可以通过，加入队列
                                    queue.append((nextx, nexty))
                                    marked.add((nextx, nexty))
                            else:  # 钥匙
                                key = 1 << (ord(grid[nextx][nexty]) - ord('a'))
                                if key & keys:  # 如果持有钥匙，直接通过，加入队列
                                    queue.append((nextx, nexty))
                                    marked.add((nextx, nexty))
                                else:  # 之前没有持有该钥匙
                                    if key | keys == allKeys:  # 如果拿到该钥匙后，所有钥匙都被收集齐，返回路径
                                        return dis + 1
                                    # 拿到钥匙后，钥匙没有收齐，需要开启新的BFS遍历
                                    newdis = bfs(nextx, nexty, dis + 1, key | keys)
                                    if newdis > 0:  # 新BFS找到了所有钥匙，尝试更新答案
                                        ans = min(ans, newdis)
                dis += 1
                if dis >= ans:  # 剪枝，如果超过以往的行走距离，退出
                    return ans
            return ans if ans != inf else -1

        return bfs(startX, startY, 0, 0)


s = Solution()
print(
    s.shortestPathAllKeys([
        "#..#.#.#..#.#.#.....#......#..", ".#.......#....#A.....#.#......", "#....#.....#.........#........", "...#.#.........#..@....#....#.",
        ".#.#.##...#.........##....#..#", "..........#..#..###....##..#.#", ".......#......#...#...#.....c#", ".#...#.##......#...#.###...#..",
        "..........##...#.......#......", "#...#.........a#....#.#.##....", "..#..#...#...#..#....#.....##.", "..........#...#.##............",
        "...#....#..#.........#..D.....", "....#E.#....##................", "...........##.#.......#.#....#", "...#..#...#.#............#e...",
        "..#####....#.#...........##..#", "##......##......#.#...#..#.#..", ".#F.......#..##.......#....#..", "............#....#..#..#...#..",
        ".............#...#f...#..##...", "....#..#...##.........#..#..#.", ".....#.....##.###..##.#......#", ".#..#.#...#.....#........###..",
        ".....#.#...#...#.....#.....#..", "##.....#....B.....#..#b.......", ".####....##..#.##..d.#......#.", "..#.....#....##........##...##",
        "...#...#...C..#..#....#.......", "#.....##.....#.#......#......."
    ]))
print(
    s.shortestPathAllKeys(
        ["..#....##.", "....d.#.D#", "#...#.c...", "..##.#..a.", "...#....##", "#....b....", ".#..#.....", "..........", ".#..##..A.", ".B..C.#..@"]))
print(
    s.shortestPathAllKeys([
        "..Ff..#..e.#...", ".....#.##...#..", "....#.#...#....", "##.......##...#", "...@#.##....#..", "#........b.....", "..#...#.....##.", ".#....#E...#...",
        "......A.#D.#...", "...#...#..#....", "...a.#B#.......", ".......c.....#.", "....#...C#...#.", "##.#.....d..#..", ".#..#......#..."
    ]))
print(s.shortestPathAllKeys(["@.a.#", "###.#", "b.A.B"]))
print(s.shortestPathAllKeys(["@..aA", "..B#.", "....b"]))
print(s.shortestPathAllKeys(["@Aa"]))
