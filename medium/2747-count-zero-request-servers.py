from collections import Counter
from typing import List
'''
[TOC]

# 思路
滑动窗口 哈希表

# 解题方法
1、复制queries，将其排序
2、用时间排序logs
3、滑动窗口遍历logs，检查每个queries时间窗口x内的服务器数量，将其加入哈希表
4、遍历一次queries，丛哈希表中提取答案

# 复杂度
- 时间复杂度: 
> $O(mlogm+llogl)$ ，m=logs.length,l=queries.length

- 空间复杂度: 
> $O(n+l)$
'''


class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        q2 = queries.copy()
        logs.sort(key=lambda log: log[1])
        q2.sort()
        low, high = 0, 0
        m = len(logs)
        serverCounter = Counter()
        zeroReqCounter = Counter()
        for q in q2:
            while high < m and logs[high][1] <= q:  # 扩大窗口，直至日志日期接近q
                serverCounter[logs[high][0]] += 1
                high += 1
            while low < high and logs[low][1] < q - x:  # 缩小窗口，将不在窗口内的日志排除
                serverCounter[logs[low][0]] -= 1
                if serverCounter[logs[low][0]] == 0:
                    del serverCounter[logs[low][0]]
                low += 1
            # 记录时间q时没有接到访问的服务器
            zeroReqCounter[q] = n - len(serverCounter)
        return [zeroReqCounter[q] for q in queries]


s = Solution()
assert s.countServers(n=3, logs=[[1, 3], [2, 6], [1, 5]], x=5, queries=[10, 11]) == [1, 2]
assert s.countServers(n=3, logs=[[2, 4], [2, 1], [1, 2], [3, 1]], x=2, queries=[3, 4]) == [0, 1]
