'''
632. 最小区间
你有 k 个 非递减排列 的整数列表。找到一个 最小 区间，使得 k 个列表中的每个列表至少有一个数包含在其中。

我们定义如果 b-a < d-c 或者在 b-a == d-c 时 a < c，则区间 [a,b] 比 [c,d] 小。

 

示例 1：

输入：nums = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
输出：[20,24]
解释： 
列表 1：[4, 10, 15, 24, 26]，24 在区间 [20,24] 中。
列表 2：[0, 9, 12, 20]，20 在区间 [20,24] 中。
列表 3：[5, 18, 22, 30]，22 在区间 [20,24] 中。
示例 2：

输入：nums = [[1,2,3],[1,2,3],[1,2,3]]
输出：[1,1]
 

提示：

nums.length == k
1 <= k <= 3500
1 <= nums[i].length <= 50
-105 <= nums[i][j] <= 105
nums[i] 按非递减顺序排列
'''

from heapq import heapify, heapreplace
from typing import List
'''
思路：贪心 堆
满足题意的区间，区间上下限分别在2个列表nums[i],nums[j]中。
因为nums[i]都是已排序的，可以用堆和贪心思路：
1、将nums中每个列表的首个元素加入堆中，记录此时的区间大小（也即堆中最大值和最小值）
2、从堆中弹出最小的那行元素，然后再将该行元素下一个值加入堆，如果区间变小，更新最小区间大小。
3、重复上述过程2，直至区间的左值所在的行已经遍历到最后一个元素，在此过程中得到的最小区间为答案。

时间复杂度：O(nklogk)，最多有数组中每个元素都进入一次堆，堆的大小为k
空间复杂度：O(k)，每行一个元素加入堆
'''


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap, rightVal = [(e[0], row, 0) for row, e in enumerate(nums)], max([e[0] for e in nums])  # 将每个行的首元素加入堆
        heapify(heap)
        minRangeSize, ans = rightVal - heap[0][0], [heap[0][0], rightVal]
        while len(nums[heap[0][1]]) - 1 > heap[0][2]:  # 如果区间右值所在的行不是最后一个元素，继续迭代，否则区间已经不能再缩小，退出
            nextVal = nums[heap[0][1]][heap[0][2] + 1]
            rightVal = max(rightVal, nextVal)
            heapreplace(heap, (nextVal, heap[0][1], heap[0][2] + 1))  # 将改行的下一个元素加入堆
            if rightVal - heap[0][0] < minRangeSize:  # 区间变小，更新答案
                minRangeSize = rightVal - heap[0][0]
                ans = [heap[0][0], rightVal]
        return ans


s = Solution()
print(s.smallestRange([[1, 2, 3], [1, 2, 3], [1, 2, 3]]))
