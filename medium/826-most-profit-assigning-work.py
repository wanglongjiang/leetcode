'''
826. 安排工作以达到最大收益
有一些工作：difficulty[i] 表示第 i 个工作的难度，profit[i] 表示第 i 个工作的收益。

现在我们有一些工人。worker[i] 是第 i 个工人的能力，即该工人只能完成难度小于等于 worker[i] 的工作。

每一个工人都最多只能安排一个工作，但是一个工作可以完成多次。

举个例子，如果 3 个工人都尝试完成一份报酬为 1 的同样工作，那么总收益为3。如果一个工人不能完成任何工作，他的收益为0 。

我们能得到的最大收益是多少？



示例：

输入: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
输出: 100
解释: 工人被分配的工作难度是 [4,4,6,6] ，分别获得 [20,20,30,30] 的收益。


提示:

1 <= difficulty.length = profit.length <= 10000
1 <= worker.length <= 10000
difficulty[i], profit[i], worker[i]  的范围是 [1, 10^5]
'''
from typing import List
import bisect
'''
思路：排序 贪心 二分查找
1. 首先对工作和收益按照难度进行排序
2. 遍历所有工作收益，当前难度的工作获得的收益是小于等于当前难度的收益最大值
3. 遍历所有工人，用二分查找查找其能工作的最高工作难度，然后用同一索引得到最大收益

时间复杂度：O(nlogm+mlogm)，这里m=len(difficulty),n=len(worker)，需要对difficulty进行排序，需要mlogm时间，然后遍历所有工人，对于每个工人需要二分查找difficulty
空间复杂度：O(m)
'''


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        difficulty, profit = zip(*sorted(zip(difficulty, profit)))  # 按照工作难度进行排序
        difficulty, profit = list(difficulty), list(profit)
        maxProfit = float('-inf')
        n = len(profit)
        for i in range(n):  # 更新当前难度最大收益
            if profit[i] < maxProfit:
                profit[i] = maxProfit
            else:
                maxProfit = profit[i]
        ans = 0
        for w in worker:
            i = bisect.bisect_right(difficulty, w)  # 二分查找最难工作索引
            if i > 0:
                ans += profit[i - 1]  # 累加最大利润
        return ans


s = Solution()
print(s.maxProfitAssignment(difficulty=[2, 4, 6, 8, 10], profit=[10, 20, 30, 40, 50], worker=[4, 5, 6, 7]))
