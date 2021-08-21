'''
剑指 Offer II 004. 只出现一次的数字
给你一个整数数组 nums ，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 。请你找出并返回那个只出现了一次的元素。

 

示例 1：

输入：nums = [2,2,3,2]
输出：3
示例 2：

输入：nums = [0,1,0,1,0,1,100]
输出：100
 

提示：

1 <= nums.length <= 3 * 10^4
-231 <= nums[i] <= 231 - 1
nums 中，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次
 

进阶：你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

 

注意：本题与主站 137 题相同：https://leetcode-cn.com/problems/single-number-ii/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/WGki4K
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
'''
思路：快速选择 快排算法里面的分区。
随机从nums中选取pivot,利用快速排序算法里面的分区函数，分成2个区，<pivot的 和 >=pivot的。如果其中一个分区大小不是3的整数倍，
    说明目标元素出现在那个分区。需要继续对分区进行再分区。重复分区过程，直至有分区大小==1，则返回该分区的数。
时间复杂度：O(n)，快排的时间复杂度为O(nlogn)，这里因为每次只对一半的分区进行再分区，所以时间复杂度为O(n)
空间复杂度：O(1)

思路2：位运算
利用状态机和位运算，
one = (one^x)&~two 只保留出现一次的数
two = (two^x)&~one 只保留出现2次的数
时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    # 思路2 位运算
    def singleNumber(self, nums: List[int]) -> int:
        one, two = 0, 0
        for x in nums:
            one = (one ^ x) & ~two
            two = (two ^ x) & ~one
        return one

    # 思路1 快排算法里面的分区
    def singleNumber1(self, nums: List[int]) -> int:
        import random

        def partition(start, end):
            if end - start == 1:
                return nums[start]
            k = random.randint(start, end - 1)
            nums[start], nums[k] = nums[k], nums[start]
            pivot = nums[start]
            i, j = start, end - 1
            while i < j:  # 分成2个区
                while i < j and nums[j] >= pivot:
                    j -= 1
                nums[i] = nums[j]
                while i < j and nums[i] < pivot:
                    i += 1
                nums[j] = nums[i]
            nums[i] = pivot
            lowSize = i - start  # 小于pivot的分区大小
            if lowSize and lowSize % 3:  # 唯一数在小的分区
                return partition(start, i)
            highSize = end - i  # 大于pivot的分区大小
            if highSize and highSize % 3:  # 唯一数在大的分区
                return partition(i, end)

        return partition(0, len(nums))
