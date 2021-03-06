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
思路2，对输入数组进行2遍扫描，第1次扫描从左到右，从右到左找出截止当前位置最大的值，
    第2次扫描根据截止最大值决定是向前搜索还是向后搜索。
    时间复杂度O(n*n) 平均时间比上面好很多
    空间复杂度O(n)
思路3，单调栈+循环数组
    创建1个单调栈，栈中存放数组下标，下标指向的元素从栈顶到栈底单调不升，
    每当移动到数组下一个元素，就判断栈顶指向的值是否小于该元素，如果小于，将栈顶元素的下一个值设置为该当前元素
    将本元素入栈。对于单调递减的列表，第1遍扫描无法找到全部元素下一值，需要进行2遍扫描
'''


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 0:
            return []
        ans = [-1] * n
        stack = []
        for i in range(2 * n - 1):
            while stack and nums[stack[-1]] < nums[i % n]:
                ans[stack.pop()] = nums[i % n]
            stack.append(i % n)
        return ans

    def nextGreaterElements2(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 0:
            return []
        forward, backward = [0] * n, [0] * n  # 存储数组从前往后，从后往前到该位置最大值
        forward[0] = nums[0]
        backward[n - 1] = nums[n - 1]
        for i in range(1, len(nums)):
            forward[i] = max(forward[i - 1], nums[i])
        for i in range(n - 2, -1, -1):
            backward[i] = max(backward[i + 1], nums[i])
        ans = [0] * len(nums)
        for i in range(n):
            if nums[i] < backward[i]:  # 向前搜索能找到
                for j in range(i + 1, n):
                    if nums[j] > nums[i]:
                        ans[i] = nums[j]
                        break
            elif nums[i] < forward[i]:  # 向后搜索能找到
                for j in range(0, i):
                    if nums[j] > nums[i]:
                        ans[i] = nums[j]
                        break
            else:
                ans[i] = -1
        return ans


s = Solution()
print(s.nextGreaterElements([5, 4, 3, 2, 1]))
print(s.nextGreaterElements([1, 2, 1]))
