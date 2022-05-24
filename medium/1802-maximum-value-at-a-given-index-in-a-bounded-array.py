'''
1802. 有界数组中指定下标处的最大值
给你三个正整数 n、index 和 maxSum 。你需要构造一个同时满足下述所有条件的数组 nums（下标 从 0 开始 计数）：

nums.length == n
nums[i] 是 正整数 ，其中 0 <= i < n
abs(nums[i] - nums[i+1]) <= 1 ，其中 0 <= i < n-1
nums 中所有元素之和不超过 maxSum
nums[index] 的值被 最大化
返回你所构造的数组中的 nums[index] 。

注意：abs(x) 等于 x 的前提是 x >= 0 ；否则，abs(x) 等于 -x 。

 

示例 1：

输入：n = 4, index = 2,  maxSum = 6
输出：2
解释：数组 [1,1,2,1] 和 [1,2,2,1] 满足所有条件。不存在其他在指定下标处具有更大值的有效数组。
示例 2：

输入：n = 6, index = 1,  maxSum = 10
输出：3
 

提示：

1 <= n <= maxSum <= 10^9
0 <= index < n
'''
'''
思路：二分查找 贪心
根据题意得知，任意2个相邻元素最多相差1
在maxSum固定的情况下，想要使nums[index]最大化，需要使用贪心，使nums[index]最大，0..index是递增的等差序列，index..n-1是递减的等差序列。
nums[index]的取值范围为1..maxSum-n+1
二分查找nums[index]，每次确定一个值，计算其形成的左右2个等差序列和是否<=maxSum

时间复杂度：O(log(maxSum))
空间复杂度：O(1)
'''


class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        lo, hi, ans = 1, maxSum - n + 1, 1
        while lo <= hi:
            mid = (lo + hi) // 2
            s = 0
            # 计算0..index构成的等差序列和，index的值为mid，向左依次递减
            if mid > index:  # 从第0项开始，能构成等差序列，用等差序列求和公式计算0..index的和
                s = (index + 1) * (mid - index + mid) // 2
            else:  # 数组最左边（有index + 1 - mid个）都是1，剩余的mid个元素才是等差序列
                s = mid * (1 + mid) // 2 + index + 1 - mid
            # 计算index+1..n-1的等差序列和，index右边第1个元素是mid-1，逻辑与上面类似
            rightSize = n - index - 1
            if mid > rightSize:
                s += rightSize * (mid - 1 + mid - 1 - (rightSize - 1)) // 2
            else:
                s += (mid - 1) * (1 + mid - 1) // 2 + rightSize - (mid - 1)
            if s > maxSum:
                hi = mid - 1
            else:
                ans = mid
                lo = mid + 1
        return ans


s = Solution()
print(s.maxValue(4, 0, 6))
print(s.maxValue(6, 0, 27))
print(s.maxValue(n=4, index=2, maxSum=6))
print(s.maxValue(n=6, index=1, maxSum=10))
