'''
2466. 统计构造好字符串的方案数
中等
9
相关企业
给你整数 zero ，one ，low 和 high ，我们从空字符串开始构造一个字符串，每一步执行下面操作中的一种：

将 '0' 在字符串末尾添加 zero  次。
将 '1' 在字符串末尾添加 one 次。
以上操作可以执行任意次。

如果通过以上过程得到一个 长度 在 low 和 high 之间（包含上下边界）的字符串，那么这个字符串我们称为 好 字符串。

请你返回满足以上要求的 不同 好字符串数目。由于答案可能很大，请将结果对 109 + 7 取余 后返回。

 

示例 1：

输入：low = 3, high = 3, zero = 1, one = 1
输出：8
解释：
一个可能的好字符串是 "011" 。
可以这样构造得到："" -> "0" -> "01" -> "011" 。
从 "000" 到 "111" 之间所有的二进制字符串都是好字符串。
示例 2：

输入：low = 2, high = 3, zero = 1, one = 2
输出：5
解释：好字符串为 "00" ，"11" ，"000" ，"110" 和 "011" 。
 

提示：

1 <= low <= high <= 105
1 <= zero, one <= low
'''
'''
[TOC]

# 思路
动态规划

# 解题方法
> 设数组dp[high+1]，dp[i]的意思是长度为i的字符的构造方法
> 状态转移方程为：dp[i] = dp[i-one]+dp[i-zero]
> 方程的意思是长度为i的字符串，可以由长度为i-one的字符串+one个1构成，也可以由长度为i-zero的字符串+zero个0构成。
> 结果为sum(dp[low..hight])


# 复杂度
- 时间复杂度: 
> $O(n)$

- 空间复杂度: 
> $O(n)$
'''


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        m = 10**9 + 7
        dp = [0] * (high + 1)
        dp[one] += 1
        dp[zero] += 1
        for i in range(min(one, zero) + 1, high + 1):
            dp[i] = (dp[i] + dp[i - one] + dp[i - zero]) % m
        return sum(dp[low:high + 1]) % m


s = Solution()
assert s.countGoodStrings(low=2, high=3, zero=1, one=2) == 5
assert s.countGoodStrings(low=3, high=3, zero=1, one=1) == 8
