'''
2106. 摘水果
困难
38
相关企业
在一个无限的 x 坐标轴上，有许多水果分布在其中某些位置。给你一个二维整数数组 fruits ，
其中 fruits[i] = [positioni, amounti] 表示共有 amounti 个水果放置在 positioni 上。
fruits 已经按 positioni 升序排列 ，每个 positioni 互不相同 。

另给你两个整数 startPos 和 k 。最初，你位于 startPos 。从任何位置，你可以选择 向左或者向右 走。
在 x 轴上每移动 一个单位 ，就记作 一步 。你总共可以走 最多 k 步。你每达到一个位置，都会摘掉全部的水果，水果也将从该位置消失（不会再生）。

返回你可以摘到水果的 最大总数 。

 

示例 1：


输入：fruits = [[2,8],[6,3],[8,6]], startPos = 5, k = 4
输出：9
解释：
最佳路线为：
- 向右移动到位置 6 ，摘到 3 个水果
- 向右移动到位置 8 ，摘到 6 个水果
移动 3 步，共摘到 3 + 6 = 9 个水果
示例 2：


输入：fruits = [[0,9],[4,1],[5,7],[6,2],[7,4],[10,9]], startPos = 5, k = 4
输出：14
解释：
可以移动最多 k = 4 步，所以无法到达位置 0 和位置 10 。
最佳路线为：
- 在初始位置 5 ，摘到 7 个水果
- 向左移动到位置 4 ，摘到 1 个水果
- 向右移动到位置 6 ，摘到 2 个水果
- 向右移动到位置 7 ，摘到 4 个水果
移动 1 + 3 = 4 步，共摘到 7 + 1 + 2 + 4 = 14 个水果
示例 3：


输入：fruits = [[0,3],[6,4],[8,5]], startPos = 3, k = 2
输出：0
解释：
最多可以移动 k = 2 步，无法到达任一有水果的地方
 

提示：

1 <= fruits.length <= 105
fruits[i].length == 2
0 <= startPos, positioni <= 2 * 105
对于任意 i > 0 ，positioni-1 < positioni 均成立（下标从 0 开始计数）
1 <= amounti <= 104
0 <= k <= 2 * 105
'''
from bisect import bisect_left
from typing import List
'''
[TOC]

# 思路
前缀和

# 解题方法
这个人可以向左走k步，或者先向左走a步，然后掉头，最终向右走k-2a步，反过来也可以

那么可以遍历这些走法，找到水果的和最大的。

因为k最大为2*10^5，所以为了在每种走法中用O(1)时间复杂度计算出此次能摘多少水果，需要以startPos为中心，计算2边的前缀和

# 复杂度
- 时间复杂度: 
> $O(k)$ 

- 空间复杂度: 
> $O(k)$
'''


class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        leftPres, rightPres = [0] * (k + 1), [0] * (k + 1)  # 两个前缀和数组
        mid = bisect_left(fruits, startPos, key=lambda f: f[0])  # 找到所在位置
        leftIdx, rightIdx = mid - 1, mid  # fruits的指针
        if mid < len(fruits):
            if fruits[mid][0] == startPos:  # 初始位置有水果，前缀和第0个初始值为该位置水果数量
                rightPres[0] = leftPres[0] = fruits[mid][1]
                rightIdx = mid + 1  # 该处水果用掉指针+1
        # 计算前缀和
        for i in range(1, k + 1):
            leftPres[i] = leftPres[i - 1]
            if leftIdx >= 0 and fruits[leftIdx][0] == startPos - i:  # 向左走i步，当前位置有水果，累计
                leftPres[i] += fruits[leftIdx][1]
                leftIdx -= 1
            rightPres[i] = rightPres[i - 1]
            if rightIdx < len(fruits) and fruits[rightIdx][0] == startPos + i:  # 向右走i步，当前位置有水果，累计
                rightPres[i] += fruits[rightIdx][1]
                rightIdx += 1
        ans = max(leftPres[k], rightPres[k])  # 统计向左或向右走k步，能够获取的水果数
        for i in range(1, k // 2 + 1):  # 向左、右走i步后，再掉头向另外一个方向走，所以i的上限是k/2
            # leftPres[i] + rightPres[k - 2 * i] - leftPres[0] 意思是向左走i步，掉头向右走k-2i步，如果startPos有水果，需要减掉
            ans = max(ans, leftPres[i] + rightPres[k - 2 * i] - leftPres[0], rightPres[i] + leftPres[k - 2 * i] - leftPres[0])
        return ans


s = Solution()
assert s.maxTotalFruits(fruits=[[0, 9], [4, 1], [5, 7], [6, 2], [7, 4], [10, 9]], startPos=5, k=4) == 14
assert s.maxTotalFruits(fruits=[[2, 8], [6, 3], [8, 6]], startPos=5, k=4) == 9
assert s.maxTotalFruits(fruits=[[0, 3], [6, 4], [8, 5]], startPos=3, k=2) == 0
