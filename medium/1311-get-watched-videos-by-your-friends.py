'''
获取你好友已观看的视频
有 n 个人，每个人都有一个  0 到 n-1 的唯一 id 。

给你数组 watchedVideos  和 friends ，其中 watchedVideos[i]  和 friends[i] 分别表示 id = i 的人观看过的视频列表和他的好友列表。

Level 1 的视频包含所有你好友观看过的视频，level 2 的视频包含所有你好友的好友观看过的视频，以此类推。
一般的，Level 为 k 的视频包含所有从你出发，最短距离为 k 的好友观看过的视频。

给定你的 id  和一个 level 值，请你找出所有指定 level 的视频，并将它们按观看频率升序返回。如果有频率相同的视频，
请将它们按字母顺序从小到大排列。

 

示例 1：



输入：watchedVideos = [["A","B"],["C"],["B","C"],["D"]], friends = [[1,2],[0,3],[0,3],[1,2]], id = 0, level = 1
输出：["B","C"]
解释：
你的 id 为 0（绿色），你的朋友包括（黄色）：
id 为 1 -> watchedVideos = ["C"] 
id 为 2 -> watchedVideos = ["B","C"] 
你朋友观看过视频的频率为：
B -> 1 
C -> 2
示例 2：



输入：watchedVideos = [["A","B"],["C"],["B","C"],["D"]], friends = [[1,2],[0,3],[0,3],[1,2]], id = 0, level = 2
输出：["D"]
解释：
你的 id 为 0（绿色），你朋友的朋友只有一个人，他的 id 为 3（黄色）。
 

提示：

n == watchedVideos.length == friends.length
2 <= n <= 100
1 <= watchedVideos[i].length <= 100
1 <= watchedVideos[i][j].length <= 8
0 <= friends[i].length < n
0 <= friends[i][j] < n
0 <= id < n
1 <= level < n
如果 friends[i] 包含 j ，那么 friends[j] 包含 i
'''
from typing import List
from collections import defaultdict
from collections import deque
'''
思路：BFS+哈希
将friends视为无向图，任意2个人如果互为好友，这2个人之间有一条边。
从id开始出发用bfs找到距离为level的所有人，将他们看过的视频加入哈希表中并进行计数。
最后将哈希表中的key按照计数、字典顺序排序。

时间复杂度：O(n*m+e)e为好友总数量,m为平均每个人观看的视频数量
空间复杂度：O(n*m)
'''


class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        n = len(friends)
        visited = [False] * n
        counter = defaultdict(int)
        # bfs遍历图，找到level的所有节点
        lv = 0
        q, nextq = deque(), deque()
        q.append(id)
        visited[id] = True
        while q:
            pid = q.popleft()
            for nextid in friends[pid]:
                if not visited[nextid]:
                    visited[nextid] = True
                    nextq.append(nextid)
            if not q:
                q, nextq = nextq, q
                lv += 1
                if lv == level:
                    break
        # 遍历level的人看过的视频
        for i in q:
            for video in watchedVideos[i]:
                counter[video] += 1
        return list(map(lambda item: item[0], sorted(counter.items(), key=lambda item: (item[1], item[0]))))


s = Solution()
print(s.watchedVideosByFriends([["A", "B"], ["C"], ["B", "C"], ["D"]], friends=[[1, 2], [0, 3], [0, 3], [1, 2]], id=0, level=1))
print(s.watchedVideosByFriends([["A", "B"], ["C"], ["B", "C"], ["D"]], friends=[[1, 2], [0, 3], [0, 3], [1, 2]], id=0, level=2))
