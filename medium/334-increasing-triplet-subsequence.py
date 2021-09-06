'''
递增的三元子序列
给你一个整数数组 nums ，判断这个数组中是否存在长度为 3 的递增子序列。

如果存在这样的三元组下标 (i, j, k) 且满足 i < j < k ，使得 nums[i] < nums[j] < nums[k] ，返回 true ；否则，返回 false 。

 

示例 1：

输入：nums = [1,2,3,4,5]
输出：true
解释：任何 i < j < k 的三元组都满足题意
示例 2：

输入：nums = [5,4,3,2,1]
输出：false
解释：不存在满足题意的三元组
示例 3：

输入：nums = [2,1,5,0,4,6]
输出：true
解释：三元组 (3, 4, 5) 满足题意，因为 nums[3] == 0 < nums[4] == 4 < nums[5] == 6
 

提示：

1 <= nums.length <= 10^5
-2^31 <= nums[i] <= 23^1 - 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/increasing-triplet-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
'''
思路：数组
有点类似于单调栈，但又不同。
设2个变量min1,min2，分别保存最小的元素和第2小的元素。算法如下：
当前元素num>min2时，找到了3元组；
num<min1时，min1=num；
num<min2时，min2=num；
说明：min1始终保存最小的元素，这没有问题，但min2有可能会是min1之前的元素，这会影响结果吗？
不会，因为[min1,min2]构成了递增序列，当min1被替换，min2虽然是min1之前的元素，但假如此时有num>min2，递增序列仍然成立。

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min1, min2 = float('inf'), float('inf')
        for num in nums:
            if num > min2:
                return True
            elif num < min1:
                min1 = num
            elif min1 < num < min2:
                min2 = num
        return False


s = Solution()
print(s.increasingTriplet([1, 1, -2, 6]))
