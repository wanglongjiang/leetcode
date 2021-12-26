'''
阶乘后的零
给定一个整数 n，返回 n! 结果尾数中零的数量。

示例 1:

输入: 3
输出: 0
解释: 3! = 6, 尾数中没有零。
示例 2:

输入: 5
输出: 1
解释: 5! = 120, 尾数中有 1 个零.
说明: 你算法的时间复杂度应为 O(log n) 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/factorial-trailing-zeroes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
思路：数学
每位数上，如果超过5则会产生1个零。
比如5会产生1个0，10会产生2个0，15会产生3个0...
迭代除以0，累加起来就是0的个数


时间复杂度：O($log^n$)
空间复杂度：O(1)
'''


class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        while n >= 5:
            n, r = divmod(n, 5)
            ans += n
        return ans


s = Solution()
print(s.trailingZeroes(5))
print(s.trailingZeroes(10))
print(s.trailingZeroes(15))
print(s.trailingZeroes(20))
print(s.trailingZeroes(25))
