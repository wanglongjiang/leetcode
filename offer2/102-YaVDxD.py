'''
剑指 Offer II 102. 加减的目标值
给定一个正整数数组 nums 和一个整数 target 。

向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：

例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。

 

示例 1：

输入：nums = [1,1,1,1,1], target = 3
输出：5
解释：一共有 5 种方法让最终目标和为 3 。
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
示例 2：

输入：nums = [1], target = 1
输出：1
 

提示：

1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 1000
 

注意：本题与主站 494 题相同： https://leetcode-cn.com/problems/target-sum/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/YaVDxD
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
from collections import defaultdict
'''
思路1，回溯
暴力回溯所有的符号变化

时间复杂度：O($2^n$)，n最大为20，大概是10^6
空间复杂度：O(n)

思路2，哈希+回溯
将数组分成2部分，分别对2部分数组和进行计数，存到哈希表中
然后遍历其中一个哈希表，在另外一个哈希表中查找target-val，如果存在，进行累计

时间复杂度：O($2^{n/2}$)
空间复杂度：O($2^{n/2}$)
'''


class Solution:
    # 思路2
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 1:
            return 1 if abs(nums[0]) == abs(target) else 0
        leftcounter, rightcounter = defaultdict(int), defaultdict(int)
        mid = n // 2

        # 统计2部分所有的和的计数
        def countSum(counter, index, end, total):
            if index == end - 1:
                counter[total + nums[index]] += 1
                counter[total - nums[index]] += 1
            else:
                countSum(counter, index + 1, end, total + nums[index])
                countSum(counter, index + 1, end, total - nums[index])

        countSum(leftcounter, 0, mid, 0)
        countSum(rightcounter, mid, n, 0)
        # 遍历leftcounter，找rightcounter中与其配对的数量
        ans = 0
        for num, count in leftcounter.items():
            ans += count * rightcounter[target - num]
        return ans

    # 思路1
    def findTargetSumWays1(self, nums: List[int], target: int) -> int:
        n = len(nums)
        count = 0

        def backtrack(index, total):
            nonlocal count
            if index == n - 1:
                if total + nums[index] == target:
                    count += 1
                if total - nums[index] == target:
                    count += 1
            else:
                backtrack(index + 1, total + nums[index])
                backtrack(index + 1, total - nums[index])

        backtrack(0, 0)
        return count
