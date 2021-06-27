'''
面试题 08.13. 堆箱子
堆箱子。给你一堆n个箱子，箱子宽 wi、深 di、高 hi。箱子不能翻转，将箱子堆起来时，下面箱子的宽度、高度和深度必须大于上面的箱子。
实现一种方法，搭出最高的一堆箱子。箱堆的高度为每个箱子高度的总和。

输入使用数组[wi, di, hi]表示每个箱子。

示例1:

 输入：box = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
 输出：6
示例2:

 输入：box = [[1, 1, 1], [2, 3, 4], [2, 6, 7], [3, 4, 5]]
 输出：10
提示:

箱子的数目不大于3000个。
'''
from typing import List
'''
思路：排序 动态规划
首先对箱子进行排序按照box[i][0]，小的在前面
设动态规划数组dp[n]，对于dp[i]意思是第i个箱子能达到的最大高度
状态转移函数为
dp[i] = max(box[2]+dp[j]), 其中j= 0..i-1，且box[i][0..2]均大于box[j][0..2]

时间复杂度：O(n^2)
空间复杂度：O(n)
'''


class Solution:
    def pileBox(self, box: List[List[int]]) -> int:
        n = len(box)
        box.sort(key=lambda b: b[0])  # 按照一个维度进行排序
        dp = list(map(lambda b: b[2], box))  # 默认值为1个箱子的高度
        ans = dp[0]
        for i in range(1, n):
            for j in range(i):
                if box[i][0] > box[j][0] and box[i][1] > box[j][1] and box[i][2] > box[j][2]:
                    dp[i] = max(dp[i], box[i][2] + dp[j])
            ans = max(ans, dp[i])
        return ans


s = Solution()
print(s.pileBox([[1, 1, 1], [2, 2, 2], [3, 3, 3]]))
print(s.pileBox([[1, 1, 1], [2, 3, 4], [2, 6, 7], [3, 4, 5]]))
