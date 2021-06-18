'''
最小好进制

对于给定的整数 n, 如果n的k（k>=2）进制数的所有数位全为1，则称 k（k>=2）是 n 的一个好进制。

以字符串的形式给出 n, 以字符串的形式返回 n 的最小好进制。

 

示例 1：

输入："13"
输出："3"
解释：13 的 3 进制是 111。
示例 2：

输入："4681"
输出："8"
解释：4681 的 8 进制是 11111。
示例 3：

输入："1000000000000000000"
输出："999999999999999999"
解释：1000000000000000000 的 999999999999999999 进制是 11。
 

提示：

n的取值范围是 [3, 10^18]。
输入总是有效且没有前导 0。
'''
'''
思路：数学
k进制的1111..1=n
则n=1+k^1+k^2+k^3+...+k^(m-1)
m为1的个数，因k>=2，故m最大值=log2(num)+1,m最小值为2（n最小为3，所以最少有2个1）
可以从大到小遍历m，然后在1的个数确定的情况下二分搜索满足条件的k，k的取值范围是2至n

时间复杂度：O(logn)
空间复杂度：O(1)
'''


class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n = int(n)
        # 求m的最大值，也就是2进制下最高位的1的位数
        m = 0
        while (n >> m) > 0:
            m += 1
        for m in range(m, 1, -1):  # 从大到小遍历m可能的值，m越大1越多，k越小
            left, right = 2, n  # 二分搜索k
            while left < right:
                k = left + (right - left) // 2
                total = 0
                for i in range(m):
                    total = total * k + 1  # 求k进制下的m个1的数值
                if total == n:
                    return str(k)
                if total < n:
                    left = k + 1
                else:
                    right = k
        return str(n - 1)  # 最坏情况下的进制是n-1进制


s = Solution()
print(s.smallestGoodBase("13"))
