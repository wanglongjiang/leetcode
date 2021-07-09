'''
面试题 17.10. 主要元素
数组中占比超过一半的元素称之为主要元素。给定一个整数数组，找到它的主要元素。若没有，返回-1。

示例 1：

输入：[1,2,5,9,5,9,5,5,5]
输出：5
 

示例 2：

输入：[3,2]
输出：-1
 

示例 3：

输入：[2,2,1,1,1,2,2]
输出：2
 

说明：
你有办法在时间复杂度为 O(N)，空间复杂度为 O(1) 内完成吗？
'''
from typing import List
'''
思路：摩尔投票

用1个变量candidate记录当前候选数字，用1个变量count记录出现次数
> 当nums[i]与candidate相同时，count+1
> 当nums[i]与candidate不同时，如果count为0，将candidate设置为nums[i]，如果count>0，将count-1

如果有一个数超过一半，留到最后的就是这个数
但如果没有超过一半的数，需要再遍历一次，验证这个数字是否超过了一半

注意：本题与主站 169 题类似：https://leetcode-cn.com/problems/majority-element/

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate if nums.count(candidate) > len(nums) // 2 else -1


s = Solution()
print(s.majorityElement([1, 2, 3]))
