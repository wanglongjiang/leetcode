'''
剑指 Offer II 090. 环形房屋偷盗
一个专业的小偷，计划偷窃一个环形街道上沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。

给定一个代表每个房屋存放金额的非负整数数组 nums ，请计算 在不触动警报装置的情况下 ，今晚能够偷窃到的最高金额。

 

示例 1：

输入：nums = [2,3,2]
输出：3
解释：你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
示例 2：

输入：nums = [1,2,3,1]
输出：4
解释：你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
     偷窃到的最高金额 = 1 + 3 = 4 。
示例 3：

输入：nums = [0]
输出：0
 

提示：

1 <= nums.length <= 100
0 <= nums[i] <= 1000
 

注意：本题与主站 213 题相同： https://leetcode-cn.com/problems/house-robber-ii/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/PzWKhm
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
'''
思路：动态规划
与198题类似。不同点在于第0个选择与否会影响最终结果。可以将计算分解成2部分，包含第0个，不包含第0个的2次计算。
最后求2次计算的最大值。
时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        f = [0] * n
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        # 第1次计算包含nums[0],不包含nums[-1]
        f[0] = nums[0]
        f[1] = nums[1]
        f[2] = f[0] + nums[2]
        for i in range(3, n - 1):
            f[i] = max(f[i - 2] + nums[i], f[i - 3] + nums[i])
        ans = max(f[-2], f[-3])
        # 第2次计算不包含nums[0]，包含nums[-1]
        f[0] = 0
        f[1] = nums[1]
        f[2] = f[0] + nums[2]
        for i in range(3, n):
            f[i] = max(f[i - 2] + nums[i], f[i - 3] + nums[i])
        return max(f[-1], f[-2], ans)  # 返回值为2次计算的最大值
