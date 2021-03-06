'''
数位成本和为目标值的最大数字

给你一个整数数组 cost 和一个整数 target 。请你返回满足如下规则可以得到的 最大 整数：

给当前结果添加一个数位（i + 1）的成本为 cost[i] （cost 数组下标从 0 开始）。
总成本必须恰好等于 target 。
添加的数位中没有数字 0 。
由于答案可能会很大，请你以字符串形式返回。

如果按照上述要求无法得到任何整数，请你返回 "0" 。

 

示例 1：

输入：cost = [4,3,2,5,6,7,2,5,5], target = 9
输出："7772"
解释：添加数位 '7' 的成本为 2 ，添加数位 '2' 的成本为 3 。所以 "7772" 的代价为 2*3+ 3*1 = 9 。
"977" 也是满足要求的数字，但 "7772" 是较大的数字。
 数字     成本
  1  ->   4
  2  ->   3
  3  ->   2
  4  ->   5
  5  ->   6
  6  ->   7
  7  ->   2
  8  ->   5
  9  ->   5
示例 2：

输入：cost = [7,6,5,5,5,6,8,7,8], target = 12
输出："85"
解释：添加数位 '8' 的成本是 7 ，添加数位 '5' 的成本是 5 。"85" 的成本为 7 + 5 = 12 。
示例 3：

输入：cost = [2,4,6,2,4,6,4,4,4], target = 5
输出："0"
解释：总成本是 target 的条件下，无法生成任何整数。
示例 4：

输入：cost = [6,10,15,40,40,40,40,40,40], target = 47
输出："32211"
 

提示：

cost.length == 9
1 <= cost[i] <= 5000
1 <= target <= 5000
'''
from typing import List
'''
思路：背包问题 动态规划
背包容量为target，是一个完全背包问题，按照套路写出代码
状态转移方程为
dp[j] = max(dp[j], dp[j-cost[i]]+(i+1))
dp[j]为一个字符串，是成本为j时的数位成本形成的最大字符串

时间复杂度：O(target)
空间复杂度：O(target)
'''


class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        dp = [""] * (target + 1)
        for i in range(9):
            for j in range(cost[i], target + 1):
                # 下面对比2个数位的大小，用数组表示数位成本
                pre = dp[j - cost[i]]
                if j != cost[i] and len(pre) == 0:  # 如果前一个没有找到数位成本，当前也无法形成合法的
                    continue
                if len(dp[j]) <= len(pre):  # 如果长度相同，pre还会再加1位，肯定是pre+i大
                    dp[j] = str(i + 1) + pre
                elif len(dp[j]) == len(pre) + 1:  # 如果长度相差1，需要比较字符串大小
                    newstr = str(i + 1) + pre
                    dp[j] = max(dp[j], newstr)
        return dp[target] if dp[target] else '0'


s = Solution()
print(s.largestNumber(cost=[4, 3, 2, 5, 6, 7, 2, 5, 5], target=9))
print(s.largestNumber(cost=[7, 6, 5, 5, 5, 6, 8, 7, 8], target=12))
print(s.largestNumber(cost=[2, 4, 6, 2, 4, 6, 4, 4, 4], target=5))
print(s.largestNumber(cost=[6, 10, 15, 40, 40, 40, 40, 40, 40], target=47))
