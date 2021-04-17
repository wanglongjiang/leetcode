'''
区间和的个数

给定一个整数数组 nums 。区间和 S(i, j) 表示在 nums 中，位置从 i 到 j 的元素之和，包含 i 和 j (i ≤ j)。

请你以下标 i （0 <= i <= nums.length ）为起点，元素个数逐次递增，计算子数组内的元素和。

当元素和落在范围 [lower, upper] （包含 lower 和 upper）之内时，记录子数组当前最末元素下标 j ，记作 有效 区间和 S(i, j) 。

求数组中，值位于范围 [lower, upper] （包含 lower 和 upper）之内的 有效 区间和的个数。

注意：
最直观的算法复杂度是 O(n2) ，请在此基础上优化你的算法。

提示：

0 <= nums.length <= 10^4
'''
from typing import List
'''
思路1，暴力计算
1、计算出0..n的累计和sums[]
2、从左向右遍历nums，对于每个nums[i]，j>i依次计算sums[j]-nums[i]得到从i+1开始的累计和
上述2个过程中，统计lower<=sums[i]<=upper的个数
时间复杂度：O(n^2)
空间复杂度：O(n)

思路2，离散化+树状数组
1、离散化前缀和
2、更新查询前缀和
时间复杂度：O(nlogn)
空间复杂度：O(n)
'''


class Solution:
    # 思路2，树状数组
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        if not nums:
            return 0
        # 离散化
        sums = [0]
        for num in nums:
            sums.append(sums[-1] + num)
        vals = set()
        for num in sums:
            vals |= {num, num + lower, num + upper}
        vals = sorted(vals)
        index = {}
        for i, num in enumerate(vals):
            index[num] = i
        n = len(vals)
        c = [0] * n

        # 定义树状数组函数
        def lowbit(x):
            return x & -x

        def update(i):
            i += 1
            while i <= n:
                c[i - 1] += 1
                i += lowbit(i)

        def getsum(i):
            res = 0
            i += 1
            while i >= 1:
                res += c[i - 1]
                i -= lowbit(i)
            return res

        # 更新查询树
        ans = 0
        for num in sums[::-1]:
            left, right = index[num + lower], index[num + upper]
            ans += getsum(right)
            if left > 0:
                ans -= getsum(left - 1)
            update(index[num])
        return ans

    # 思路1，暴力计算
    def countRangeSum1(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        count = 1 if lower <= nums[0] <= upper else 0
        if n == 1:
            return count
        sums = [0] * n
        sums[0] = nums[0]
        for i in range(1, n):
            sums[i] = sums[i - 1] + nums[i]
            count += 1 if lower <= sums[i] <= upper else 0
        # sums依次减少nums[0..n-1]
        for i in range(n - 1):
            for j in range(i + 1, n):
                sums[j] = sums[j] - nums[i]
                count += 1 if lower <= sums[j] <= upper else 0
        return count


s = Solution()
print(s.countRangeSum(nums=[-2, 5, -1], lower=-2, upper=2))
