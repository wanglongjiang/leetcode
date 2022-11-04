'''
1298. 你能从盒子里获得的最大糖果数
困难
34
相关企业
给你 n 个盒子，每个盒子的格式为 [status, candies, keys, containedBoxes] ，其中：

状态字 status[i]：整数，如果 box[i] 是开的，那么是 1 ，否则是 0 。
糖果数 candies[i]: 整数，表示 box[i] 中糖果的数目。
钥匙 keys[i]：数组，表示你打开 box[i] 后，可以得到一些盒子的钥匙，每个元素分别为该钥匙对应盒子的下标。
内含的盒子 containedBoxes[i]：整数，表示放在 box[i] 里的盒子所对应的下标。
给你一个 initialBoxes 数组，表示你现在得到的盒子，你可以获得里面的糖果，也可以用盒子里的钥匙打开新的盒子，
还可以继续探索从这个盒子里找到的其他盒子。

请你按照上述规则，返回可以获得糖果的 最大数目 。

 

示例 1：

输入：status = [1,0,1,0], candies = [7,5,4,100], keys = [[],[],[1],[]], containedBoxes = [[1,2],[3],[],[]], initialBoxes = [0]
输出：16
解释：
一开始你有盒子 0 。你将获得它里面的 7 个糖果和盒子 1 和 2。
盒子 1 目前状态是关闭的，而且你还没有对应它的钥匙。所以你将会打开盒子 2 ，并得到里面的 4 个糖果和盒子 1 的钥匙。
在盒子 1 中，你会获得 5 个糖果和盒子 3 ，但是你没法获得盒子 3 的钥匙所以盒子 3 会保持关闭状态。
你总共可以获得的糖果数目 = 7 + 4 + 5 = 16 个。
示例 2：

输入：status = [1,0,0,0,0,0], candies = [1,1,1,1,1,1], keys = [[1,2,3,4,5],[],[],[],[],[]], 
containedBoxes = [[1,2,3,4,5],[],[],[],[],[]], initialBoxes = [0]
输出：6
解释：
你一开始拥有盒子 0 。打开它你可以找到盒子 1,2,3,4,5 和它们对应的钥匙。
打开这些盒子，你将获得所有盒子的糖果，所以总糖果数为 6 个。
示例 3：

输入：status = [1,1,1], candies = [100,1,100], keys = [[],[0,2],[]], containedBoxes = [[],[],[]], initialBoxes = [1]
输出：1
示例 4：

输入：status = [1], candies = [100], keys = [[]], containedBoxes = [[]], initialBoxes = []
输出：0
示例 5：

输入：status = [1,1,1], candies = [2,3,2], keys = [[],[],[]], containedBoxes = [[],[],[]], initialBoxes = [2,1,0]
输出：7
 

提示：

1 <= status.length <= 1000
status.length == candies.length == keys.length == containedBoxes.length == n
status[i] 要么是 0 要么是 1 。
1 <= candies[i] <= 1000
0 <= keys[i].length <= status.length
0 <= keys[i][j] < status.length
keys[i] 中的值都是互不相同的。
0 <= containedBoxes[i].length <= status.length
0 <= containedBoxes[i][j] < status.length
containedBoxes[i] 中的值都是互不相同的。
每个盒子最多被一个盒子包含。
0 <= initialBoxes.length <= status.length
0 <= initialBoxes[i] < status.length
'''
from typing import List
'''
[TOC]

# 思路
BFS

# 解题方法
> 设2个哈希集合freeKeys和lockBoxes，分别保存已经释放出来的钥匙和锁住的盒子id
> 初始将所有initialBoxes中的盒子id加入队列
> 用BFS套路开始遍历队列中的盒子，打开盒子i，
>> 将盒子中的keys拿出来，如果key对应的盒子在lockBoxes中，将盒子加入队列
>> 将盒子中的盒子，也即 containedBoxes[i]中释放出来，如果这些盒子的钥匙在freeKeys中或者status[i]==1，将盒子加入队列，否则盒子加入lockBoxes
> 持续上述过程，直至队列为空，处理过程中累计打开的盒子中的糖果数量

# 复杂度
- 时间复杂度: 
>  $O(n)$，每个盒子最多加入队列1次，加入freeKeys1次，加入lockBoxes1次

- 空间复杂度: 
> $O(n)$
'''


class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        freeKeys, lockBoxes, marked = set(), set(), set()
        queue, ans = [i for i in initialBoxes if status[i] == 1], 0  # 未锁住的盒子加入队列
        lockBoxes.update(i for i in initialBoxes if status[i] == 0)  # 锁住的盒子加入lockBoxes
        marked.update(queue)
        while queue:
            i = queue.pop()
            ans += candies[i]
            for key in keys[i]:
                if key in marked:  # 该盒子已经打开，跳过
                    continue
                if key in lockBoxes:  # 锁住的盒子找到了钥匙，将盒子加入队列待打开
                    queue.append(key)
                    marked.add(key)
                else:  # 没有找到盒子的钥匙收起来
                    freeKeys.add(key)
            for box in containedBoxes[i]:
                if box in marked:  # 该盒子已经打开，跳过
                    continue
                if box in freeKeys or status[box]:  # 有钥匙或者未锁的盒子加入队列待打开
                    queue.append(box)
                    marked.add(box)
                else:  # 锁住且没有钥匙的盒子加入lockBoxes
                    lockBoxes.add(box)
        return ans


