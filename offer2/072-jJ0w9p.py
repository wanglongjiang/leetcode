'''
剑指 Offer II 072. 求平方根
给定一个非负整数 x ，计算并返回 x 的平方根，即实现 int sqrt(int x) 函数。

正数的平方根有两个，只输出其中的正数平方根。

如果平方根不是整数，输出只保留整数的部分，小数部分将被舍去。

 

示例 1:

输入: x = 4
输出: 2
示例 2:

输入: x = 8
输出: 2
解释: 8 的平方根是 2.82842...，由于小数部分将被舍去，所以返回 2
 

提示:

0 <= x <= 231 - 1
 

注意：本题与主站 69 题相同： https://leetcode-cn.com/problems/sqrtx/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jJ0w9p
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
解题思路1，暴力搜索，使用4则运算，从1开始搜索，直至i*i<=x and (i+1)*(i+1)>x 返回i
时间复杂度：O(求根n)
解题思路2，牛顿法，使用4则运算，每次求guess和x/guess的平均值来渐进
时间复杂度：O(log(n))
'''


class Solution:
    # 思路1
    def mySqrt1(self, x: int) -> int:
        a, b = 0, 0
        while b * b <= x:
            a = b
            b += 1
        return a

    # 思路2
    def mySqrt(self, x: int) -> int:
        guess = x
        while True:
            if guess * guess <= x:
                return guess
            guess = (x // guess + guess) >> 1
