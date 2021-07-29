'''
最大间距

给定一个无序的数组，找出数组在排序之后，相邻元素之间最大的差值。

如果数组元素个数小于 2，则返回 0。
你可以假设数组中所有元素都是非负整数，且数值在 32 位有符号整数范围内。
请尝试在线性时间复杂度和空间复杂度的条件下解决此问题。

示例 1:

输入: [3,6,9,1]
输出: 3
解释: 排序后的数组是 [1,3,6,9], 其中相邻元素 (3,6) 和 (6,9) 之间都存在最大差值 3。
示例 2:

输入: [10]
输出: 0
解释: 数组元素个数小于 2，因此返回 0。
说明:

你可以假设数组中所有元素都是非负整数，且数值在 32 位有符号整数范围内。
请尝试在线性时间复杂度和空间复杂度的条件下解决此问题。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-gap
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
'''
思路：桶排序。
基于比较的算法上限就是O(nlogn)，没有办法达到O(n)，可以使用桶排序
先找出最大值、最小值max,min，(max-min)/(n+1)即为桶的大小
一个数的桶索引是(num-min)/(max-min)/(n+1)，优化下算法，r = max-min，bucketLen=n+1, index = bucketLen*(num-min)//r
最大差出现在1个桶的最小值-前一个桶内最大值。
不会出现在桶内，因为桶内最大差<buketSize = (max-min)/(n+1)。而因为桶有n+1个，必然有空桶存在，也就是最大差必然大于buketSize
时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        # 找到最大、最小值
        maxn, minn = float('-inf'), float('inf')
        for num in nums:
            if num > maxn:
                maxn = num
            if num < minn:
                minn = num
        # 桶排序
        bucketLen, r = len(nums) + 1, maxn - minn
        buckets = [[] for _ in range(bucketLen)]  # 桶内存放数组，数组只保存2个元素，最大值和最小值
        buckets[-1].append(maxn)  # 特殊处理最大值，避免下标溢出
        for num in nums:
            if num == maxn:
                continue
            index = (bucketLen * (num - minn)) // r
            if buckets[index]:
                if len(buckets[index]) == 2:
                    if buckets[index][0] > num:
                        buckets[index][0] = num
                    elif buckets[index][1] < num:
                        buckets[index][1] = num
                else:
                    if buckets[index][0] < num:
                        buckets[index].append(num)
                    elif buckets[index][0] > num:
                        buckets[index].insert(0, num)
            else:
                buckets[index].append(num)
        # 求2个桶之间的最大差
        ans = 0
        pre = None
        for bucket in buckets:
            if bucket:
                if pre:
                    ans = max(ans, bucket[0] - pre[-1])
                pre = bucket
        return ans


s = Solution()
print(s.maximumGap([1, 3, 100]))
print(s.maximumGap([3, 6, 9, 1]))
print(s.maximumGap([10]))
print(s.maximumGap([1, 10000000]))
