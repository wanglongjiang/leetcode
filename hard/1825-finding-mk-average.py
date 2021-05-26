'''
求出 MK 平均值
给你两个整数 m 和 k ，以及数据流形式的若干整数。你需要实现一个数据结构，计算这个数据流的 MK 平均值 。

MK 平均值 按照如下步骤计算：

如果数据流中的整数少于 m 个，MK 平均值 为 -1 ，否则将数据流中最后 m 个元素拷贝到一个独立的容器中。
从这个容器中删除最小的 k 个数和最大的 k 个数。
计算剩余元素的平均值，并 向下取整到最近的整数 。
请你实现 MKAverage 类：

MKAverage(int m, int k) 用一个空的数据流和两个整数 m 和 k 初始化 MKAverage 对象。
void addElement(int num) 往数据流中插入一个新的元素 num 。
int calculateMKAverage() 对当前的数据流计算并返回 MK 平均数 ，结果需 向下取整到最近的整数 。
 

示例 1：

输入：
["MKAverage", "addElement", "addElement", "calculateMKAverage", "addElement", "calculateMKAverage",
"addElement", "addElement", "addElement", "calculateMKAverage"]
[[3, 1], [3], [1], [], [10], [], [5], [5], [5], []]
输出：
[null, null, null, -1, null, 3, null, null, null, 5]

解释：
MKAverage obj = new MKAverage(3, 1)
obj.addElement(3)        # 当前元素为 [3]
obj.addElement(1)        # 当前元素为 [3,1]
obj.calculateMKAverage() # 返回 -1 ，因为 m = 3 ，但数据流中只有 2 个元素
obj.addElement(10)       # 当前元素为 [3,1,10]
obj.calculateMKAverage() # 最后 3 个元素为 [3,1,10]
                          # 删除最小以及最大的 1 个元素后，容器为 [3]
                          # [3] 的平均值等于 3/1 = 3 ，故返回 3
obj.addElement(5)        # 当前元素为 [3,1,10,5]
obj.addElement(5)        # 当前元素为 [3,1,10,5,5]
obj.addElement(5)        # 当前元素为 [3,1,10,5,5,5]
obj.calculateMKAverage() # 最后 3 个元素为 [5,5,5]
                          # 删除最小以及最大的 1 个元素后，容器为 [5]
                          # [5] 的平均值等于 5/1 = 5 ，故返回 5
 

提示：

3 <= m <= 10^5
1 <= k*2 < m
1 <= num <= 10^5
addElement 与 calculateMKAverage 总操作次数不超过 10^5 次。
'''
from collections import Counter
from collections import deque
from sortedcontainers import SortedList
'''
思路：队列+平衡二叉树
设1个队列q，保持数据流中最多m个元素
设3个平衡二叉树的实现sortedList：minK,maxK,mid，保存最小、最大、中间的k、k、m-2k个元素

算法如下：
如果数据流小于m，暂存到数值中。
一旦数据流大于等于m，则：
> 将最大的k个数加入最小堆
> 将最小的k个数加入最大堆
> 剩余的数求和total，记住不在最大最小堆中的数据个数count

后续每加入一个新的元素num，
> 如果大于最大k个数中的最小数，将其替换最大k个数中最小数a，此时calculateMKAverage结果为(total+a)/(count+1)
> 如果小于最小k个数中的最大数，将其替换最小k个数中最大数a，此时calculateMKAverage结果为(total+a)/(count+1)

时间复杂度：单次addElement为O(logk)，触发建堆的那一次addElement的时间复杂度为O(mlogk)，单次calculateMKAverage为O(1)
空间复杂度：O(k)，需要2个k大小的堆

TODO 第15个测试案例未通过
'''


