'''
1906. 查询差绝对值的最小值
一个数组 a 的 差绝对值的最小值 定义为：0 <= i < j < a.length 且 a[i] != a[j] 的 |a[i] - a[j]| 的 最小值。如果 a 中所有元素都 相同 ，那么差绝对值的最小值为 -1 。

比方说，数组 [5,2,3,7,2] 差绝对值的最小值是 |2 - 3| = 1 。注意答案不为 0 ，因为 a[i] 和 a[j] 必须不相等。
给你一个整数数组 nums 和查询数组 queries ，其中 queries[i] = [li, ri] 。对于每个查询 i ，计算 子数组 nums[li...ri] 中 差绝对值的最小值 ，
子数组 nums[li...ri] 包含 nums 数组（下标从 0 开始）中下标在 li 和 ri 之间的所有元素（包含 li 和 ri 在内）。

请你返回 ans 数组，其中 ans[i] 是第 i 个查询的答案。

子数组 是一个数组中连续的一段元素。

|x| 的值定义为：

如果 x >= 0 ，那么值为 x 。
如果 x < 0 ，那么值为 -x 。
 

示例 1：

输入：nums = [1,3,4,8], queries = [[0,1],[1,2],[2,3],[0,3]]
输出：[2,1,4,1]
解释：查询结果如下：
- queries[0] = [0,1]：子数组是 [1,3] ，差绝对值的最小值为 |1-3| = 2 。
- queries[1] = [1,2]：子数组是 [3,4] ，差绝对值的最小值为 |3-4| = 1 。
- queries[2] = [2,3]：子数组是 [4,8] ，差绝对值的最小值为 |4-8| = 4 。
- queries[3] = [0,3]：子数组是 [1,3,4,8] ，差的绝对值的最小值为 |3-4| = 1 。
示例 2：

输入：nums = [4,5,2,2,7,10], queries = [[2,3],[0,2],[0,5],[3,5]]
输出：[-1,1,1,3]
解释：查询结果如下：
- queries[0] = [2,3]：子数组是 [2,2] ，差绝对值的最小值为 -1 ，因为所有元素相等。
- queries[1] = [0,2]：子数组是 [4,5,2] ，差绝对值的最小值为 |4-5| = 1 。
- queries[2] = [0,5]：子数组是 [4,5,2,2,7,10] ，差绝对值的最小值为 |4-5| = 1 。
- queries[3] = [3,5]：子数组是 [2,7,10] ，差绝对值的最小值为 |7-10| = 3 。
 

提示：

2 <= nums.length <= 105
1 <= nums[i] <= 100
1 <= queries.length <= 2 * 104
0 <= li < ri < nums.length
'''
from typing import List
'''
思路：前缀和
设一个前缀和数组pre，数组中是大小为101的数组，pre[i]存储截止i元素的所有值的计数。
首先遍历一次nums，统计pre
然后遍历queries，对于每个查询，通过对前缀和数组进行算术运算得到该子数组内所有元素的计数，遍历不为0的元素的间隔，返回最小的那个即可

时间复杂度：O(100n+100m),n为nums.length，m为queries.length
空间复杂度：O(100n)
'''


class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        pre = [None for _ in range(n)]
        pre[0] = [0] * 101
        pre[0][nums[0]] = 1
        for i in range(1, n):
            pre[i] = pre[i - 1].copy()
            pre[i][nums[i]] += 1  # 统计每个元素的前缀和计数
        ans = []
        for q in queries:
            count = [pre[q[1]][i] - pre[q[0]][i] for i in range(101)]
            count[nums[q[0]]] += 1
            diff = 101
            preNum = -100
            # 下面的迭代过程目的是为了找出最小的间隔
            for i in range(1, 101):
                if count[i]:
                    diff = min(diff, i - preNum)
                    preNum = i
                if diff == 1:
                    break
            if diff == 101:
                diff = -1
            ans.append(diff)
        return ans


s = Solution()
print(s.minDifference(nums=[1, 3, 4, 8], queries=[[0, 1], [1, 2], [2, 3], [0, 3]]))
print(s.minDifference(nums=[4, 5, 2, 2, 7, 10], queries=[[2, 3], [0, 2], [0, 5], [3, 5]]))
