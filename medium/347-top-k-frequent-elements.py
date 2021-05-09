'''
前 K 个高频元素
给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。
示例 1:

输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
示例 2:

输入: nums = [1], k = 1
输出: [1]
 

提示：

1 <= nums.length <= 105
k 的取值范围是 [1, 数组中不相同的元素的个数]
题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的
 

进阶：你所设计算法的时间复杂度 必须 优于 O(n log n) ，其中 n 是数组大小。
'''
from typing import List
'''
思路：计数+堆
1、先对所有的元素进行计数
2、对元素按照计数的大小进行建立大小为k的最小堆，元素依次入堆，如果计数>堆中最小值，替换最小元素。直至所有元素都尝试入堆完毕。
时间复杂度：O(nlogk)，堆的建立需要nlogk
空间复杂度：O(n)，需要大小为n的哈希表及大小为k的堆
'''


# 定义最小堆
class MinHeap:
    def __init__(self):
        self.heap = []
        self.size = 0

    # 向堆中插入值
    def insert(self, item):
        self.heap.append(item)
        i = self.size
        self.size += 1
        while i > 0 and self.heap[self.parent(i)][1] > item[1]:  # 将小于父节点的值向上提升
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    # 替换堆中最小元素
    def tryReplaceMin(self, item):
        if item[1] > self.heap[0][1]:
            self.heap[0] = item
            self.minHeapify(0)

    # 保持最小堆的性质
    def minHeapify(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        minIndex = i
        # 如果左、右子节点小于父节点，不满足最小堆性质，需要将父节点与左或右节点交换，使之满足最小堆性质
        if left < self.size and self.heap[left][1] < self.heap[minIndex][1]:
            minIndex = left
        if right < self.size and self.heap[right][1] < self.heap[minIndex][1]:
            minIndex = right
        if minIndex != i:
            self.heap[minIndex], self.heap[i] = self.heap[i], self.heap[minIndex]
            self.minHeapify(minIndex)  # 交换后子节点可能不满足最小堆性质，需要递归向下执行

    # 求父节点的索引
    def parent(self, i):
        return (i - 1) // 2

    def getMin(self):
        return self.heap[0]

    def notEmpty(self):
        return self.size > 0


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        # 1、元素计数
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1

        # 2、将元素加入堆中，堆的大小保持最大为k
        heap = MinHeap()
        for item in counter.items():
            if heap.size < k:
                heap.insert(item)
            else:
                heap.tryReplaceMin(item)
        return [item[0] for item in heap.heap]


s = Solution()
print(s.topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2))
print(s.topKFrequent(nums=[1], k=1))
