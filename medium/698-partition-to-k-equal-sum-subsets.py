'''
划分为k个相等的子集

给定一个整数数组  nums 和一个正整数 k，找出是否有可能把这个数组分成 k 个非空子集，其总和都相等。
提示：

1 <= k <= len(nums) <= 16
0 < nums[i] < 10000
'''
from typing import List
'''
思路：回溯
首先判断数组之和total/k能被整除，如果不能整除，则没有解
然后商d为每个子数组之和，nums中最大元素如果大于d，则没有解
如果通过了上面的检查，每次从数组中选取一个<=d的数nums[i]，d-=nums[i]，
如果d==0，则找到1个分组，继续查找下一个分组，直至所有分组都能找完
时间复杂度：O(2^n*n)，组合有2^n种，再加上每层查找的过程
空间复杂度：O(n)
TODO
'''


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        d, r = divmod(total, k)
        if r != 0:  # 数组之和不能被k整除，没有解
            return False
        if max(nums) > d:  # 最大值大于d，没有解
            return False

        def backtrack(sets, target):
            if sets > len(nums):
                return False
            for i in range(len(nums)):
                num = nums[i]
                if num <= target:  # 只有<=target的数才拿出来尝试组合
                    nums[i] = nums[-1]  # 进入组合的元素要删除
                    nums.pop()
                    if target == num:  # 找到了一个子集
                        if sets == 1:  # 如果是最后一个子集，则返回true
                            return True
                        else:
                            if backtrack(sets - 1, d):  # 不是最后一个子集，递归查找
                                return True
                    else:  # 子集的数据不够，递归
                        if backtrack(sets, target - num):
                            return True
                    nums.append(num)
            return False

        return backtrack(k, d)


s = Solution()
print(s.canPartitionKSubsets(nums=[4, 3, 2, 3, 5, 2, 1], k=4))
