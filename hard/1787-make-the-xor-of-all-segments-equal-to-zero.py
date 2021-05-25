'''
使所有区间的异或结果为零
给你一个整数数组 nums​​​ 和一个整数 k​​​​​ 。区间 [left, right]（left <= right）的 异或结果
是对下标位于 left 和 right（包括 left 和 right ）之间所有元素进行
XOR 运算的结果：nums[left] XOR nums[left+1] XOR ... XOR nums[right] 。

返回数组中 要更改的最小元素数 ，以使所有长度为 k 的区间异或结果等于零。

 

示例 1：
输入：nums = [1,2,0,3,0], k = 1
输出：3
解释：将数组 [1,2,0,3,0] 修改为 [0,0,0,0,0]

示例 2：
输入：nums = [3,4,5,2,1,7,3,4,7], k = 3
输出：3
解释：将数组 [3,4,5,2,1,7,3,4,7] 修改为 [3,4,7,3,4,7,3,4,7]

示例 3：
输入：nums = [1,2,4,1,2,5,1,2,6], k = 3
输出：3
解释：将数组[1,2,4,1,2,5,1,2,6] 修改为 [1,2,3,1,2,3,1,2,3]
 

提示：

1 <= k <= nums.length <= 2000
​​​​​​0 <= nums[i] < 2^10
'''
from typing import List
from collections import defaultdict
'''
思路：动态规划
根据提示，如果k个数的异或为0，那么这k个数会在数组中循环出现，也就是nums[i]=nums[i+k]
所以可以将数组划分成大小为k的多个子数组，这些子数组在相同的下标处必须是同样的数才能满足题目要求。
设一个二维dp数组，dp[i][v]为子数组第i个数的异或为v时的最小的更改值
dp[i][v]的最大值为min(dp[i-1][0..1023])+count(i)，说明一下，min(dp[i-1][0..1023])是第i-1个数中最少的替换次数，count(i)是第i个数有多少个，最极端就是全部替换
dp[i][v]得到上面的最大值之后，还需要进一步优化，优化方法为遍历在第i位上所有出现过的数字num，
其在第i-1位上的最少更换次数为dp[i-1][v^num]+count(i)-gcount(i,num)，gcount(i,num)指第i位上num出现的次数
根据上面的分析写出代码

时间复杂度：O(1024n)
空间复杂度：O(1024n)
'''


class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = [0] * k  # 用于统计子数组第i位上共有多少个数字
        gcount = [defaultdict(int) for _ in range(k)]  # 用于统计子数组第i位上num出现了多少次
        for i in range(n):
            gcount[i % k][nums[i]] += 1
            count[i % k] += 1
        dp = [[2000] * 1024 for _ in range(k + 1)]  # 初始化为2000的原因是数组长度最大为2000,也就是最大替换2000次
        dp[0][0] = 0  # 第0位为哨兵，简化计算用，子数组的第i位dp数组从1开始，注意上面的计数是从0开始的，下面计算dp的时候需要注意转换
        for i in range(1, k + 1):
            maxCnt = min(dp[i - 1])
            for j in range(1024):
                dp[i][j] = maxCnt + count[i - 1]  # 设置最大替换次数，也就是第i位的数字全部替换
            for num, cnt in gcount[i - 1].items():  # 遍历i位上所有出现的数字
                for v in range(1024):  # 对于dp[i][v]其上一个dp元素是dp[i][v^num]，因为此次是要全部替换为num，v^num^num=v
                    dp[i][v] = min(dp[i][v], dp[i - 1][num ^ v] + count[i - 1] - cnt)
        return dp[k][0]


s = Solution()
print(s.minChanges(nums=[1, 2, 0, 3, 0], k=1))
