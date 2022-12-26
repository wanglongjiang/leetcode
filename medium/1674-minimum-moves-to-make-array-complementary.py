'''
1674. 使数组互补的最少操作次数
给你一个长度为 偶数 n 的整数数组 nums 和一个整数 limit 。每一次操作，你可以将 nums 中的任何整数替换为 1 到 limit 之间的另一个整数。

如果对于所有下标 i（下标从 0 开始），nums[i] + nums[n - 1 - i] 都等于同一个数，则数组 nums 是 互补的 。
例如，数组 [1,2,3,4] 是互补的，因为对于所有下标 i ，nums[i] + nums[n - 1 - i] = 5 。

返回使数组 互补 的 最少 操作次数。

 

示例 1：

输入：nums = [1,2,4,3], limit = 4
输出：1
解释：经过 1 次操作，你可以将数组 nums 变成 [1,2,2,3]（加粗元素是变更的数字）：
nums[0] + nums[3] = 1 + 3 = 4.
nums[1] + nums[2] = 2 + 2 = 4.
nums[2] + nums[1] = 2 + 2 = 4.
nums[3] + nums[0] = 3 + 1 = 4.
对于每个 i ，nums[i] + nums[n-1-i] = 4 ，所以 nums 是互补的。
示例 2：

输入：nums = [1,2,2,1], limit = 2
输出：2
解释：经过 2 次操作，你可以将数组 nums 变成 [2,2,2,2] 。你不能将任何数字变更为 3 ，因为 3 > limit 。
示例 3：

输入：nums = [1,2,1,2], limit = 2
输出：0
解释：nums 已经是互补的。
 

提示：

n == nums.length
2 <= n <= 105
1 <= nums[i] <= limit <= 105
n 是偶数。
'''

from typing import List
'''
我们考虑任意一个数对(a,b)(a,b)，不妨假设a\leq ba≤b。假设最终选定的和值为targettarget，则我们可以发现，对于(a,b)(a,b)这个数对：

当target<1+atarget<1+a时，需要操作两次；
当1+a\leq target<a+b1+a≤target<a+b时，需要操作一次；
当target=a+btarget=a+b时，不需要操作；
当a+b<target\leq b+limita+b<target≤b+limit时，需要操作一次；
当target>b+limittarget>b+limit时，需要操作两次。
我们设初始操作次数为两次。令targettarget从数轴最左端开始向右移动，我们会发现：

在1+a1+a处，操作次数减少一次；
在a+ba+b处，操作次数减少一次；
在a+b+1a+b+1处，操作次数增加一次；
在b+limit+1b+limit+1处，操作次数增加一次。
因此，我们可以遍历数组中的所有数对，求出每个数对的这四个关键位置，然后更新差分数组。最后，我们遍历（扫描）差分数组，就可以找到令总操作次数最小的targettarget，同时可以得到最少的操作次数。

时间复杂度O(N+L)O(N+L)。
空间复杂度O(L)O(L)。
TODO
'''


class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        pass
