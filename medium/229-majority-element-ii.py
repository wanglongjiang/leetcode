'''
求众数 II
给定一个大小为 n 的整数数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。

进阶：尝试设计时间复杂度为 O(n)、空间复杂度为 O(1)的算法解决此问题。
'''
from typing import List
from collections import defaultdict
'''
一题三解

思路1，排序
排序后，遍历数组，计算相同元素的个数
时间复杂度：O(nlogn)
空间复杂度：O(1)

思路2，哈希
用哈希表统计所有元素的个数
时间复杂度：O(n)
空间复杂度：O(n)

思路3，快速选择
用快速选择的思路，将子数组划分成>pivot =pivot <pivot 3部分。
如果=pivot的部分长度>n/3，则需要将pivot加入结果，否则丢弃=pivot部分
如果>pivot或<pivot部分长度<n/3，则丢弃，否则将其递归快速选择
时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    # 思路1，排序
    def majorityElement1(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = []
        i, n, targetLen = 0, len(nums), len(nums) // 3
        while i < n:
            j = i
            while j < n and nums[i] == nums[j]:
                j += 1
            if j - i > targetLen:
                ans.append(nums[i])
            i = j
        return ans

    # 思路2，哈希
    def majorityElement2(self, nums: List[int]) -> List[int]:
        ans, n = set(), len(nums) // 3
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] += 1
            if hashmap[num] > n:
                ans.add(num)
        return list(ans)

    # 思路3，快速选择
    def majorityElement(self, nums: List[int]) -> List[int]:
        targetLen = len(nums) // 3
        ans = []

        def quick(lo, hi):
            lt, i, gt = lo, lo + 1, hi
            while i <= gt:
                if nums[i] < nums[lt]:
                    nums[i], nums[lt] = nums[lt], nums[i]
                    i += 1
                    lt += 1
                elif nums[i] > nums[lt]:
                    nums[i], nums[gt] = nums[gt], nums[i]
                    gt -= 1
                else:
                    i += 1
            if gt - lt + 1 > targetLen:
                ans.append(nums[lt])
            if lt - lo > targetLen:
                quick(lo, lt - 1)
            if hi - gt > targetLen:
                quick(gt + 1, hi)

        quick(0, len(nums) - 1)
        return ans


s = Solution()
print(s.majorityElement([2, 2]))
