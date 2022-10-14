'''
2121. 相同元素的间隔之和
给你一个下标从 0 开始、由 n 个整数组成的数组 arr 。

arr 中两个元素的 间隔 定义为它们下标之间的 绝对差 。更正式地，arr[i] 和 arr[j] 之间的间隔是 |i - j| 。

返回一个长度为 n 的数组 intervals ，其中 intervals[i] 是 arr[i] 和 arr 中每个相同元素（与 arr[i] 的值相同）的 间隔之和 。

注意：|x| 是 x 的绝对值。

 

示例 1：

输入：arr = [2,1,3,1,2,3,3]
输出：[4,2,7,2,4,4,5]
解释：
- 下标 0 ：另一个 2 在下标 4 ，|0 - 4| = 4
- 下标 1 ：另一个 1 在下标 3 ，|1 - 3| = 2
- 下标 2 ：另两个 3 在下标 5 和 6 ，|2 - 5| + |2 - 6| = 7
- 下标 3 ：另一个 1 在下标 1 ，|3 - 1| = 2
- 下标 4 ：另一个 2 在下标 0 ，|4 - 0| = 4
- 下标 5 ：另两个 3 在下标 2 和 6 ，|5 - 2| + |5 - 6| = 4
- 下标 6 ：另两个 3 在下标 2 和 5 ，|6 - 2| + |6 - 5| = 5
示例 2：

输入：arr = [10,5,10,10]
输出：[5,0,3,4]
解释：
- 下标 0 ：另两个 10 在下标 2 和 3 ，|0 - 2| + |0 - 3| = 5
- 下标 1 ：只有这一个 5 在数组中，所以到相同元素的间隔之和是 0
- 下标 2 ：另两个 10 在下标 0 和 3 ，|2 - 0| + |2 - 3| = 3
- 下标 3 ：另两个 10 在下标 0 和 2 ，|3 - 0| + |3 - 2| = 4
 

提示：

n == arr.length
1 <= n <= 105
1 <= arr[i] <= 105
'''
from collections import defaultdict
import itertools
from typing import List
'''
思路：哈希表 前缀和
首先用一个哈希表将所有相同值的下标用list聚集在一起。
然后，同一个list内的下标需要计数与其他下标的间隔，这里可以计算整个list的前缀和，
- 对于i，与前面的下标的间隔是i*n-前面n项的前缀和
- 对于i，与后面的下标的间隔是后面m项目的前缀和-i*m

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        groupList = defaultdict(list)
        for i, val in enumerate(arr):
            groupList[val].append(i)
        ans = [0] * len(arr)
        for li in groupList.values():
            presum = list(itertools.accumulate(li))  # 计算前缀和
            for idx, i in enumerate(li):
                if idx > 0:
                    ans[i] = i * idx - presum[idx - 1]
                if idx < len(li) - 1:
                    ans[i] += presum[-1] - presum[idx] - (len(li) - idx - 1) * i
        return ans


s = Solution()
assert s.getDistances([2, 1, 3, 1, 2, 3, 3]) == [4, 2, 7, 2, 4, 4, 5]
assert s.getDistances([10, 5, 10, 10]) == [5, 0, 3, 4]
