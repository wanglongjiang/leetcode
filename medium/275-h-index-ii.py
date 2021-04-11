'''
H 指数 II
给定一位研究者论文被引用次数的数组（被引用次数是非负整数），数组已经按照 升序排列 。编写一个方法，计算出研究者的 h 指数。

h 指数的定义: “h 代表“高引用次数”（high citations），一名科研人员的 h 指数是指他（她）的 （N 篇论文中）
总共有 h 篇论文分别被引用了至少 h 次。（其余的 N - h 篇论文每篇被引用次数不多于 h 次。）"
进阶：

这是 H 指数 的延伸题目，本题中的 citations 数组是保证有序的。
你可以优化你的算法到对数时间复杂度吗？
'''
from typing import List
'''
思路：二分查找。
设mid=(left+right)/2，如果有:
    (n-mid)=nums[mid]，说明h指数就是nums[mid]
    (n-mid)>nums[mid]，说明有更大的h指数，需要在mid..right区间继续查找
    (n-mid)<nums[mid]，说明h指数更小，需要在left..mid区间查找
时间复杂度：O(logn)
空间复杂度：O(1)
'''


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left, right, n = 0, len(citations), len(citations)
        h = 0
        while left < right:
            mid = (left + right) // 2
            if n - mid == citations[mid]:
                return citations[mid]
            elif n - mid > citations[mid]:
                h = max(h, citations[mid])  # h指数>=当前引用树
                left = mid + 1
            else:
                h = n - mid  # h指数至少>= n-mid，需要记录下来
                right = mid
        return min(h, n)


s = Solution()
print(s.hIndex([0, 0, 4, 4]))
print(s.hIndex([1, 1, 3]))
print(s.hIndex([0]))
print(s.hIndex([1, 2]))
print(s.hIndex([2]))
print(s.hIndex([100]))
print(s.hIndex([0, 1, 3, 5, 6]))
