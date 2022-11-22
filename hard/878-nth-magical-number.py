'''
878. 第 N 个神奇数字
困难
122
相关企业
一个正整数如果能被 a 或 b 整除，那么它是神奇的。

给定三个整数 n , a , b ，返回第 n 个神奇的数字。因为答案可能很大，所以返回答案 对 109 + 7 取模 后的值。

 

示例 1：

输入：n = 1, a = 2, b = 3
输出：2
示例 2：

输入：n = 4, a = 2, b = 3
输出：6
 

提示：

1 <= n <= 109
2 <= a, b <= 4 * 104
'''
import math
'''
[TOC]

# 思路
二分查找

# 解题方法
设第n个数为x，它的取值范围最大值为min(a,b)*n，最小值为n，
它内部包含的a的个数为x/a，b的个数为x/b，设lcmAB为a、b的最小公倍数，
x/a+x/b-x/lcmAB即为x的序号，如果它超过n，需要减小，如果它小于n需要增大。

根据上面的性质，可以用二分查找。

# 复杂度
- 时间复杂度: 
> $O(log(min(a,b)*n))$ 

- 空间复杂度: 
> $O(1)$
'''


class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        low, high = n, min(a, b) * n
        lcmAB = math.lcm(a, b)
        while low < high:
            x = (low + high) // 2
            no = x // a + x // b - x // lcmAB
            if no < n:
                low = x + 1
            else:
                high = x
        return low % (10**9 + 7)


s = Solution()
assert s.nthMagicalNumber(5, 2, 4) == 10
assert s.nthMagicalNumber(n=1, a=2, b=3) == 2
assert s.nthMagicalNumber(n=4, a=2, b=3) == 6
