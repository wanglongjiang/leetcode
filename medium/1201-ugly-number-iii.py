'''
1201. 丑数 III

给你四个整数：n 、a 、b 、c ，请你设计一个算法来找出第 n 个丑数。

丑数是可以被 a 或 b 或 c 整除的 正整数 。

示例 1：

输入：n = 3, a = 2, b = 3, c = 5
输出：4
解释：丑数序列为 2, 3, 4, 5, 6, 8, 9, 10... 其中第 3 个是 4。
示例 2：

输入：n = 4, a = 2, b = 3, c = 4
输出：6
解释：丑数序列为 2, 3, 4, 6, 8, 9, 10, 12... 其中第 4 个是 6。
示例 3：

输入：n = 5, a = 2, b = 11, c = 13
输出：10
解释：丑数序列为 2, 4, 6, 8, 10, 11, 12, 13... 其中第 5 个是 10。
示例 4：

输入：n = 1000000000, a = 2, b = 217983653, c = 336916467
输出：1999999984
 

提示：

1 <= n, a, b, c <= 10^9
1 <= a * b * c <= 10^18
本题结果在 [1, 2 * 10^9] 的范围内

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/ugly-number-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
思路：二分查找 数学
设一个数字x，小于等于x的丑数个数是：
    x//a+x//b+x//c- x//lcm(a,b) - x//lcm(b,c) - x//lcm(a,c) + x // lcm(a, b, c)
其中lcm为最小公倍数。上面公式中的前半部分“x//a+x//b+x//c”比较容易理解，就是x中a,b,c的倍数之和。
然后，对于a,b,c的最小公倍数“x//lcm(a,b)  x//lcm(b,c)  x//lcm(a,c)”，因为计算a,b,c的倍数时已经统计过一次，此时需要减掉
最后，lcm(a, b, c)是3个数的最小公倍数，第2步减去的2个数的公倍数还可能会重复减，此时需要再加上。

知道了任意一个数字x中丑数的个数，已知x的上下界为[1,2*10^9]，那么可以用二分查找了。

时间复杂度：O(log(2*10^9))
空间复杂度：O(1)
'''

from math import lcm


class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        l, r = 1, 2 * 10**9
        ans = 0
        while l <= r:
            x = (l + r) // 2
            count = x // a + x // b + x // c - x // lcm(a, b) - x // lcm(a, c) - x // lcm(b, c) + x // lcm(a, b, c)  # 计算小于等于x的丑数的个数
            if count >= n:
                ans = x
                r = x - 1
            else:
                l = x + 1
        return ans


# 6 1 2 3,
s = Solution()
print(s.nthUglyNumber(25, 2, 4, 7))
print(s.nthUglyNumber(6, 2, 1, 3))
print(s.nthUglyNumber(n=4, a=2, b=3, c=4))
print(s.nthUglyNumber(n=5, a=2, b=11, c=13))
print(s.nthUglyNumber(n=3, a=2, b=3, c=5))
print(s.nthUglyNumber(n=1000000000, a=2, b=217983653, c=336916467))
