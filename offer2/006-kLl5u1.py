'''
剑指 Offer II 006. 排序数组中两个数字之和
给定一个已按照 升序排列  的整数数组 numbers ，请你从数组中找出两个数满足相加之和等于目标数 target 。

函数应该以长度为 2 的整数数组的形式返回这两个数的下标值。numbers 的下标 从 0 开始计数 ，所以答案数组应当满足 0 <= answer[0] < answer[1] < numbers.length 。

假设数组中存在且只存在一对符合条件的数字，同时一个数字不能使用两次。

 

示例 1：

输入：numbers = [1,2,4,6,10], target = 8
输出：[1,3]
解释：2 与 6 之和等于目标数 8 。因此 index1 = 1, index2 = 3 。
示例 2：

输入：numbers = [2,3,4], target = 6
输出：[0,2]
示例 3：

输入：numbers = [-1,0], target = -1
输出：[0,1]
 

提示：

2 <= numbers.length <= 3 * 10^4
-1000 <= numbers[i] <= 1000
numbers 按 递增顺序 排列
-1000 <= target <= 1000
仅存在一个有效答案
 

注意：本题与主站 167 题相似（下标起点不同）：https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kLl5u1
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
'''
思路：双指针
设left,right2个指针，初始分别指向数组的2端。
1. 当left,right指向的元素之和>target时，right指针需要向内移动，使和变小
2. 当left,right指向的元素之和<target时，left指针需要向右移动，使和变大
3. 重复上面过程，直至left,right指向的元素之和等于target

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            val = numbers[left] + numbers[right]
            if val > target:
                right -= 1
            elif val < target:
                left += 1
            else:
                return [left, right]
        return []
