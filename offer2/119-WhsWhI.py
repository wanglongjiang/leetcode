'''
剑指 Offer II 119. 最长连续序列
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

 

示例 1：

输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
示例 2：

输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9
 

提示：

0 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
 

进阶：可以设计并实现时间复杂度为 O(n) 的解决方案吗？

 

注意：本题与主站 128 题相同： https://leetcode-cn.com/problems/longest-consecutive-sequence/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/WhsWhI
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
'''
思路1，排序后再遍历数组，找到连续最长序列。
    时间复杂度：O(n*logn)
    空间复杂度：O(1)
思路2，哈希。
    1、第1次遍历将数组nums中所有数字加入allNums
    2、第2次遍历时，对于元素nums[i]，检查nums[i]+1是否在allNUms，如果存在将其从allNums中删除，当前序列长度+1，继续搜索nums[i]+2
        检查完+n之后，再检查nums[i]-1...-n。
        这样操作之后，nums[i]所在的序列从allNums中删除。
        遍历nums[i+1]，
            如果在allNums中不存在，说明其作为序列中的元素已被使用过，跳过。
            如果在allNums中存在，又有新的序列可以搜索。
    时间复杂度：O(n)，2次遍历nums，所有元素在哈希表中被添加、删除1次。
    空间复杂度：O(n)
'''


class Solution:
    # 哈希
    def longestConsecutive(self, nums: List[int]) -> int:
        allNums = set(nums)
        ans, curLen = 0, 1
        for i in nums:
            if i in allNums:
                allNums.remove(i)
                inc = i + 1
                while inc in allNums:
                    curLen += 1
                    allNums.remove(inc)
                    inc += 1
                dec = i - 1
                while dec in allNums:
                    curLen += 1
                    allNums.remove(dec)
                    dec -= 1
                ans = max(ans, curLen)
                curLen = 1
        return ans

    # 思路1，排序后搜索
    def longestConsecutive1(self, nums: List[int]) -> int:
        nums.sort()
        ans, curLen = 0, 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                curLen += 1
            else:
                ans = max(ans, curLen)
                curLen = 1
        ans = max(ans, curLen)
        return ans
