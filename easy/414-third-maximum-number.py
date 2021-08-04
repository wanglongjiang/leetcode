'''
第三大的数
给你一个非空数组，返回此数组中 第三大的数 。如果不存在，则返回数组中最大的数。

 

示例 1：

输入：[3, 2, 1]
输出：1
解释：第三大的数是 1 。
示例 2：

输入：[1, 2]
输出：2
解释：第三大的数不存在, 所以返回最大的数 2 。
示例 3：

输入：[2, 2, 3, 1]
输出：1
解释：注意，要求返回第三大的数，是指在所有不同数字中排第三大的数。
此例中存在两个值为 2 的数，它们都排第二。在所有不同数字中排第三大的数为 1 。
 

提示：

1 <= nums.length <= 104
-2^31 <= nums[i] <= 2^31 - 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/third-maximum-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
'''
思路：数组
设3个遍历a1,a2,a3分别代表最大的元素，第2个大的元素，第3大的元素
遍历数组，依次判断比较。
> 当num==a1 or a2，最大的数或者第2大的数不会发生变化，跳过
> 当num>a1时，最大值、第2大、第3大发生变动
> 当num>a2时，第2大，第3大发生变动
> 当num>a3时，第3大发生变动

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        a1, a2, a3 = float('-inf'), float('-inf'), float('-inf')
        for n in nums:
            if n == a1 or n == a2:
                pass
            elif n > a1:
                a3, a2, a1 = a2, a1, n
            elif n > a2:
                a3, a2 = a2, n
            elif n > a3:
                a3 = n
        return a3 if a3 != float('-inf') else a1


s = Solution()
print(s.thirdMax([3, 2, 1]))
print(s.thirdMax([1, 2]))
print(s.thirdMax([2, 2, 3, 1]))
print(s.thirdMax([2, 2, 2, 2]))
