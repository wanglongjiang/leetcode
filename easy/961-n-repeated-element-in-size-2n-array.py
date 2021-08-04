'''
重复 N 次的元素
在大小为 2N 的数组 A 中有 N+1 个不同的元素，其中有一个元素重复了 N 次。

返回重复了 N 次的那个元素。

 

示例 1：

输入：[1,2,3,3]
输出：3
示例 2：

输入：[2,1,2,5,3,2]
输出：2
示例 3：

输入：[5,1,5,2,5,3,5,4]
输出：5
 

提示：

4 <= A.length <= 10000
0 <= A[i] < 10000
A.length 为偶数

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/n-repeated-element-in-size-2n-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
'''
思路：空间复杂度为O(1)的摩尔投票
1. 首先判断前3个数字里面有没有重复出现的，如果有，这个数字就是结果。
2. 如果前3个数字里面没有重复的，扣除这3个，剩下的元素中，重复元素肯定超过了一半，剩下的元素可以使用摩尔投票法找到重复的。
> 摩尔投票法的思路：设2个变量count和candidate，相同的数字count+1，不同的数字count-1，当count=0时更换candidate，
> 因为众数>n/2，所以剩到最后的就是重复元素。

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        # 首先判断前3个数有没有重复的
        if nums[0] == nums[1]:
            return nums[0]
        if nums[0] == nums[2]:
            return nums[0]
        if nums[1] == nums[2]:
            return nums[1]
        # 剩下的元素用摩尔投票找到众数
        candidate = None
        count = 0
        for i in range(3, len(nums)):
            if count == 0:
                candidate = nums[i]
            if nums[i] == candidate:
                count += 1
            else:
                count -= 1
        return candidate
