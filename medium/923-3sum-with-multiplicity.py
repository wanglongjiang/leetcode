'''
923. 三数之和的多种可能
给定一个整数数组 arr ，以及一个整数 target 作为目标值，返回满足 i < j < k 且 arr[i] + arr[j] + arr[k] == target 的元组 i, j, k 的数量。

由于结果会非常大，请返回 109 + 7 的模。

 

示例 1：

输入：arr = [1,1,2,2,3,3,4,4,5,5], target = 8
输出：20
解释：
按值枚举(arr[i], arr[j], arr[k])：
(1, 2, 5) 出现 8 次；
(1, 3, 4) 出现 8 次；
(2, 2, 4) 出现 2 次；
(2, 3, 3) 出现 2 次。
示例 2：

输入：arr = [1,1,2,2,2,2], target = 5
输出：12
解释：
arr[i] = 1, arr[j] = arr[k] = 2 出现 12 次：
我们从 [1,1] 中选择一个 1，有 2 种情况，
从 [2,2,2,2] 中选出两个 2，有 6 种情况。
 

提示：

3 <= arr.length <= 3000
0 <= arr[i] <= 100
0 <= target <= 300
'''

from typing import Counter, List
'''
思路：数学 哈希
根据题意，出现的数字只有0..100，可以统计所有数字出现的个数。
然后遍历任意2个不同数字a、b的组合，查找满足c=target-a-b，如果存在c，
满足：a!=b!=c时，那么个数是count[a]*count[b]*count[c]
满足：a=c!=b 或者时b=c!=a，组合的个数用二项式公式计算
满嘴：a=b=c时，用二项式计算

时间复杂度：O(set(arr)^2)
空间复杂度：O(set(arr))
'''


class Solution(object):
    def threeSumMulti(self, A, target):
        MOD = 10**9 + 7
        count = [0] * 101
        for x in A:
            count[x] += 1

        ans = 0

        # All different
        for x in range(101):
            for y in range(x + 1, 101):
                z = target - x - y
                if y < z <= 100:
                    ans += count[x] * count[y] * count[z]
                    ans %= MOD

        # x == y
        for x in range(101):
            z = target - 2 * x
            if x < z <= 100:
                ans += count[x] * (count[x] - 1) // 2 * count[z]
                ans %= MOD

        # y == z
        for x in range(101):
            if (target - x) % 2 == 0:
                y = (target - x) // 2
                if x < y <= 100:
                    ans += count[x] * count[y] * (count[y] - 1) // 2
                    ans %= MOD

        # x == y == z
        if target % 3 == 0:
            x = target // 3
            if 0 <= x <= 100:
                ans += count[x] * (count[x] - 1) * (count[x] - 2) // 6
                ans %= MOD

        return ans


s = Solution()
print(s.threeSumMulti([0, 0, 0], 0))
print(s.threeSumMulti([2, 1, 3], 6))
print(s.threeSumMulti(arr=[1, 1, 2, 2, 3, 3, 4, 4, 5, 5], target=8))
