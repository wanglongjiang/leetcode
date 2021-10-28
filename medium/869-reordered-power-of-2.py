'''
重新排序得到 2 的幂
给定正整数 N ，我们按任何顺序（包括原始顺序）将数字重新排序，注意其前导数字不能为零。

如果我们可以通过上述方式得到 2 的幂，返回 true；否则，返回 false。

 

示例 1：

输入：1
输出：true
示例 2：

输入：10
输出：false
示例 3：

输入：16
输出：true
示例 4：

输入：24
输出：false
示例 5：

输入：46
输出：true
 

提示：

1 <= N <= 10^9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reordered-power-of-2
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from functools import lru_cache
'''
思路：枚举
实际上是一个排列问题，将数字n在10进制上的各个数字进行交换，如果得到的数字是2的幂，返回true
使用回溯，对所有数字的排列进行

时间复杂度：O(logn!)，题目中给出了n的范围是1~10^9，最大是9！
空间复杂度：O(logn)，题目中给出了n的范围是1~10^9，因此递归深度是10以内
'''


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        if n & (n - 1) == 0:
            return True
        t = [0] * 11  # 存储10^0..10^10
        m = 1  # 存储数字n的位数
        t[0] = 1
        for i in range(1, 11):
            t[i] = t[i - 1] * 10
            if t[i] < n:
                m = i + 1

        # 交换n中2位数字
        def exchange(n, i, j):
            biti = (n % t[i + 1]) // t[i]
            bitj = (n % t[j + 1]) // t[j]
            if j != m or biti != 0:  # 确保最高位不能是0
                n = n - biti * t[i] - bitj * t[j] + biti * t[j] + bitj * t[i]
            return n

        # 回溯搜索
        @lru_cache
        def backtrack(n, index):
            for i in range(index + 1, m):
                newn = exchange(n, index, i)
                if newn & (newn - 1) == 0:
                    return True
                if backtrack(newn, index + 1):
                    return True
            if index + 1 < m and backtrack(n, index + 1):
                return True
            return False

        return backtrack(n, 0)


s = Solution()
print(s.reorderedPowerOf2(218))
print(s.reorderedPowerOf2(8204))
print(s.reorderedPowerOf2(46))
print(s.reorderedPowerOf2(1))
print(s.reorderedPowerOf2(10))
print(s.reorderedPowerOf2(16))
print(s.reorderedPowerOf2(24))
print(s.reorderedPowerOf2(1042))
