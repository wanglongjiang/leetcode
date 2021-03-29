'''
平均等待时间
有一个餐厅，只有一位厨师。你有一个顾客数组 customers ，其中 customers[i] = [arrivali, timei] ：

arrivali 是第 i 位顾客到达的时间，到达时间按 非递减 顺序排列。
timei 是给第 i 位顾客做菜需要的时间。
当一位顾客到达时，他将他的订单给厨师，厨师一旦空闲的时候就开始做这位顾客的菜。每位顾客会一直等待到厨师完成他的订单。厨师同时只能做一个人的订单。厨师会严格按照 订单给他的顺序 做菜。

请你返回所有顾客需要等待的 平均 时间。与标准答案误差在 10-5 范围以内，都视为正确结果。

提示：

1 <= customers.length <= 105
1 <= arrivali, timei <= 104
arrivali <= arrivali+1
'''
from typing import List
'''
思路：动态规划。
第i个顾客的做菜完成时间为finish[i] = max(第i个顾客到达时间，第i-1个顾客做菜完成时间)+第i个顾客做菜需要时间，等待时间=finish[i] - 第i个顾客到达时间
可以优化空间使用，用1个变量finishTime 存储上一个顾客完成时间，用1个变量totalWaitTime存储总计等待时间
时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        finishTime, totalWaitTime = 0, 0
        for c in customers:
            finishTime = max(c[0], finishTime) + c[1]
            totalWaitTime += finishTime - c[0]
        return totalWaitTime / len(customers)


s = Solution()
print(s.averageWaitingTime([[1, 2], [2, 5], [4, 3]]))
print(s.averageWaitingTime([[5, 2], [5, 4], [10, 3], [20, 1]]))
