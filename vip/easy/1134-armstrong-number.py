'''
1134. 阿姆斯特朗数
假设存在一个 k 位数 N，其每一位上的数字的 k 次幂的总和也是 N，那么这个数是阿姆斯特朗数。

给你一个正整数 N，让你来判定他是否是阿姆斯特朗数，是则返回 true，不是则返回 false。



示例 1：

输入：153
输出：true
示例：
153 是一个 3 位数，且 153 = 1^3 + 5^3 + 3^3。
示例 2：

输入：123
输出：false
解释：
123 是一个 3 位数，且 123 != 1^3 + 2^3 + 3^3 = 36。


提示：

1 <= N <= 10^8
'''
'''
思路：数学
遍历每一位，求其k次幂的和

时间复杂度：O(logn)
空间复杂度：O(1)
'''


class Solution:
    def isArmstrong(self, n: int) -> bool:
        num = n
        k = 0
        while num:
            num //= 10
            k += 1
        num = n
        s = 0
        while num:
            num, r = divmod(num, 10)
            s += r**k
        return s == n


s = Solution()
print(s.isArmstrong(153))
print(s.isArmstrong(123))
