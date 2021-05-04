'''
剑指 Offer 59 - I. 滑动窗口的最大值
给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。
示例:

输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7]
解释:

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
 

提示：

你可以假设 k 总是有效的，在输入数组不为空的情况下，1 ≤ k ≤ 输入数组的大小。

注意：本题与主站 239 题相同：https://leetcode-cn.com/problems/sliding-window-maximum/
'''
from typing import List
'''
思路1，使用红黑树
每移动一次滑动窗口，将移出的元素从红黑树中删除，将新的元素加入红黑树，然后求最大值
红黑树使用java实现
时间复杂度：O(nlogk)
空间复杂度：O(logk)

思路2，最大堆
与红黑树类似，每移动一次窗口，将移出的元素从堆中删除，将新加入的元素加入堆，然后求最大值
最大堆用python
时间复杂度：O(nlogk)
空间复杂度：O(logk)
'''


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        if k == 1:
            return nums
        n = len(nums)
        if k == n:
            return [max(nums)]
        heap = MaxHeap(nums, k)  # 创建堆
        ans = []
        ans.append(heap.getMax())
        for j in range(k, n):  # 滑动窗口
            i = j - k
            heap.replace(i, j)  # 移出最左侧元素，移入最右侧元素
            ans.append(heap.getMax())
        return ans


class MaxHeap:
    def __init__(self, nums, k):
        self.size = k
        self.heap = nums[:k]
        self.arrIdxToheapIdx = {}
        self.heapIdxToArrIdx = {}
        for i in range(k):
            self.arrIdxToheapIdx[i] = i
            self.heapIdxToArrIdx[i] = i
        self.nums = nums
        self.build()

    # 建堆
    def build(self):
        for i in range(self.size // 2, -1, -1):
            self.maxHeapify(i)

    # 将i元素替换为j元素
    def replace(self, i, j):
        heapIndex = self.arrIdxToheapIdx[i]
        del self.arrIdxToheapIdx[i]
        self.arrIdxToheapIdx[j] = heapIndex
        self.heapIdxToArrIdx[heapIndex] = j
        self.heap[heapIndex] = self.nums[j]
        if self.nums[i] < self.nums[j]:
            self.promote(heapIndex, self.nums[j])
        elif self.nums[i] > self.nums[j]:
            self.maxHeapify(heapIndex)

    # 提升某个值在堆中的位置
    def promote(self, i, val):
        while i > 0 and self.heap[self.parent(i)] < val:  # 将大于父节点的值向上提升
            self.swap(i, self.parent(i))
            i = self.parent(i)

    # 保持最大堆的性质
    def maxHeapify(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        maxIndex = i
        # 如果左、右子节点大于父节点，不满足最大堆性质，需要将父节点与左或右节点交换，使之满足最大堆性质
        if left < self.size and self.heap[left] > self.heap[maxIndex]:
            maxIndex = left
        if right < self.size and self.heap[right] > self.heap[maxIndex]:
            maxIndex = right
        if maxIndex != i:
            self.swap(maxIndex, i)
            self.maxHeapify(maxIndex)  # 交换后子节点可能不满足最大堆性质，需要递归向下执行

    # 交换堆中2个元素
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        heapIndexI, heapIndexJ = self.heapIdxToArrIdx[i], self.heapIdxToArrIdx[j]
        self.heapIdxToArrIdx[i], self.heapIdxToArrIdx[j] = heapIndexJ, heapIndexI
        self.arrIdxToheapIdx[heapIndexI], self.arrIdxToheapIdx[heapIndexJ] = j, i

    # 求父节点的索引
    def parent(self, i):
        return (i - 1) // 2

    def getMax(self):
        return self.heap[0]

    def notEmpty(self):
        return self.size > 0


s = Solution()
print(s.maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))
print(s.maxSlidingWindow(nums=[1], k=1))
print(s.maxSlidingWindow(nums=[1, -1], k=1))
print(s.maxSlidingWindow(nums=[9, 11], k=2))
print(s.maxSlidingWindow(nums=[4, -2], k=2))
