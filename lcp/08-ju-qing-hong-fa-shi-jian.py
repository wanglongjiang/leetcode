'''
LCP 08. 剧情触发时间

在战略游戏中，玩家往往需要发展自己的势力来触发各种新的剧情。一个势力的主要属性有三种，分别是文明等级（C），资源储备（R）以及人口数量（H）。
在游戏开始时（第 0 天），三种属性的值均为 0。

随着游戏进程的进行，每一天玩家的三种属性都会对应增加，我们用一个二维数组 increase 来表示每天的增加情况。
这个二维数组的每个元素是一个长度为 3 的一维数组，例如 [[1,2,1],[3,4,2]] 表示第一天三种属性分别增加 1,2,1 而第二天分别增加 3,4,2。

所有剧情的触发条件也用一个二维数组 requirements 表示。这个二维数组的每个元素是一个长度为 3 的一维数组，
对于某个剧情的触发条件 c[i], r[i], h[i]，如果当前 C >= c[i] 且 R >= r[i] 且 H >= h[i] ，则剧情会被触发。

根据所给信息，请计算每个剧情的触发时间，并以一个数组返回。如果某个剧情不会被触发，则该剧情对应的触发时间为 -1 。
'''
from typing import List
'''
思路1，根据increase(长度为m)生成各个时间点上的属性list(长度为m)，然后遍历requirements数组(长度为n)，二分查找满足需求的时间点。
时间复杂度：O(m+nlogm)，根据输入，大概是4*10^6
空间复杂度：O(m)，10^4

思路2，动态规划。创建10^5的资源列表，遍历increase，把满足该资源点的时刻填充上，然后再遍历requirements，用索引查找各个资源点的时刻。
时间复杂度：O(m+n)，最大是10^5
空间复杂度：O(10m)，最大10^5
'''


class Solution:
    # 思路2
    def getTriggerTime(self, increase: List[List[int]], requirements: List[List[int]]) -> List[int]:
        m, n = len(increase), len(requirements)
        M = m * 10 + 1
        C, R, H = [-1] * M, [-1] * M, [-1] * M
        C[0], R[0], H[0] = 0, 0, 0
        c, r, h = 0, 0, 0
        # 设置满足资源点的最小时刻
        for i in range(m):
            c, r, h = c + increase[i][0], r + increase[i][1], h + increase[i][2]
            for j in range(c, 0, -1):
                if C[j] < 0:
                    C[j] = i + 1
                else:
                    break
            for j in range(r, 0, -1):
                if R[j] < 0:
                    R[j] = i + 1
                else:
                    break
            for j in range(h, 0, -1):
                if H[j] < 0:
                    H[j] = i + 1
                else:
                    break
        # 查找满足触发剧情的时间点
        ans = [-1] * n
        for i in range(n):
            c, r, h = requirements[i]
            if c >= M or r >= M or h >= M:  # 如果需求超过范围返回-1
                continue
            if C[c] < 0 or R[r] < 0 or H[h] < 0:
                continue
            ans[i] = max(C[c], R[r], H[h])
        return ans


s = Solution()
print(s.getTriggerTime(increase=[[2, 8, 4], [2, 5, 0], [10, 9, 8]], requirements=[[2, 11, 3], [15, 10, 7], [9, 17, 12], [8, 1, 14]]))
print(s.getTriggerTime(increase=[[0, 4, 5], [4, 8, 8], [8, 6, 1], [10, 10, 0]], requirements=[[12, 11, 16], [20, 2, 6], [9, 2, 6], [10, 18, 3], [8, 14, 9]]))
print(s.getTriggerTime(increase=[[1, 1, 1]], requirements=[[0, 0, 0]]))
