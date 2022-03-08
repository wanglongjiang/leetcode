'''
2055. 蜡烛之间的盘子
给你一个长桌子，桌子上盘子和蜡烛排成一列。给你一个下标从 0 开始的字符串 s ，它只包含字符 '*' 和 '|' ，其中 '*' 表示一个 盘子 ，'|' 表示一支 蜡烛 。

同时给你一个下标从 0 开始的二维整数数组 queries ，其中 queries[i] = [lefti, righti] 表示 子字符串 s[lefti...righti] （包含左右端点的字符）。对于每个查询，你需要找到 子字符串中 在 两支蜡烛之间 的盘子的 数目 。如果一个盘子在 子字符串中 左边和右边 都 至少有一支蜡烛，那么这个盘子满足在 两支蜡烛之间 。

比方说，s = "||**||**|*" ，查询 [3, 8] ，表示的是子字符串 "*||**|" 。子字符串中在两支蜡烛之间的盘子数目为 2 ，子字符串中右边两个盘子在它们左边和右边 都 至少有一支蜡烛。
请你返回一个整数数组 answer ，其中 answer[i] 是第 i 个查询的答案。

 

示例 1:

ex-1

输入：s = "**|**|***|", queries = [[2,5],[5,9]]
输出：[2,3]
解释：
- queries[0] 有两个盘子在蜡烛之间。
- queries[1] 有三个盘子在蜡烛之间。
示例 2:

ex-2

输入：s = "***|**|*****|**||**|*", queries = [[1,17],[4,5],[14,17],[5,11],[15,16]]
输出：[9,0,0,0,0]
解释：
- queries[0] 有 9 个盘子在蜡烛之间。
- 另一个查询没有盘子在蜡烛之间。
 

提示：

3 <= s.length <= 105
s 只包含字符 '*' 和 '|' 。
1 <= queries.length <= 105
queries[i].length == 2
0 <= lefti <= righti < s.length
'''

from operator import le
from turtle import left
from typing import List
'''
思路：前缀和
设3个数组，preSum用于记录蜡烛左侧的盘子数量，leftIdx记录盘子左侧最近的蜡烛的索引，rightIdx记录盘子右侧最近的蜡烛的索引

首先扫描字符串s两次：
第1次，如果当前是蜡烛，记录蜡烛左侧的盘子数量，如果当前是盘子，记录上一个蜡烛的索引。
第2次，从右向左遍历，如果当前是盘子，记录盘子右侧最近的蜡烛的索引

然后遍历queries数组：
针对每个查询queries[i] = [lefti, righti]，
如果s[lefti]是盘子，再查询rightIdx[lefti]，找到左侧蜡烛。
如果s[righti]是盘子，再查询leftIdx[righti]，找到右侧蜡烛。
最后在前缀数组preSum查询2个蜡烛之间的盘子数量。
还有一些特殊情况，比如蜡烛超出范围等，需要特殊处理。

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        preSum, leftIdx, rightIdx = [0] * n, [0] * n, [0] * n
        preCandle, count = -1, 0
        for i, chr in enumerate(s):  # 第1次遍历，统计前缀和，盘子左侧蜡烛的索引
            if chr == '|':
                leftIdx[i] = i
                preCandle = i
            else:
                count += 1
                leftIdx[i] = preCandle
            preSum[i] = count
        preCandle, count = n, 0
        for i in range(n - 1, -1, -1):  # 第2次遍历，统计盘子右侧蜡烛的索引
            if s[i] == '|':
                preCandle = i
            else:
                rightIdx[i] = preCandle
        ans = [0] * len(queries)
        for i, q in enumerate(queries):
            leftCandle = q[0]
            if s[leftCandle] == '*':  # lefti为盘子，需要查找右边最近的蜡烛
                leftCandle = rightIdx[leftCandle]
            rightCandle = q[1]
            if s[rightCandle] == '*':  # righti为盘子，需要查找左边最近的蜡烛
                rightCandle = leftIdx[rightCandle]
            if leftCandle < rightCandle:  # 两根蜡烛之间有空间，通过计算前缀和数组的差得到答案
                ans[i] = preSum[rightCandle] - preSum[leftCandle]
        return ans


s = Solution()
print(s.platesBetweenCandles(s="***|**|*****|**||**|*", queries=[[1, 17], [4, 5], [14, 17], [5, 11], [15, 16]]))
print(s.platesBetweenCandles(s="**|**|***|", queries=[[2, 5], [5, 9]]))
