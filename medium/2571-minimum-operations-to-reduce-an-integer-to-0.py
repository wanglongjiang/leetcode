'''
2571. 将整数减少到零需要的最少操作数
中等
18
相关企业
给你一个正整数 n ，你可以执行下述操作 任意 次：

n 加上或减去 2 的某个 幂
返回使 n 等于 0 需要执行的 最少 操作数。

如果 x == 2i 且其中 i >= 0 ，则数字 x 是 2 的幂。

 

示例 1：

输入：n = 39
输出：3
解释：我们可以执行下述操作：
- n 加上 20 = 1 ，得到 n = 40 。
- n 减去 23 = 8 ，得到 n = 32 。
- n 减去 25 = 32 ，得到 n = 0 。
可以证明使 n 等于 0 需要执行的最少操作数是 3 。
示例 2：

输入：n = 54
输出：3
解释：我们可以执行下述操作：
- n 加上 21 = 2 ，得到 n = 56 。
- n 加上 23 = 8 ，得到 n = 64 。
- n 减去 26 = 64 ，得到 n = 0 。
使 n 等于 0 需要执行的最少操作数是 3 。 
 

提示：

1 <= n <= 105
'''
'''
[TOC]

# 思路
贪心

# 解题方法
从低位开始遍历n的每一bit，如果遇到连续>=2位的1，加上1，使其进位；如果遇到不连续的1，直接消掉

# 复杂度
- 时间复杂度: 
> $O(logn)$ 

- 空间复杂度: 
> $O(1)$
'''


class Solution:
    def minOperations(self, n: int) -> int:
        ans = 0
        count = 0
        for bit in reversed(list(bin(n)[2:])):
            if bit == '1':
                count += 1
            else:
                if count >= 2:  # 遇到连续的1，需要加1次1，使其进位
                    count = 1
                    ans += 1
                elif count > 0:  # 遇到单独的1，直接消掉
                    ans += 1
                    count = 0
        if count >= 2:
            ans += 2
        elif count > 0:
            ans += 1
        return ans


s = Solution()
print(bin(54))
assert s.minOperations(54) == 3
assert s.minOperations(39) == 3
