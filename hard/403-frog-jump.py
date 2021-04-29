'''
青蛙过河

一只青蛙想要过河。 假定河流被等分为若干个单元格，并且在每一个单元格内都有可能放有一块石子（也有可能没有）。 青蛙可以跳上石子，但是不可以跳入水中。

给你石子的位置列表 stones（用单元格序号 升序 表示）， 请判定青蛙能否成功过河（即能否在最后一步跳至最后一块石子上）。

开始时， 青蛙默认已站在第一块石子上，并可以假定它第一步只能跳跃一个单位（即只能从单元格 1 跳至单元格 2 ）。

如果青蛙上一步跳跃了 k 个单位，那么它接下来的跳跃距离只能选择为 k - 1、k 或 k + 1 个单位。 另请注意，青蛙只能向前方（终点的方向）跳跃。

提示：

2 <= stones.length <= 2000
0 <= stones[i] <= 2^31 - 1
stones[0] == 0
'''
from typing import List
'''
思路1，暴力回溯。用k到达stones[i]之后，尝试k-1,k,k+1是否能够到达一个石头，如果能，将步数和下一个石头坐标传给回溯函数。
时间复杂度：O(3^n)
空间复杂度：O(n)

思路2，动态规划。
当前为第i个石头，如果能从第i-1个石头到达，需要的步数为k1=stones[i]-stones[i-1]，那么到达stones[i-1]的步数需要有k1,k1-1,k1+1。
    同理，如果能从第i-2个石头到达，需要的步数为k2=stones[i]-stones[i-2]，那么道道stones[i-2]的步数里需要有k2,k2-1,k2+1。
可以设置一个数组jumps[]，每个元素jumps[i]为哈希表，存储跳到第i个石头的步数。
状态转移方程为：jumps[i]= if (stones[i]-stones[i-1])+0 or +1 or -1 in jumps[i-1], if (stones[i]-stones[i-2])+0 or +1 or -1 in jumps[i-2]...直至0
时间复杂度：O(n^2)，每个元素需要向前搜索i-1个元素
空间复杂度：O(n^2)，需要辅助数组jumps，jumps的每个元素为哈希表，最大为n
'''


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        jumps = [set() for _ in range(n)]
        jumps[0].add(0)  # 第0个只有0步，第1个只有等于1的时候才能从0跳到1
        maxk = 0  # 保存当前最大的步数
        for i in range(1, n):
            for j in range(i - 1, -1, -1):
                k = stones[i] - stones[j]
                if k > maxk + 1:  # 如果当前步数超过以往最大的步数+1，肯定无法从stones[j]跳到当前石头，中断循环，不需要向前搜索了。
                    break
                if k in jumps[j] or k - 1 in jumps[j] or k + 1 in jumps[j]:
                    jumps[i].add(k)
                    maxk = max(maxk, k)
        return len(jumps[n - 1]) > 0


s = Solution()
print(s.canCross(stones=[0, 1, 3, 5, 6, 8, 12, 17]))
print(s.canCross(stones=[0, 1, 2, 3, 4, 8, 9, 11]))
