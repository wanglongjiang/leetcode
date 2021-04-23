'''
面试题 16.10. 生存人数
给定 N 个人的出生年份和死亡年份，第 i 个人的出生年份为 birth[i]，死亡年份为 death[i]，
实现一个方法以计算生存人数最多的年份。

你可以假设所有人都出生于 1900 年至 2000 年（含 1900 和 2000 ）之间。如果一个人在某一年的任意时期处于生存状态，
那么他应该被纳入那一年的统计中。例如，生于 1908 年、死于 1909 年的人应当被列入 1908 年和 1909 年的计数。

如果有多个年份生存人数相同且均为最大值，输出其中最小的年份。

提示：

0 < birth.length == death.length <= 10000
birth[i] <= death[i]
'''
from typing import List
'''
思路：差分数组
设置1个101大小的数组第0个元素代表1900年的人数
出生的年份+1，死亡的年份的下一年-1

时间复杂度：O(n+100)
空间复杂度：O(100)
'''


class Solution:
    def maxAliveYear(self, birth: List[int], death: List[int]) -> int:
        diff = [0] * 102
        # 计算差分数组
        for b, d in zip(birth, death):
            diff[b - 1900] += 1
            diff[d - 1900 + 1] -= 1
        count = [0] * 102
        count[0] = diff[0]
        maxnum = 0
        # 合计没年的人口数
        for i in range(1, 102):
            count[i] = count[i - 1] + diff[i]
            maxnum = max(maxnum, count[i])
        # 找到年份最小，人口最多的年份
        for i in range(101):
            if maxnum == count[i]:
                return 1900 + i


s = Solution()
print(s.maxAliveYear(birth=[1900, 1901, 1950], death=[1948, 1951, 2000]))
