'''
通过指令创建有序数组
给你一个整数数组 instructions ，你需要根据 instructions 中的元素创建一个有序数组。一开始你有一个空的数组 nums ，
你需要 从左到右 遍历 instructions 中的元素，将它们依次插入 nums 数组中。每一次插入操作的 代价 是以下两者的 较小值 ：

nums 中 严格小于  instructions[i] 的数字数目。
nums 中 严格大于  instructions[i] 的数字数目。
比方说，如果要将 3 插入到 nums = [1,2,3,5] ，那么插入操作的 代价 为 min(2, 1) (元素 1 和  2 小于 3 ，元素 5 大于 3 ），
插入后 nums 变成 [1,2,3,3,5] 。

请你返回将 instructions 中所有元素依次插入 nums 后的 总最小代价 。由于答案会很大，请将它对 10^9 + 7 取余 后返回。

示例 1：

输入：instructions = [1,5,6,2]
输出：1
解释：一开始 nums = [] 。
插入 1 ，代价为 min(0, 0) = 0 ，现在 nums = [1] 。
插入 5 ，代价为 min(1, 0) = 0 ，现在 nums = [1,5] 。
插入 6 ，代价为 min(2, 0) = 0 ，现在 nums = [1,5,6] 。
插入 2 ，代价为 min(1, 2) = 1 ，现在 nums = [1,2,5,6] 。
总代价为 0 + 0 + 0 + 1 = 1 。

示例 2:

输入：instructions = [1,2,3,6,5,4]
输出：3
解释：一开始 nums = [] 。
插入 1 ，代价为 min(0, 0) = 0 ，现在 nums = [1] 。
插入 2 ，代价为 min(1, 0) = 0 ，现在 nums = [1,2] 。
插入 3 ，代价为 min(2, 0) = 0 ，现在 nums = [1,2,3] 。
插入 6 ，代价为 min(3, 0) = 0 ，现在 nums = [1,2,3,6] 。
插入 5 ，代价为 min(3, 1) = 1 ，现在 nums = [1,2,3,5,6] 。
插入 4 ，代价为 min(3, 2) = 2 ，现在 nums = [1,2,3,4,5,6] 。
总代价为 0 + 0 + 0 + 0 + 1 + 2 = 3 。


提示：

1 <= instructions.length <= 10^5
1 <= instructions[i] <= 10^5
'''
from typing import List
'''
思路：树状数组
从题目可以看出，每次都查找之前的数据形成的数组里面大于当前值的个数great，小于当前值的个数less
插入一次数据的代价为min(great, less)
可以使用树状数组，树状数组会记录前缀和，通过前缀和，可以很容易的计算出great和less的数值
时间复杂度：O(nlogn)，遍历数组，对于每个元素都要查询、更新树状数组；树状数组的单次更新、查询的时间复杂度都是O(logn)
空间复杂度：O(n)
'''


class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        n = max(instructions)
        c = [0] * (n + 1)

        def lowbit(x):
            return x & -x

        # 更新计数
        def update(i):
            while i <= n:
                c[i] += 1
                i += lowbit(i)

        # 获取大于等i的数量
        def get(i):
            res = 0
            while i > 0:
                res += c[i]
                i -= lowbit(i)
            return res

        ans = 0
        for val in instructions:  # 遍历数组，查询小于当前值，大于当前元素的数量
            less = get(val - 1)
            great = get(n) - get(val)
            ans += min(less, great)
            update(val)
        return ans % (10**9 + 7)


s = Solution()
print(s.createSortedArray([1, 2, 3, 6, 5, 4]))
print(s.createSortedArray([1, 5, 6, 2]))
print(s.createSortedArray([1, 3, 3, 3, 2, 4, 2, 1, 2]))
