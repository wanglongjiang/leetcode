'''
最多能完成排序的块
数组arr是[0, 1, ..., arr.length - 1]的一种排列，我们将这个数组分割成几个“块”，并将这些块分别进行排序。之后再连接起来，使得连接的结果和按升序排序后的原数组相同。

我们最多能将数组分成多少块？

示例 1:

输入: arr = [4,3,2,1,0]
输出: 1
解释:
将数组分成2块或者更多块，都无法得到所需的结果。
例如，分成 [4, 3], [2, 1, 0] 的结果是 [3, 4, 0, 1, 2]，这不是有序的数组。
示例 2:

输入: arr = [1,0,2,3,4]
输出: 4
解释:
我们可以把它分成两块，例如 [1, 0], [2, 3, 4]。
然而，分成 [1, 0], [2], [3], [4] 可以得到最多的块数。
注意:

arr 的长度在 [1, 10] 之间。
arr[i]是 [0, 1, ..., arr.length - 1]的一种排列。
'''
from typing import List
'''
思路：滑动窗口
一个能划分的最小数组需要满足如下要求：
子数组arr[i..j]，中最小值为i，最大值为j，子数组大小为j-i+1。
用2个指针遍历arr，找到所有满足上面的条件子数组

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        left, right, n = 0, 0, len(arr)
        ans = 0
        while right < n:
            hasMin = False  # 是否已经找到当前需要的最小值
            maxNum = float('-inf')  # 子数组最大值
            while not hasMin or maxNum != right - 1:  # 扩大窗口大小，直至找到最小值，且最大值与右边界索引相同
                if arr[right] == left:
                    hasMin = True
                maxNum = max(maxNum, arr[right])
                right += 1
            left = right
            ans += 1
        return ans


s = Solution()
print(s.maxChunksToSorted([4, 3, 2, 1, 0]))
print(s.maxChunksToSorted([1, 0, 2, 3, 4]))
print(s.maxChunksToSorted([1, 2, 0, 3]))
print(s.maxChunksToSorted([2, 0, 1]))
