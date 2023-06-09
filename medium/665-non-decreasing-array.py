'''
665. 非递减数列
给你一个长度为 n 的整数数组，请你判断在 最多 改变 1 个元素的情况下，该数组能否变成一个非递减数列。

我们是这样定义一个非递减数列的： 对于数组中任意的 i (0 <= i <= n-2)，总满足 nums[i] <= nums[i + 1]。



示例 1:
输入: nums = [4,2,3]
输出: true
解释: 你可以通过把第一个4变成1来使得它成为一个非递减数列。

示例 2:
输入: nums = [4,2,1]
输出: false
解释: 你不能在只改变一个元素的情况下将其变为非递减数列。


提示：

1 <= n <= 10 ^ 4
- 10 ^ 5 <= nums[i] <= 10 ^ 5
'''
from typing import List
'''
思路：贪心
初始设变量changed为false，表示未发生过改变。
遍历依次数组，查找数组中紧邻的递减数对，
如果发现有nums[i-1]>nums[i]，且changed为False，执行如下判断（changed为true返回false）：
> 如果nums[i-2]<=nums[i]，可以将nums[i-1]变小形成非递减序列
> 如果nums[i-2]不存在，可以将nums[i-1]变小形成非递减序列
> 如果nums[i-1]<=nums[i+1]，可以将nums[i]增大形成非递减序列
> 如果nums[i+1]不存在，可以将nums[i]增大形成非递减序列
> 如果满足上述4种情况之一，将changed改为true；如果均不满足，返回false。


时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True
        changed = False
        n = len(nums)
        for i in range(1, n):
            if nums[i] < nums[i - 1]:  # 违反非递减的要求
                if changed:  # 之前已经发生过一次，返回false
                    return False
                if i - 2 >= 0:
                    if nums[i - 2] <= nums[i]:  # 可以将nums[i-1]变小形成非递减序列
                        changed = True
                else:  # 可以将nums[i-1]变小形成非递减序列
                    changed = True
                if i + 1 < n:
                    if nums[i - 1] <= nums[i + 1]:  # 可以将nums[i]增大形成非递减序列
                        changed = True
                else:  # 可以将nums[i]增大形成非递减序列
                    changed = True
                if not changed:  # 无法通过修改某个值形成非递减序列，返回false
                    return False

        return True


s = Solution()
print(s.checkPossibility([4, 2, 3]))
print(s.checkPossibility([4, 2, 1]))
