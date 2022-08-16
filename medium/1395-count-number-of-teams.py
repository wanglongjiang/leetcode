'''
1395. 统计作战单位数
 n 名士兵站成一排。每个士兵都有一个 独一无二 的评分 rating 。

每 3 个士兵可以组成一个作战单位，分组规则如下：

从队伍中选出下标分别为 i、j、k 的 3 名士兵，他们的评分分别为 rating[i]、rating[j]、rating[k]
作战单位需满足： rating[i] < rating[j] < rating[k] 或者 rating[i] > rating[j] > rating[k] ，其中  0 <= i < j < k < n
请你返回按上述条件可以组建的作战单位数量。每个士兵都可以是多个作战单位的一部分。

 

示例 1：

输入：rating = [2,5,3,4,1]
输出：3
解释：我们可以组建三个作战单位 (2,3,4)、(5,4,1)、(5,3,1) 。
示例 2：

输入：rating = [2,1,3]
输出：0
解释：根据题目条件，我们无法组建作战单位。
示例 3：

输入：rating = [1,2,3,4]
输出：4
 

提示：

n == rating.length
3 <= n <= 1000
1 <= rating[i] <= 10^5
rating 中的元素都是唯一的
'''
from typing import List
from sortedcontainers import SortedList
'''
思路：有序集合 映射
对于rating[k]，以其中点的作战单元个数=左侧小于rating[k]*右侧大于rating[k]+左侧大于rating[k]*右侧小于rating[k]
首先将rating进行排序，对每个数字rating[i]映射成其在数组中的排序
然后设一个有序集合，在遍历rating过程中依次将元素加入其中。
对于rating[k]，通过二分查找，能够知道左侧小于它和大于它的元素个数，再结合映射知道右侧大于它和小于它的个数，
有了这2组数，就可以计算出以其为中点的作战单元个数

时间复杂度：O(nlogn)
空间复杂度：O(n)
'''


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        sortMap = {rate: i for i, rate in enumerate(sorted(rating))}  # 建立数组与顺序的映射
        sl = SortedList()
        ans, n = 0, len(rating)
        for rate in rating:
            leftLt = sl.bisect_left(rate)  # 左侧小于它的
            leftGt = len(sl) - leftLt  # 左侧大于它的
            rightLt = sortMap[rate] - leftLt  # 右侧小于它的
            rightGt = n - leftLt - leftGt - rightLt - 1  # 右侧大于它的
            ans += leftLt * rightGt + leftGt * rightLt  # 计算以其为中点的单元个数，并累计到答案中
            sl.add(rate)
        return ans
