'''
面试题 16.17. 连续数列
给定一个整数数组，找出总和最大的连续数列，并返回总和。

示例：

输入： [-2,1,-3,4,-1,2,1,-5,4]
输出： 6
解释： 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶：

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
'''
from typing import List
'''
思路：滑动窗口 贪心算法
设left,right指针，初始都指向最左边，2个指针构成滑动窗口
> 如果窗口内的和<=0，向右移动left指针，缩小窗口大小
> 如果窗口内的和>0，向右移动right指针，扩大窗口大小
另外设一个变量ans，记录滑动窗口内和的大小
算法成立的理由分析：如果和<=0，说明窗口内有负数，需要将负数移出范围；如果和>0，向右扩大窗口的过程中，只要和>0，后面就有可能累计更大的和。

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, 1
        ans, total = nums[0], nums[0]
        while right < n:
            if total > 0 and right < n:
                total += nums[right]
                right += 1
            elif total <= 0 and left < right - 1:
                total -= nums[left]
                left += 1
            else:
                if right < n:
                    total = nums[right]
                    left = right
                    right += 1
            ans = max(ans, total)
        return ans
