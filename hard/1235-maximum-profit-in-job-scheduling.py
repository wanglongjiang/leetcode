'''
规划兼职工作

你打算利用空闲时间来做兼职工作赚些零花钱。

这里有 n 份兼职工作，每份工作预计从 startTime[i] 开始到 endTime[i] 结束，报酬为 profit[i]。

给你一份兼职工作表，包含开始时间 startTime，结束时间 endTime 和预计报酬 profit 三个数组，请你计算并返回可以获得的最大报酬。

注意，时间上出现重叠的 2 份工作不能同时进行。

如果你选择的工作在时间 X 结束，那么你可以立刻进行在时间 X 开始的下一份工作。

 

示例 1：
输入：startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
输出：120
解释：
我们选出第 1 份和第 4 份工作，
时间范围是 [1-3]+[3-6]，共获得报酬 120 = 50 + 70。

示例 2：
输入：startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
输出：150
解释：
我们选择第 1，4，5 份工作。
共获得报酬 150 = 20 + 70 + 60。


示例 3：
输入：startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
输出：6
 

提示：

1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4
1 <= startTime[i] < endTime[i] <= 10^9
1 <= profit[i] <= 10^4
'''
from typing import List
'''
思路：动态规划
1、按照结束时间进行排序
2、设2个数组：dp为当前元素的最大利润，maxprofits为结束时间的最大利润
3、动态规划转移方程为：
    dp[0]设置为第0个元素的利润
    dp[i]为endTime[j]<startTime[i]的最大利润maxprofits[j]+profit[i]
时间复杂度：O(nlogn)，排序需要O(nlogn)，动态规划计算过程中需要二分查找，也是O(nlogn)
空间复杂度：O(n)
'''


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        import bisect
        jobs = list(zip(startTime, endTime, profit))
        jobs.sort(key=lambda job: job[1])  # 1、按照结束时间排序
        endTime = [job[1] for job in jobs]
        n = len(jobs)
        dp, maxprofit = [0] * n, [0] * n
        dp[0] = jobs[0][2]
        maxprofit[0] = dp[0]
        for i in range(1, n):
            before = bisect.bisect(endTime, jobs[i][0], lo=0, hi=i)  # 二分查找截止时间<=当前开始时间的坐标
            before -= 1
            if before >= 0:
                dp[i] = maxprofit[before] + jobs[i][2]  # 如果前面有已完成的任务，选择利润最大的任务作为前置任务
            else:
                dp[i] = jobs[i][2]  # 前面没有已完成的任务，最大利润就是任务本身
            maxprofit[i] = max(maxprofit[i - 1], dp[i])
        return maxprofit[-1]


s = Solution()
print(s.jobScheduling(startTime=[1, 2, 3, 3], endTime=[3, 4, 5, 6], profit=[50, 10, 40, 70]))
print(s.jobScheduling(startTime=[1, 2, 3, 4, 6], endTime=[3, 5, 10, 6, 9], profit=[20, 20, 100, 70, 60]))
print(s.jobScheduling(startTime=[1, 1, 1], endTime=[2, 3, 4], profit=[5, 6, 4]))
