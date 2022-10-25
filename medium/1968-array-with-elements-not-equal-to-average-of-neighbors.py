'''
1968. 构造元素不等于两相邻元素平均值的数组
给你一个 下标从 0 开始 的数组 nums ，数组由若干 互不相同的 整数组成。你打算重新排列数组中的元素以满足：
重排后，数组中的每个元素都 不等于 其两侧相邻元素的 平均值 。

更公式化的说法是，重新排列的数组应当满足这一属性：对于范围 1 <= i < nums.length - 1 中的每个 i ，(nums[i-1] + nums[i+1]) / 2 
不等于 nums[i] 均成立 。

返回满足题意的任一重排结果。

 

示例 1：

输入：nums = [1,2,3,4,5]
输出：[1,2,4,5,3]
解释：
i=1, nums[i] = 2, 两相邻元素平均值为 (1+4) / 2 = 2.5
i=2, nums[i] = 4, 两相邻元素平均值为 (2+5) / 2 = 3.5
i=3, nums[i] = 5, 两相邻元素平均值为 (4+3) / 2 = 3.5
示例 2：

输入：nums = [6,2,0,9,7]
输出：[9,7,6,2,0]
解释：
i=1, nums[i] = 7, 两相邻元素平均值为 (9+6) / 2 = 7.5
i=2, nums[i] = 6, 两相邻元素平均值为 (7+2) / 2 = 4.5
i=3, nums[i] = 2, 两相邻元素平均值为 (6+0) / 2 = 3
 

提示：

3 <= nums.length <= 105
0 <= nums[i] <= 105
'''
from typing import List
'''
思路：排序
数组排序后，前一半元素放到偶数下标上，后一半元素放到奇数下标上

时间复杂度：O(nlogn)
空间复杂度：O(n)
'''


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = [0] * len(nums)
        for i in range(len(nums) // 2 + (len(nums) & 1)):
            ans[2 * i] = nums[i]
        j = 1
        for i in range(len(nums) // 2 + (len(nums) & 1), len(nums)):
            ans[j] = nums[i]
            j += 2
        return ans


s = Solution()
print(s.rearrangeArray(nums=[1, 2, 3, 4, 5]))
