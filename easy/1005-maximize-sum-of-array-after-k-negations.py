'''
K 次取反后最大化的数组和
给定一个整数数组 A，我们只能用以下方法修改该数组：我们选择某个索引 i 并将 A[i] 替换为 -A[i]，然后总共重复这个过程 K 次。
（我们可以多次选择同一个索引 i。）

以这种方式修改数组后，返回数组可能的最大和。

 

示例 1：

输入：A = [4,2,3], K = 1
输出：5
解释：选择索引 (1,) ，然后 A 变为 [4,-2,3]。
示例 2：

输入：A = [3,-1,0,2], K = 3
输出：6
解释：选择索引 (1, 2, 2) ，然后 A 变为 [3,1,0,2]。
示例 3：

输入：A = [2,-3,-1,5,-4], K = 2
输出：13
解释：选择索引 (1, 4) ，然后 A 变为 [2,3,-1,5,4]。
 

提示：

1 <= A.length <= 10000
1 <= K <= 10000
-100 <= A[i] <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximize-sum-of-array-after-k-negations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
'''
思路：排序、贪心
1. 将数组排序
2. 从小到大将数组中尽量多的负数取反，最多不超过k个数字。
> 如果负数有剩余，合计整个数组的和
> 如果负数不够k个，剩下的取反次数如果是奇数，需要选择数组中最小的数值进行取反

时间复杂度：O(nlog)
空间复杂度：O(1)
'''


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        for i in range(len(nums)):
            if k > 0:
                if nums[i] < 0:
                    nums[i] = -nums[i]
                    k -= 1
                else:
                    if k % 2:
                        if i > 0 and nums[i] < nums[i - 1]:
                            nums[i - 1] = -nums[i - 1]
                        else:
                            nums[i] = -nums[i]
                    break
        return sum(nums)
