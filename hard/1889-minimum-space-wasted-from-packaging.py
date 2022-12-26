'''
1889. 装包裹的最小浪费空间
困难
29
相关企业
给你 n 个包裹，你需要把它们装在箱子里，每个箱子装一个包裹。总共有 m 个供应商提供 不同尺寸 的箱子（每个规格都有无数个箱子）。
如果一个包裹的尺寸 小于等于 一个箱子的尺寸，那么这个包裹就可以放入这个箱子之中。

包裹的尺寸用一个整数数组 packages 表示，其中 packages[i] 是第 i 个包裹的尺寸。
供应商用二维数组 boxes 表示，其中 boxes[j] 是第 j 个供应商提供的所有箱子尺寸的数组。

你想要选择 一个供应商 并只使用该供应商提供的箱子，使得 总浪费空间最小 。
对于每个装了包裹的箱子，我们定义 浪费的 空间等于 箱子的尺寸 - 包裹的尺寸 。
总浪费空间 为 所有 箱子中浪费空间的总和。

比方说，如果你想要用尺寸数组为 [4,8] 的箱子装下尺寸为 [2,3,5] 的包裹，你可以将尺寸为 2 和 3 的两个包裹装入两个尺寸为 4 的箱子中，
同时把尺寸为 5 的包裹装入尺寸为 8 的箱子中。总浪费空间为 (4-2) + (4-3) + (8-5) = 6 。
请你选择 最优 箱子供应商，使得 总浪费空间最小 。如果 无法 将所有包裹放入箱子中，请你返回 -1 。
由于答案可能会 很大 ，请返回它对 109 + 7 取余 的结果。

 

示例 1：

输入：packages = [2,3,5], boxes = [[4,8],[2,8]]
输出：6
解释：选择第一个供应商最优，用两个尺寸为 4 的箱子和一个尺寸为 8 的箱子。
总浪费空间为 (4-2) + (4-3) + (8-5) = 6 。
示例 2：

输入：packages = [2,3,5], boxes = [[1,4],[2,3],[3,4]]
输出：-1
解释：没有箱子能装下尺寸为 5 的包裹。
示例 3：

输入：packages = [3,5,8,10,11,12], boxes = [[12],[11,9],[10,5,14]]
输出：9
解释：选择第三个供应商最优，用两个尺寸为 5 的箱子，两个尺寸为 10 的箱子和两个尺寸为 14 的箱子。
总浪费空间为 (5-3) + (5-5) + (10-8) + (10-10) + (14-11) + (14-12) = 9 。
 

提示：

n == packages.length
m == boxes.length
1 <= n <= 105
1 <= m <= 105
1 <= packages[i] <= 105
1 <= boxes[j].length <= 105
1 <= boxes[j][k] <= 105
sum(boxes[j].length) <= 105
boxes[j] 中的元素 互不相同 。
'''
from bisect import bisect_right
import itertools
from math import inf
from typing import List
'''
[TOC]

# 思路
二分查找 排序 前缀和

# 解题方法
1. 排序packages，然后计算它的前缀和数组pres
2. 遍历boxes，对于每个供应商的所有箱子boxes[i]，也进行排序
3. 遍历boxes[i]，对于每个箱子boxes[i][j]，packages中所有比它小的都可以放到它内部，可以使用二分查找进行查找，然后用前缀和数组计算浪费的空间

# 复杂度
- 时间复杂度: 
> $O(nlog(n)+mlog(m)+m*log(n))$ 

- 空间复杂度: 
> $O(n)$
'''


class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        packages.sort()
        pres = list(itertools.accumulate(packages))  # 计算前缀和
        ans, n = inf, len(packages)
        for bs in boxes:
            bs.sort()
            if bs[-1] < packages[-1]:  # 该供应商最大的箱子放不下最大的包裹，中止当前供应商的计算
                continue
            left, space = 0, 0  # left记录未被放入箱子的包裹索引，space为当前供应商浪费的空间
            for box in bs:
                i = bisect_right(packages, box, left)
                if i > left:  # 当前未放入箱子的包裹可以放入box
                    space += (i - left) * box - (pres[i - 1] - pres[left - 1] if left else pres[i - 1])
                    left = i
                if i == n:  # 已经把所有包裹放入，退出
                    break
            ans = min(ans, space)
        return ans % (10**9 + 7) if ans != inf else -1


s = Solution()
assert s.minWastedSpace(packages=[3, 5, 8, 10, 11, 12], boxes=[[12], [11, 9], [10, 5, 14]]) == 9
assert s.minWastedSpace(packages=[2, 3, 5], boxes=[[4, 8], [2, 8]]) == 6
assert s.minWastedSpace(packages=[2, 3, 5], boxes=[[1, 4], [2, 3], [3, 4]]) == -1
