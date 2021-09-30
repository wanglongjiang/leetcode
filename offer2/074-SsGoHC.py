'''
剑指 Offer II 074. 合并区间
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。

 

示例 1：

输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2：

输入：intervals = [[1,4],[4,5]]
输出：[[1,5]]
解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。
 

提示：

1 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= starti <= endi <= 10^4
 

注意：本题与主站 56 题相同： https://leetcode-cn.com/problems/merge-intervals/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/SsGoHC
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
'''
思路：排序 贪心
数组排序后，相邻的区间肯定靠在一起。类似于冒泡，从左向右合并区间，合并后的区间更新掉原值，当与右边无法合并时，加入结果list
时间复杂度：O(nlogn)，有排序nLogn，一次遍历
空间复杂度：O(n)，辅助数组存放返回值，最坏情况下N
'''


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = []
        n = len(intervals)
        for i in range(1, n):
            left, right = intervals[i - 1], intervals[i]
            if left[1] >= right[0]:
                right[0] = left[0]
                right[1] = max(left[1], right[1])
            else:
                result.append(left)
        result.append(intervals[n - 1])
        return result
