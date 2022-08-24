'''
957. N 天后的牢房
监狱中 8 间牢房排成一排，每间牢房可能被占用或空置。

每天，无论牢房是被占用或空置，都会根据以下规则进行变更：

如果一间牢房的两个相邻的房间都被占用或都是空的，那么该牢房就会被占用。
否则，它就会被空置。
注意：由于监狱中的牢房排成一行，所以行中的第一个和最后一个牢房不存在两个相邻的房间。

给你一个整数数组 cells ，用于表示牢房的初始状态：如果第 i 间牢房被占用，则 cell[i]==1，否则 cell[i]==0 。另给你一个整数 n 。

请你返回 n 天后监狱的状况（即，按上文描述进行 n 次变更）。

 

示例 1：

输入：cells = [0,1,0,1,1,0,0,1], n = 7
输出：[0,0,1,1,0,0,0,0]
解释：下表总结了监狱每天的状况：
Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
Day 7: [0, 0, 1, 1, 0, 0, 0, 0]
示例 2：

输入：cells = [1,0,0,1,0,0,1,0], n = 1000000000
输出：[0,0,1,1,1,1,1,0]
 

提示：

cells.length == 8
cells[i] 为 0 或 1
1 <= n <= 109
'''
from typing import List
'''
思路：位运算
最多有65种状态，初始状态第0位和第8位有可能为1，第1次天之后，第0位、第8位的1都会消失，剩下2~7位最多有2^6个状态变化
当某个状态再次出现时，说明状态变化进入了循环，n除以循环周期，得到余数r，第r个状态即为答案

时间复杂度：O(65)
空间复杂度：O(65)
'''


class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        status, statusSet, statusList = 0, set(), []
        for i in range(8):  # 状态压缩
            status |= cells[i] << (7 - i)
        while True:
            if status in statusSet:  # 如果状态出现重复，出现了循环，需要退出。
                break
            statusSet.add(status)  # 变化出的新状态加入list和set。
            statusList.append(status)
            oldStatus, status = status, 0
            for i in range(1, 7):
                if ((oldStatus >> (i - 1) & 1)) ^ (oldStatus >> (i + 1) & 1) == 0:  # 第i位两边都是1或都是0，需要设置为1
                    status |= 1 << i
        i = statusList.index(status)  # 找到循环开始的状态下标
        period = len(statusList) - i  # 循环周期
        status = statusList[i + (n - i) % period] if n > i else statusList[n]  # 如果n较大，n-i除以循环周期得到余数r，从i起第r个即为目标状态；假如n比较小，未进入循环，第n个状态即可
        ans = [0] * 8
        for i in range(8):  # 状态展开
            ans[i] = (status >> (7 - i)) & 1
        return ans


s = Solution()
print(s.prisonAfterNDays([1, 0, 0, 1, 0, 0, 1, 0], 1000000000) == [0, 0, 1, 1, 1, 1, 1, 0])
print(s.prisonAfterNDays([0, 1, 0, 1, 1, 0, 0, 1], 7) == [0, 0, 1, 1, 0, 0, 0, 0])
