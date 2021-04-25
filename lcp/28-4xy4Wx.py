'''
LCP 28. 采购方案
小力将 N 个零件的报价存于数组 nums。小力预算为 target，假定小力仅购买两个零件，要求购买零件的花费不超过预算，
请问他有多少种采购方案。

注意：答案需要以 1e9 + 7 (1000000007) 为底取模，如：计算初始结果为：1000000008，请返回 1

提示：

2 <= nums.length <= 10^5
1 <= nums[i], target <= 10^5
'''
from typing import List
'''
思路：树状数组、线段树、二分查找
这里采用树状数组。
1、建立树状数组
2、遍历数组，在树状数组中查找target-nums[i]的元素个数
num[i]与<=(target-num[i])的数据都是合法的解
时间复杂度：O(nlogn)，建立树状数组O(nlogn)，查找组合O(nlogn)
空间复杂度：O(n)
'''


class Solution:
    def purchasePlans(self, nums: List[int], target: int) -> int:
        # 1、建立树状数组
        n = 1000001
        c = [0] * n

        def lowbit(x):
            return x & -x

        def update(x):
            while x <= n:
                c[x] += 1
                x += lowbit(x)

        def getcount(x):
            res = 0
            while x > 0:
                res += c[x]
                x -= lowbit(x)
            return res

        for num in nums:
            update(num)
        # 2、查找target-nums[i]的数据个数
        ans = 0
        for num in nums:
            cnt = getcount(target - num)
            if cnt > 0 and target - num >= num:  # 如果num<=target-num，需要将其自身排除
                cnt -= 1
            ans += cnt
        return (ans // 2) % 1000000007  # 除以2的原因是每个合法的组合都出行了2次即nums[i],nums[j]和nums[j],nums[i]


s = Solution()
print(s.purchasePlans(nums=[2, 5, 3, 5], target=6))
print(s.purchasePlans(nums=[2, 2, 1, 9], target=10))
