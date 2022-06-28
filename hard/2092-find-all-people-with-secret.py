'''
2092. 找出知晓秘密的所有专家
给你一个整数 n ，表示有 n 个专家从 0 到 n - 1 编号。另外给你一个下标从 0 开始的二维整数数组 meetings ，
其中 meetings[i] = [xi, yi, timei] 表示专家 xi 和专家 yi 在时间 timei 要开一场会。一个专家可以同时参加 多场会议 。
最后，给你一个整数 firstPerson 。

专家 0 有一个 秘密 ，最初，他在时间 0 将这个秘密分享给了专家 firstPerson 。接着，这个秘密会在每次有知晓这个秘密的专家参加会议时进行传播。
更正式的表达是，每次会议，如果专家 xi 在时间 timei 时知晓这个秘密，那么他将会与专家 yi 分享这个秘密，反之亦然。

秘密共享是 瞬时发生 的。也就是说，在同一时间，一个专家不光可以接收到秘密，还能在其他会议上与其他专家分享。

在所有会议都结束之后，返回所有知晓这个秘密的专家列表。你可以按 任何顺序 返回答案。

 

示例 1：

输入：n = 6, meetings = [[1,2,5],[2,3,8],[1,5,10]], firstPerson = 1
输出：[0,1,2,3,5]
解释：
时间 0 ，专家 0 将秘密与专家 1 共享。
时间 5 ，专家 1 将秘密与专家 2 共享。
时间 8 ，专家 2 将秘密与专家 3 共享。
时间 10 ，专家 1 将秘密与专家 5 共享。
因此，在所有会议结束后，专家 0、1、2、3 和 5 都将知晓这个秘密。
示例 2：

输入：n = 4, meetings = [[3,1,3],[1,2,2],[0,3,3]], firstPerson = 3
输出：[0,1,3]
解释：
时间 0 ，专家 0 将秘密与专家 3 共享。
时间 2 ，专家 1 与专家 2 都不知晓这个秘密。
时间 3 ，专家 3 将秘密与专家 0 和专家 1 共享。
因此，在所有会议结束后，专家 0、1 和 3 都将知晓这个秘密。
示例 3：

输入：n = 5, meetings = [[3,4,2],[1,2,1],[2,3,1]], firstPerson = 1
输出：[0,1,2,3,4]
解释：
时间 0 ，专家 0 将秘密与专家 1 共享。
时间 1 ，专家 1 将秘密与专家 2 共享，专家 2 将秘密与专家 3 共享。
注意，专家 2 可以在收到秘密的同一时间分享此秘密。
时间 2 ，专家 3 将秘密与专家 4 共享。
因此，在所有会议结束后，专家 0、1、2、3 和 4 都将知晓这个秘密。
 

提示：

2 <= n <= 105
1 <= meetings.length <= 105
meetings[i].length == 3
0 <= xi, yi <= n - 1
xi != yi
1 <= timei <= 105
1 <= firstPerson <= n - 1
'''
from collections import defaultdict, deque
from typing import List
'''
思路：BFS
这道题的烦人点在于开会的同时，秘密能即时共享。为解决这个问题，思路是：
1、对所有会议按照开会时间排序。
2、设一个集合knowSet，保存所有知道专家的集合，初始将0和firstPerson放入。
3、遍历排序好的会议，相同时间的为一组，每组会议从已知秘密的专家出发，多路BFS遍历参与会议的专家，能遍历到的专家加入knowSet。
4、重复上述过程4，直至所有会议都被处理完毕，此时konwSet中即为知道秘密的专家。

时间复杂度：O(m),m==meetings.length
空间复杂度：O(m)
'''


class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key=lambda m: m[2])  # 对会议排序
        knowSet = set()
        knowSet.add(firstPerson)
        knowSet.add(0)

        def bfs(start, end):
            adjList = defaultdict(list)  # 邻接表，key为专家，value为与该专家开会的其他专家
            q = deque()  # bfs的队列
            marked = set()
            for meeting in meetings[start:end]:  # 遍历同一时间的所有会议，加入邻接表，已知专家加入队列待遍历
                adjList[meeting[0]].append(meeting[1])
                adjList[meeting[1]].append(meeting[0])
                if meeting[0] in knowSet and meeting[0] not in marked:
                    q.append(meeting[0])
                    marked.add(meeting[0])
                if meeting[1] in knowSet and meeting[1] not in marked:
                    q.append(meeting[1])
                    marked.add(meeting[1])
            while q:
                for next in adjList[q.popleft()]:  # 将专家的所有共同参会人加入已知秘密团伙，并将其加入队列待遍历
                    if next not in marked:
                        marked.add(next)
                        knowSet.add(next)
                        q.append(next)

        start = 0
        for i in range(len(meetings)):
            if meetings[i][2] != meetings[start][2]:  # 会议时间发生变化，将这一组会议进行BFS查找所有能知道秘密的专家
                bfs(start, i)
                start = i
        bfs(start, len(meetings))
        return list(knowSet)


s = Solution()
print(s.findAllPeople(6, [[0, 2, 1], [1, 3, 1], [4, 5, 1]], 1))
print(s.findAllPeople(n=6, meetings=[[1, 2, 5], [2, 3, 8], [1, 5, 10]], firstPerson=1))
print(s.findAllPeople(n=4, meetings=[[3, 1, 3], [1, 2, 2], [0, 3, 3]], firstPerson=3))
print(s.findAllPeople(n=5, meetings=[[3, 4, 2], [1, 2, 1], [2, 3, 1]], firstPerson=1))
