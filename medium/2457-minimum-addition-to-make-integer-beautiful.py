'''
2457. 美丽整数的最小增量
给你两个正整数 n 和 target 。

如果某个整数每一位上的数字相加小于或等于 target ，则认为这个整数是一个 美丽整数 。

找出并返回满足 n + x 是 美丽整数 的最小非负整数 x 。生成的输入保证总可以使 n 变成一个美丽整数。

 

示例 1：

输入：n = 16, target = 6
输出：4
解释：最初，n 是 16 ，且其每一位数字的和是 1 + 6 = 7 。在加 4 之后，n 变为 20 且每一位数字的和变成 2 + 0 = 2 。可以证明无法加上一个小于 4 的非负整数使 n 变成一个美丽整数。
示例 2：

输入：n = 467, target = 6
输出：33
解释：最初，n 是 467 ，且其每一位数字的和是 4 + 6 + 7 = 17 。在加 33 之后，n 变为 500 且每一位数字的和变成 5 + 0 + 0 = 5 。可以证明无法加上一个小于 33 的非负整数使 n 变成一个美丽整数。
示例 3：

输入：n = 1, target = 1
输出：0
解释：最初，n 是 1 ，且其每一位数字的和是 1 ，已经小于等于 target 。
 

提示：

1 <= n <= 1012
1 <= target <= 150
生成的输入保证总可以使 n 变成一个美丽整数。
'''
from itertools import accumulate
'''
思路：贪心 前缀和 数学
任意一个整数n，都可以通过在低位依次补上一个数，消去低位的1。
例如n=1234，加上6，消掉最低位的6，变成1240；加上66，消掉最低2位，变成1300。。。，最坏情况下，加上8766，变成10000
因此，可以从高位开始，依次累加，遇到第1个前缀和>=target，从这个位开始，需要补差到进位，这个差，即为结果。
当然还有一些特殊情况，需要特殊处理，详见代码。

时间复杂度：O(logn)
空间复杂度：O(logn)
'''


class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        pres = list(accumulate(map(int, str(n))))  # 求数字n从高到低的前缀和
        for i, pre in enumerate(pres):
            if pre < target:
                continue
            if pre == target and pres[-1] == target:  # 低位都是0，不需要补差
                return 0
            # i后面还有值，需要补差，消掉包含当前位i在内所有的低位的数值
            m = 10**(len(pres) - i)
            return m - n % m
        return 0  # 前缀和已经小于target，不需要补差消位


s = Solution()
print(s.makeIntegerBeautiful(n=16, target=6))
print(s.makeIntegerBeautiful(n=467, target=6))
print(s.makeIntegerBeautiful(n=1, target=1))
