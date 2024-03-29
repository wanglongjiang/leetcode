'''
1326. 灌溉花园的最少水龙头数目
困难
116
相关企业
在 x 轴上有一个一维的花园。花园长度为 n，从点 0 开始，到点 n 结束。

花园里总共有 n + 1 个水龙头，分别位于 [0, 1, ..., n] 。

给你一个整数 n 和一个长度为 n + 1 的整数数组 ranges ，其中 ranges[i] （下标从 0 开始）表示：
如果打开点 i 处的水龙头，可以灌溉的区域为 [i -  ranges[i], i + ranges[i]] 。

请你返回可以灌溉整个花园的 最少水龙头数目 。如果花园始终存在无法灌溉到的地方，请你返回 -1 。

 

示例 1：



输入：n = 5, ranges = [3,4,1,1,0,0]
输出：1
解释：
点 0 处的水龙头可以灌溉区间 [-3,3]
点 1 处的水龙头可以灌溉区间 [-3,5]
点 2 处的水龙头可以灌溉区间 [1,3]
点 3 处的水龙头可以灌溉区间 [2,4]
点 4 处的水龙头可以灌溉区间 [4,4]
点 5 处的水龙头可以灌溉区间 [5,5]
只需要打开点 1 处的水龙头即可灌溉整个花园 [0,5] 。
示例 2：

输入：n = 3, ranges = [0,0,0,0]
输出：-1
解释：即使打开所有水龙头，你也无法灌溉整个花园。
 

提示：

1 <= n <= 104
ranges.length == n + 1
0 <= ranges[i] <= 100
'''

from typing import List
'''
[TOC]

# 思路
排序 贪心

# 解题方法
1. 先计算每个水龙头的覆盖范围[[left1,right1],...[lefti,righti]...]
2. 按照左边界升序，右边界降序，排序上面的区间数组
3. 所有的区间需要能够连结起来，如果中间有空挡，返回-1
4. 遍历过程中，如果一个区间没有被上一个区间覆盖，肯定能够用上（因为按照左边界升序、右边界降序排序过），计数需要+1

# 复杂度
- 时间复杂度: 
> $O(nlog(n))$

- 空间复杂度: 
> $O(n)$
'''


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        prev = [x for x in range(n + 1)]
        for i in range(n + 1):
            l = max(i - ranges[i], 0)
            r = min(i + ranges[i], n)
            prev[r] = min(prev[r], l)

        breakpoint, furthest = n, 2**30
        ans = 0
        for i in range(n, 0, -1):
            furthest = min(furthest, prev[i])
            if i == breakpoint:
                if furthest >= i:
                    return -1
                breakpoint = furthest
                ans += 1

        return ans


s = Solution()
assert s.minTaps(n=5, ranges=[3, 4, 1, 1, 0, 0]) == 1
assert s.minTaps(n=3, ranges=[0, 0, 0, 0]) == -1
