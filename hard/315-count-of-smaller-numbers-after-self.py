'''
给定一个整数数组 nums，按要求返回一个新数组 counts。数组 counts 有该性质： counts[i] 的值是  nums[i] 右侧小于 nums[i] 的元素的数量。

提示：
0 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4

'''

from typing import List
'''
思路1，暴力搜索。
对于每个数字nums[i]，都向右搜索比它大的元素
时间复杂度：O(n^2)，结合输入的规模，达到10^10
空间复杂度：O(1)

思路2，离散化+树状数组
首先离散化数组
然后从右至左将数值更新到树状数组里面，统计<当前值i的个数
时间复杂度：O(nlogn)，排序和树状数组更新都是O(nlogn)
空间复杂度：O(n)
'''


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counts = [0] * n
        mp = {}
        # 离散化数组
        for i, v in enumerate(sorted(nums)):
            mp[v - 1] = 2 * i + 1
            mp[v] = 2 * i + 2
        c = [0] * (n + 1) * 2

        # 树状数组的函数
        def lowbit(x):
            return x & -x

        def add(x):
            while x <= 2 * n:
                c[x] += 1
                x += lowbit(x)

        def getcount(x):
            res = 0
            while x > 0:
                res += c[x]
                x -= lowbit(x)
            return res

        # 统计树状数组中<num[i]的元素个数
        for i in range(n - 1, -1, -1):
            counts[i] = getcount(mp[nums[i] - 1])
            add(mp[nums[i]])

        return counts


s = Solution()
print(s.countSmaller([-1, -2]))
print(s.countSmaller([-1, -1]))
print(s.countSmaller([5, 2, 6, 1]))
