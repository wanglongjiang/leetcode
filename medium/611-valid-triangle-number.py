'''
有效三角形的个数
给定一个包含非负整数的数组，你的任务是统计其中可以组成三角形三条边的三元组个数。

示例 1:

输入: [2,2,3,4]
输出: 3
解释:
有效的组合是:
2,3,4 (使用第一个 2)
2,3,4 (使用第二个 2)
2,2,3
注意:

数组长度不超过1000。
数组里整数的范围为 [0, 1000]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-triangle-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
import bisect
'''
思路：排序、二分查找
三角形的2个短边之和要大于第三条边，也就是3个数字要求任意2个数字之和要大于剩余的那个数字。
可以对数组进行排序，双重循环先确定2个数的组合，然后用二分查找确定剩余的数组中能满足<a+b的数字个数累加起来

时间复杂度：O(n^2*logn)
空间复杂度：O(1)
'''


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()  # 数字排序
        ans = 0
        n = len(nums)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                k = bisect.bisect_left(nums, nums[i] + nums[j], j + 1, n)  # 查找小于nums[i]+nums[j]的索引
                ans += k - j - 1  # k和j之间的数值均小于nums[i]+nums[j]，可以形成三角形
        return ans


s = Solution()
print(s.triangleNumber([2, 2, 3, 4]))
