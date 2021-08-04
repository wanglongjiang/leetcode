'''
三角形的最大周长
给定由一些正数（代表长度）组成的数组 A，返回由其中三个长度组成的、面积不为零的三角形的最大周长。

如果不能形成任何面积不为零的三角形，返回 0。

 

示例 1：

输入：[2,1,2]
输出：5
示例 2：

输入：[1,2,1]
输出：0
示例 3：

输入：[3,2,3,4]
输出：10
示例 4：

输入：[3,6,2,3]
输出：8
 

提示：

3 <= A.length <= 10000
1 <= A[i] <= 10^6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/largest-perimeter-triangle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
'''
思路：排序、贪心
能形成三角形的3个字数，2个短边边长之和要小于第3条边长。
可以对数组进行排序，从大到小，找到的第1个符合条件的三元组。

时间复杂度：O(nlogn)
空间复杂度：O(1)
'''


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(2, len(nums)):
            if nums[i - 2] < nums[i - 1] + nums[i]:
                return nums[i - 2] + nums[i - 1] + nums[i]
        return 0


s = Solution()
print(s.largestPerimeter([2, 1, 2]))
