'''
摆动排序 II
给你一个整数数组 nums，将它重新排列成 nums[0] < nums[1] > nums[2] < nums[3]... 的顺序。

你可以假设所有输入数组都可以得到满足题目要求的结果。

 

示例 1：

输入：nums = [1,5,1,1,6,4]
输出：[1,6,1,5,1,4]
解释：[1,4,1,5,1,6] 同样是符合题目要求的结果，可以被判题程序接受。
示例 2：

输入：nums = [1,3,2,2,3,1]
输出：[2,3,1,3,1,2]
 

提示：

1 <= nums.length <= 5 * 10^4
0 <= nums[i] <= 5000
题目数据保证，对于给定的输入 nums ，总能产生满足题目要求的结果
 

进阶：你能用 O(n) 时间复杂度和 / 或原地 O(1) 额外空间来实现吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/wiggle-sort-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
import random
'''
思路：分治，快速选择
主要思路是将nums从中间分成2部分，左边的一半要全部小于右边的一半。
1. 设k=n/2，使用快速排序里面的分区方法，随机选择pivot，将nums分成<pivot和>pivot的2部分
2. 设2部分大小为lowSize和highSize，
> 如果lowSize<k，则需要继续从大于pivot的区域截取k-lowSize个元素以便将数组切分成大小2部分
> 如果lowSize>k，则需要将<pivot的部分进行切分。
> 如果lowSize==k，则数组已经切分成了大小2个区
3. 迭代执行上面的1.2.直至数组切分成2个区之后，将数组复制到辅助数组里，然后从低、高区域轮流取一个元素复制到原数组

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        n = len(nums)
        k = n // 2 + n % 2
        start, end = 0, len(nums) - 1
        lowArr = []
        while k:
            pivotIdx = random.randint(start, end)
            nums[pivotIdx], nums[start] = nums[start], nums[pivotIdx]
            pivot = nums[start]
            i, j = start, end
            while i < j:
                while i < j and nums[j] >= pivot:
                    j -= 1
                nums[i] = nums[j]
                while i < j and nums[i] < pivot:
                    i += 1
                nums[j] = nums[i]
            nums[i] = pivot
            lowSize = i - start
            if lowSize == 0 and nums[start] == nums[end]:  # 如果低区没有元素被选中
                mid = (start + end) // 2
                if nums[start] == nums[mid]:  # 子数组的开始、中间、结束全部相同，大概率是子数组全部元素都相同
                    for j in range(start + 1, end + 1):
                        if nums[start] != nums[j]:
                            break
                    else:  # 经过一次遍历，确认子数组所有元素都相同，用分治法无法再分区，数组已经按照低区、高区分好
                        while k:
                            lowArr.extend(nums[start:start + k])
                            k = 0
                        break
            if lowSize == k:  # 够了k个数，中断分区
                lowArr.extend(nums[start:i])
                break
            elif lowSize < k:  # 不够k个数，将lowSize个数加入结果，然后继续对高区进行分区
                lowArr.extend(nums[start:i])
                k -= lowSize
                start = i
            else:  # 超过k个数，将低位继续分区
                end = i - 1
        # 下面将低位、高位的数轮流取出，合并
        k = n // 2 + n % 2
        highArr = nums[k:]
        for i in range(n):
            if i % 2:
                nums[i] = highArr.pop()
            else:
                nums[i] = lowArr.pop()
        return nums


s = Solution()
print(s.wiggleSort([4, 5, 5, 5, 5, 6, 6, 6]))
print(s.wiggleSort([1, 1, 2, 1, 2, 2, 1]))
print(s.wiggleSort([1, 2, 1, 2, 1, 1, 2, 2, 1]))
print(s.wiggleSort([4, 5, 5, 6]))
print(s.wiggleSort([1, 3, 2, 2, 3, 1]))
print(s.wiggleSort([1, 5, 1, 1, 6, 4]))
