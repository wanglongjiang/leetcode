'''
668. 乘法表中第k小的数
几乎每一个人都用 乘法表。但是你能在乘法表中快速找到第k小的数字吗？

给定高度m 、宽度n 的一张 m * n的乘法表，以及正整数k，你需要返回表中第k 小的数字。

例 1：

输入: m = 3, n = 3, k = 5
输出: 3
解释: 
乘法表:
1	2	3
2	4	6
3	6	9

第5小的数字是 3 (1, 2, 2, 3, 3).
例 2：

输入: m = 2, n = 3, k = 6
输出: 6
解释: 
乘法表:
1	2	3
2	4	6

第6小的数字是 6 (1, 2, 2, 3, 4, 6).
注意：

m 和 n 的范围在 [1, 30000] 之间。
k 的范围在 [1, m * n] 之间。
'''
'''
思路：二分查找
设第k个数是x，遍历每行，检查每行比x小的数。
经过观察乘法表可知，每行比x小的数的个数是min(n,x//rowNum)。
可以使用二分x，如果乘法表中大于x的数字个数<k，需要增大x；
否则缩小x。

时间复杂度：O(mlog(k))
空间复杂度：O(1)
'''


class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def getSmallCount(x):
            ans = 0
            for i in range(1, m + 1):
                ans += min(n, x // i)
            return ans

        l, r = 1, m * n
        while l < r:
            mid = (l + r) // 2
            if getSmallCount(mid) >= k:
                r = mid
            else:
                l = mid + 1
        return r
