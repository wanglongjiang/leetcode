'''
面试题 16.06. 最小差
给定两个整数数组a和b，计算具有最小差绝对值的一对数值（每个数组中取一个值），并返回该对数值的差

 

示例：

输入：{1, 3, 15, 11, 2}, {23, 127, 235, 19, 8}
输出：3，即数值对(11, 8)
 

提示：

1 <= a.length, b.length <= 100000
-2147483648 <= a[i], b[i] <= 2147483647
正确结果在区间 [0, 2147483647] 内
'''
from typing import List
import bisect
'''
思路：排序 二分查找
> 1. 对数组b进行排序
> 2. 遍历数组a中每一个元素a[i]，在b中二分查找与a[i]最接近的2个数，计算其差值

时间复杂度：O(nlogn+mlogn),m为a的长度，n为b的长度
空间复杂度：O(1)
'''


class Solution:
    def smallestDifference(self, a: List[int], b: List[int]) -> int:
        n = len(b)
        b.sort()
        ans = float('inf')
        for num in a:
            idx = bisect.bisect(b, num)
            if idx == 0:
                ans = min(ans, b[idx] - num)
            elif idx == n:
                ans = min(ans, num - b[idx - 1])
            else:
                ans = min(ans, b[idx] - num)
                ans = min(ans, num - b[idx - 1])
            if ans == 0:
                break
        return ans


s = Solution()
print(s.smallestDifference([0], [2147483647]))
