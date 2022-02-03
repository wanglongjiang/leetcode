'''
1414. 和为 K 的最少斐波那契数字数目
给你数字 k ，请你返回和为 k 的斐波那契数字的最少数目，其中，每个斐波那契数字都可以被使用多次。

斐波那契数字定义为：

F1 = 1
F2 = 1
Fn = Fn-1 + Fn-2 ， 其中 n > 2 。
数据保证对于给定的 k ，一定能找到可行解。

 

示例 1：

输入：k = 7
输出：2 
解释：斐波那契数字为：1，1，2，3，5，8，13，……
对于 k = 7 ，我们可以得到 2 + 5 = 7 。
示例 2：

输入：k = 10
输出：2 
解释：对于 k = 10 ，我们可以得到 2 + 8 = 10 。
示例 3：

输入：k = 19
输出：3 
解释：对于 k = 19 ，我们可以得到 1 + 5 + 13 = 19 。
 

提示：

1 <= k <= 10^9
'''
import bisect
'''
思路：贪心 二分查找
1. 生成所有小于等于k的斐波那契数列，保存到数组中
2. k减去数组中小于等于k的最大数字
3. 重复上面的2.直至k变为0

时间复杂度：O(n),feb(n)<=k
空间复杂度：O(n)
'''


class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        feb = [1, 1]
        while feb[-1] <= k:
            feb.append(feb[-1] + feb[-2])
        ans = 0
        while k:
            k -= feb[bisect.bisect_right(feb, k) - 1]
            ans += 1
        return ans


s = Solution()
print(s.findMinFibonacciNumbers(7))
print(s.findMinFibonacciNumbers(10))
print(s.findMinFibonacciNumbers(19))