s = Solution()
assert s.maxCandies(
    status=[1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0],
    candies=[
        732, 320, 543, 300, 814, 568, 947, 685, 142, 111, 805, 233, 813, 306, 55, 1, 290, 944, 36, 592, 150, 596, 372, 299, 644, 445, 605, 202, 64, 807, 753,
        731, 552, 766, 119, 862, 453, 136, 43, 572, 801, 518, 936, 408, 515, 215, 492, 738, 154
    ],
    keys=[[42, 2, 24, 8, 39, 16, 46], [20, 39, 46, 21, 32, 31, 43, 16, 12, 23, 3], [21, 14, 30, 2, 11, 13, 27, 37, 4, 48], [16, 17, 15, 6],
          [31, 14, 3, 32, 35, 19, 42, 43, 44, 29, 25, 41], [7, 39, 2, 3, 40, 28, 37, 35, 43, 22, 6, 23, 48, 10, 21, 11],
          [27, 1, 37, 3, 45, 32, 30, 26, 16, 2, 35, 19, 31, 47, 5, 14], [28, 35, 23, 17, 6], [6, 39, 34,
                                                                                              22], [44, 29, 36, 31, 40, 22, 9, 11, 17, 25, 1, 14, 41],
          [39, 37, 11, 36, 17, 42, 13, 12, 7, 9, 43, 41], [23, 16, 32, 37], [36, 39, 21, 41], [15, 27, 5, 42], [11, 5, 18, 48, 25, 47, 17, 0, 41, 26, 9, 29],
          [18, 36, 40, 35, 12, 33, 11, 5, 44, 14, 46, 7], [48, 22, 11, 33, 14], [44, 12, 3, 31, 25, 15, 18, 28, 42, 43], [36, 9, 0, 42],
          [1, 22, 3, 24, 9, 11, 43, 8, 35, 5, 41, 29, 40], [15, 47, 32, 28, 33, 31, 4, 43], [1, 11, 6, 37, 28], [46, 20, 47, 32, 26, 15, 11, 40],
          [33, 45, 26, 40, 12, 3, 16, 18, 10, 28, 5], [14, 6, 4, 46, 34, 9, 33, 24, 30, 12, 37], [45, 24, 18, 31, 32, 39, 26, 27],
          [29, 0, 32, 15, 7, 48, 36, 26, 33, 31, 18, 39, 23, 34, 44], [25, 16, 42, 31, 41, 35, 26, 10, 3, 1, 4, 29],
          [8, 11, 5, 40, 9, 18, 10, 16, 26, 30, 19, 2, 14, 4], [], [0, 20, 17, 47, 41, 36, 23, 42, 15, 13, 27], [7, 15, 44, 38, 41, 42, 26, 19, 5, 47], [],
          [37, 22], [21, 24, 15, 48, 33, 6, 39, 11], [23, 7, 3, 29, 10, 40, 1, 16, 6, 8, 27], [27, 29, 25, 26, 46, 15, 16],
          [33, 40, 10, 38, 13, 19, 17, 23, 32, 39, 7], [35, 3, 39, 18], [47, 11, 27, 23, 35, 26, 43, 4, 22, 38, 44, 31, 1, 0], [],
          [18, 43, 46, 9, 15, 3, 42, 31, 13, 4, 12, 39, 22], [42, 45, 47, 18, 26, 41, 38, 9, 0, 35, 8, 16, 29, 36, 31], [3, 20, 29, 12, 46, 41, 23, 4, 9, 27],
          [19, 33], [32, 18], [17, 28, 7, 35, 6, 22, 4, 43], [41, 31, 20, 28, 35, 32, 24, 23, 0, 33, 18, 39, 29, 30, 16], [43, 47, 46]],
    containedBoxes=[[14], [], [26], [4, 47], [], [6], [39, 43, 46], [30], [], [], [0, 3], [], [], [], [], [27], [], [], [], [], [12], [], [], [41], [], [31],
                    [20, 29], [13, 35], [18], [10, 40], [], [38], [], [], [19], [5], [], [], [11], [1], [15], [], [], [], [24], [], [], [], []],
    initialBoxes=[2, 7, 8, 9, 16, 17, 21, 22, 23, 25, 28, 32, 33, 34, 36, 37, 42, 44, 45, 48]) == 23185
assert s.maxCandies(status=[1, 0, 1, 0], candies=[7, 5, 4, 100], keys=[[], [], [], []], containedBoxes=[[1, 2], [3], [], []], initialBoxes=[1, 2]) == 4
assert s.maxCandies(status=[1, 1, 1], candies=[100, 1, 100], keys=[[], [0, 2], []], containedBoxes=[[], [], []], initialBoxes=[1]) == 1
assert s.maxCandies(status=[1, 0, 1, 0], candies=[7, 5, 4, 100], keys=[[], [], [1], []], containedBoxes=[[1, 2], [3], [], []], initialBoxes=[0]) == 16
assert s.maxCandies(status=[1, 0, 0, 0, 0, 0],
                    candies=[1, 1, 1, 1, 1, 1],
                    keys=[[1, 2, 3, 4, 5], [], [], [], [], []],
                    containedBoxes=[[1, 2, 3, 4, 5], [], [], [], [], []],
                    initialBoxes=[0]) == 6
assert s.maxCandies(status=[1], candies=[100], keys=[[]], containedBoxes=[[]], initialBoxes=[]) == 0
assert s.maxCandies(status=[1, 1, 1], candies=[2, 3, 2], keys=[[], [], []], containedBoxes=[[], [], []], initialBoxes=[2, 1, 0]) == 7
