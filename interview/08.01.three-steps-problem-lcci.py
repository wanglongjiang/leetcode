'''
面试题 08.01. 三步问题
三步问题。有个小孩正在上楼梯，楼梯有n阶台阶，小孩一次可以上1阶、2阶或3阶。实现一种方法，
计算小孩有多少种上楼梯的方式。结果可能很大，你需要对结果模1000000007。

示例1:

 输入：n = 3
 输出：4
 说明: 有四种走法
示例2:

 输入：n = 5
 输出：13
提示:

n范围在[1, 1000000]之间
'''
'''
思路：动态规划
设动态规划数组dp[n+1]，dp[i]的意思是跳到dp[i]的方法
那么状态转移函数为
dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
意思是i可以从i-1走1步，也可以从i-2走2步，还可以从i-3走3步过来。3个方式的组合。
dp[0] = 0
dp[1] = 1
dp[2] = 2
dp[3] = 4

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def waysToStep(self, n: int) -> int:
        dp = [0] * max(n + 1, 4)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        dp[3] = 4
        for i in range(4, n + 1):
            dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % 1000000007
        return dp[n]


s = Solution()
print(s.waysToStep(3))
print(s.waysToStep(4))
print(s.waysToStep(5))