class MKAverage:
    def __init__(self, m: int, k: int):
        self.minK = SortedList()
        self.maxK = SortedList()
        self.mid = SortedList()
        self.q = deque(maxlen=m)
        self.count = m - 2 * k
        self.total = 0
        self.avg = -1
        self.data = []
        self.m = m
        self.k = k

    def addElement(self, num: int) -> None:
        if len(self.data) < self.m - 1:
            self.data.append(num)
            return
        if len(self.data) == self.m - 1:
            self.data.append(num)
            self.initHeap()
            return
        # 将队头的元素删除
        front = self.q.popleft()
        self.q.append(num)
        if front in self.mid:
            self.total -= front
            self.mid.remove(front)
        elif front in self.minK:
            self.minK.remove(front)
        else:
            self.maxK.remove(front)
        # 将新元素加入
        if len(self.minK) != 0 and num < self.minK[-1]:
            self.minK.add(num)
        elif len(self.maxK) != 0 and num > self.maxK[0]:
            self.maxK.add(num)
        else:
            self.mid.add(num)
            self.total += num
        # 检查3个分区大小是否正常，如果不正常，进行调整
        if len(self.minK) > self.k:
            val = self.minK[-1]
            self.mid.add(val)
            self.total += val
            del self.minK[-1]
        elif len(self.minK) < self.k:
            val = self.mid[0]
            self.minK.add(val)
            self.total -= val
            del self.mid[0]
        if len(self.mid) > self.k:
            val = self.mid[-1]
            self.maxK.add(val)
            self.total -= val
            del self.mid[-1]
        elif len(self.mid) < self.k:
            val = self.maxK[0]
            self.mid.add(val)
            self.total += val
            del self.maxK[0]
        self.avg = self.total // self.count

    def initHeap(self):
        counter = Counter(self.data)
        # 将数据加入最大集最小集
        for num in self.data:
            self.q.append(num)
            if len(self.minK) < self.k:
                self.minK.add(num)
                self.maxK.add(num)
            else:
                if self.minK[-1] > num:
                    del self.minK[-1]
                    self.minK.add(num)
                if self.maxK[0] < num:
                    del self.maxK[0]
                    self.maxK.add(num)
        for i in range(self.k):
            counter[self.minK[i]] -= 1
            counter[self.maxK[i]] -= 1
        # 将剩余的元素加入mid
        self.total = 0
        for val in counter.elements():
            self.total += val
            self.mid.add(val)
        self.avg = self.total // self.count

    def calculateMKAverage(self) -> int:
        return self.avg


obj = MKAverage(3, 1)
obj.addElement(3)  # 当前元素为 [3]
obj.addElement(1)  # 当前元素为 [3,1]
print(obj.calculateMKAverage())  # 返回 -1 ，因为 m = 3 ，但数据流中只有 2 个元素
obj.addElement(10)  # 当前元素为 [3,1,10]
print(obj.calculateMKAverage())  # 最后 3 个元素为 [3,1,10]
# 删除最小以及最大的 1 个元素后，容器为 [3]
# [3] 的平均值等于 3/1 = 3 ，故返回 3
obj.addElement(5)  # 当前元素为 [3,1,10,5]
obj.addElement(5)  # 当前元素为 [3,1,10,5,5]
obj.addElement(5)  # 当前元素为 [3,1,10,5,5,5]
print(obj.calculateMKAverage())  # 最后 3 个元素为 [5,5,5]
# 删除最小以及最大的 1 个元素后，容器为 [5]
# [5] 的平均值等于 5/1 = 5 ，故返回 5

obj = MKAverage(3, 1)
obj.addElement(17612)  # 当前元素为 [3]
obj.addElement(74607)  # 当前元素为 [3,1]
print(obj.calculateMKAverage())  # 返回 -1 ，因为 m = 3 ，但数据流中只有 2 个元素
obj.addElement(8272)  # 当前元素为 [3,1,10]
obj.addElement(33433)  # 当前元素为 [3,1,10,5]
print(obj.calculateMKAverage())  # 最后 3 个元素为 [3,1,10]
# 删除最小以及最大的 1 个元素后，容器为 [3]
# [3] 的平均值等于 3/1 = 3 ，故返回 3
obj.addElement(15456)  # 当前元素为 [3,1,10,5,5]
obj.addElement(64938)  # 当前元素为 [3,1,10,5,5,5]
print(obj.calculateMKAverage())  # 最后 3 个元素为 [5,5,5]
obj.addElement(99741)  # 当前元素为 [3,1,10,5,5,5]
# 删除最小以及最大的 1 个元素后，容器为 [5]
# [5] 的平均值等于 5/1 = 5 ，故返回 5
