'''
累加数
累加数是一个字符串，组成它的数字可以形成累加序列。

一个有效的累加序列必须至少包含 3 个数。除了最开始的两个数以外，字符串中的其他数都等于它之前两个数相加的和。

给定一个只包含数字 '0'-'9' 的字符串，编写一个算法来判断给定输入是否是累加数。

说明: 累加序列里的数不会以 0 开头，所以不会出现 1, 2, 03 或者 1, 02, 3 的情况。

示例 1:

输入: "112358"
输出: true
解释: 累加序列为: 1, 1, 2, 3, 5, 8 。1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
示例 2:

输入: "199100199"
输出: true
解释: 累加序列为: 1, 99, 100, 199。1 + 99 = 100, 99 + 100 = 199
'''
'''
思路：回溯+剪枝
最外层有个循环，依次遍历从2开始的位置，将0..i切分成2个整数a、b，求出2个整数之和target
回溯确认从num[i]开始的数与target相同，然后后面与b+target相同，再次回溯

时间复杂度：O(n!)
空间复杂度：O(n)
'''


class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        def backtrack(i, b, target):
            t = str(target)
            if n - i < len(t):  # 剪枝，剩余长度不满足要求
                return False
            if n - i == len(t):  # 剩余长度与target相同，判断字符串是否相同
                return num[i:] == t
            if num[i:i + len(t)] != t:  # 开始的字符串不相同
                return False
            if num[i + len(t)] == '0':  # 剪枝，数字不能以0开头
                return False
            return backtrack(i + len(t), target, b + target)

        for i in range(2, n // 3 * 2 + 1):  # 开始的2个数字长度最多占到2/3
            if num[i] == '0' and i != 2:  # 剪枝，数字不能以0开头
                continue
            for j in range(1, i):  # 遍历长度为i的子串中所有分割点
                if num[j] == '0' and i - j > 1:  # 剪枝，数字不能以0开头
                    continue
                if num[0] == '0' and j > 1:  # 剪枝，数字不能以0开头
                    continue
                a, b = num[:j], num[j:i]
                b = int(b)
                if backtrack(i, b, int(a) + b):
                    return True
        return False


s = Solution()
print(s.isAdditiveNumber("0235813"))
print(s.isAdditiveNumber("000"))
print(s.isAdditiveNumber("101"))
print(s.isAdditiveNumber("123"))
print(s.isAdditiveNumber("112358"))
print(s.isAdditiveNumber("199100199"))
