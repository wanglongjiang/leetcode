'''
质数排列
请你帮忙给从 1 到 n 的数设计排列方案，使得所有的「质数」都应该被放在「质数索引」（索引从 1 开始）上；你需要返回可能的方案总数。

让我们一起来回顾一下「质数」：质数一定是大于 1 的，并且不能用两个小于它的正整数的乘积来表示。

由于答案可能会很大，所以请你返回答案 模 mod 10^9 + 7 之后的结果即可。

 

示例 1：

输入：n = 5
输出：12
解释：举个例子，[1,2,5,4,3] 是一个有效的排列，但 [5,2,3,4,1] 不是，因为在第二种情况里质数 5 被错误地放在索引为 1 的位置上。
示例 2：

输入：n = 100
输出：682289015
 

提示：

1 <= n <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/prime-arrangements
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
思路：数学
质数只能与质数交换位置，非质数只能与非质数交换位置
也就是答案=质数的排列数*非质数的排列数
首先用筛法求出质数的数量，然后用上面的公式计算

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        primes = [1] * (n + 1)
        primes[0], primes[1] = 0, 0
        primeCount = 0
        for i in range(2, n + 1):
            if primes[i]:
                primeCount += 1
                j = 2
                while j * i <= n:
                    primes[j * i] = 0
                    j += 1
        m = 10**9 + 7
        # 计算质数和合数的排列
        n1 = 1
        for i in range(2, primeCount + 1):
            n1 = (n1 * i) % m
        n2 = 1
        for i in range(2, n - primeCount + 1):
            n2 = (n2 * i) % m
        return (n1 * n2) % m


s = Solution()
print(s.numPrimeArrangements(5))
