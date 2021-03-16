'''
加油站
在一条环路上有 N 个加油站，其中第 i 个加油站有汽油 gas[i] 升。

你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。你从其中的一个加油站出发，开始时油箱为空。

如果你可以绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1。

说明: 

如果题目有解，该答案即为唯一答案。
输入数组均为非空数组，且长度相同。
输入数组中的元素均为非负数。
'''
from typing import List
'''
思路1，暴力检查法。
gas[i]-cost[i]得到剩余汽油的数组remainder，
尝试从任意remainder[i]>=0的位置开始向前累积sumGas，如果中间出现sumGas<0，则从i开始无法绕路一周。
    如果能找到sumGas始终>=0，则返回该编号，
    如果遍历所有位置未找到，则返回-1
时间复杂度：O(n*n)
空间复杂度：O(n)
思路2，滑动窗口。
    第0个元素开始，找到第1个>=0的坐标left，right指针向后滑动，sumGas开始累积
    如果出现<0，从left到right这段坐标都不能作为起点，left从right开始定位下一个>=0的。
    left如果回到坐标0，说明未找到起点，返回-1。
时间复杂度:O(n)
空间复杂度:O(1)
'''


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        left, right = 0, 0
        while True:
            while gas[left] - cost[left] < 0:  # 找到1个可以到达下一加油站的站点
                left += 1
                if left == n:  # left回到起点未找到可以到达下一加油站的地点，说明找不到
                    return -1
            right = left
            sumGas = gas[right] - cost[right]
            while sumGas >= 0:  # 油量低于0 或者 right回到left处 都需要中止
                right += 1
                if right == n:
                    right = 0
                if right == left:
                    break
                sumGas += gas[right] - cost[right]
            # 油量不足，left直接定位到right
            if sumGas < 0:
                if right < left:  # 如果right在left左边，说明找不到可以绕一圈的加油站
                    return -1
                left = right
                continue
            if left == right:  # right回到left处，说明已绕了一圈，需要中止运行，返回left指针
                return left


s = Solution()
print(s.canCompleteCircuit(gas=[2, 3, 4], cost=[3, 4, 3]))
print(s.canCompleteCircuit(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2]))
