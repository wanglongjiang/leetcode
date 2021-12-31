'''
507. 完美数
对于一个 正整数，如果它和除了它自身以外的所有 正因子 之和相等，我们称它为 「完美数」。

给定一个 整数 n， 如果是完美数，返回 true，否则返回 false

 

示例 1：

输入：num = 28
输出：true
解释：28 = 1 + 2 + 4 + 7 + 14
1, 2, 4, 7, 和 14 是 28 的所有正因子。
示例 2：

输入：num = 6
输出：true
示例 3：

输入：num = 496
输出：true
示例 4：

输入：num = 8128
输出：true
示例 5：

输入：num = 2
输出：false
 

提示：

1 <= num <= 10^8
'''
'''
思路：数学
找到num的所有因数，进行累加
正因数从1到sqrt(num)即可

时间复杂度：O(sqrt(num))
空间复杂度：O(1)
'''


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        ans = 1
        for a in range(2, int(num**0.5) + 1):
            d, r = divmod(num, a)
            if r == 0:
                ans += d + a
        return ans == num


s = Solution()
print(s.checkPerfectNumber(28))
print(s.checkPerfectNumber(6))
print(s.checkPerfectNumber(496))
print(s.checkPerfectNumber(8128))
print(s.checkPerfectNumber(2))
