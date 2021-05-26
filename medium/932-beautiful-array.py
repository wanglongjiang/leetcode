'''
漂亮数组
对于某些固定的 N，如果数组 A 是整数 1, 2, ..., N 组成的排列，使得：

对于每个 i < j，都不存在 k 满足 i < k < j 使得 A[k] * 2 = A[i] + A[j]。

那么数组 A 是漂亮数组。

 

给定 N，返回任意漂亮数组 A（保证存在一个）。

 

示例 1：

输入：4
输出：[2,1,4,3]
示例 2：

输入：5
输出：[3,1,2,5,4]
 

提示：

1 <= N <= 1000
'''
from typing import List
'''
思路：数学
从网上看来的思路，数组A如果是一个漂亮数组，那么A的每一个元素都变成2*A-1是漂亮数组，每个元素变成2倍，2*A也是漂亮数组，将2个新生成的数组A1+A2连结起来也是漂亮数组

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def beautifulArray(self, N: int) -> List[int]:
        ans = [1]
        while len(ans) < N:
            ans = [2 * i - 1 for i in ans] + [2 * i for i in ans]
        return [i for i in ans if i <= N]


s = Solution()
print(s.beautifulArray(4))
print(s.beautifulArray(5))
