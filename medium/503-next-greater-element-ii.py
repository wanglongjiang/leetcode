'''
下一个更大元素 II
给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），输出每个元素的下一个更大元素。
数字 x 的下一个更大的元素是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。
如果不存在，则输出 -1。

'''
from typing import List
'''
思路1，按照题目给出的算法，每次都向前搜索下一个更大的元素，最坏情况下（数组中所有元素相同）需要2重循环，
    时间复杂度O(n*n)，按照题目中给出的最大数量量，会是10^8。
    空间复杂度O(1)
思路2，对输入数组进行2遍扫描，第1次提取其中不重复集合，并排序，第2次遍历输入数组找出下一个最大的元素。
    时间复杂度，2遍遍历，1次元素集合的排序，O(nlogn)
    空间复杂度O(n)
'''


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        li = list({x for x in nums})
        li.sort()
        nextMap = {}
        for i in range(len(li) - 1):
            nextMap[li[i]] = li[i + 1]
        nextMap[li[len(li) - 1]] = -1
        ans = [0] * len(nums)
        for i in range(len(nums)):
            ans[i] = nextMap[nums[i]]
        return ans


s = Solution()
print(s.nextGreaterElements([1, 2, 1]))
