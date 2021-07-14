'''
RLE 迭代器
编写一个遍历游程编码序列的迭代器。

迭代器由 RLEIterator(int[] A) 初始化，其中 A 是某个序列的游程编码。更具体地，对于所有偶数 i，
A[i] 告诉我们在序列中重复非负整数值 A[i + 1] 的次数。

迭代器支持一个函数：next(int n)，它耗尽接下来的  n 个元素（n >= 1）并返回以这种方式耗去的最后一个元素。
如果没有剩余的元素可供耗尽，则  next 返回 -1 。

例如，我们以 A = [3,8,0,9,2,5] 开始，这是序列 [8,8,8,5,5] 的游程编码。这是因为该序列可以读作 “三个八，零个九，两个五”。

 

示例：

输入：["RLEIterator","next","next","next","next"], [[[3,8,0,9,2,5]],[2],[1],[1],[2]]
输出：[null,8,8,5,-1]
解释：
RLEIterator 由 RLEIterator([3,8,0,9,2,5]) 初始化。
这映射到序列 [8,8,8,5,5]。
然后调用 RLEIterator.next 4次。

.next(2) 耗去序列的 2 个项，返回 8。现在剩下的序列是 [8, 5, 5]。

.next(1) 耗去序列的 1 个项，返回 8。现在剩下的序列是 [5, 5]。

.next(1) 耗去序列的 1 个项，返回 5。现在剩下的序列是 [5]。

.next(2) 耗去序列的 2 个项，返回 -1。 这是由于第一个被耗去的项是 5，
但第二个项并不存在。由于最后一个要耗去的项不存在，我们返回 -1。
 

提示：

0 <= A.length <= 1000
A.length 是偶数。
0 <= A[i] <= 10^9
每个测试用例最多调用 1000 次 RLEIterator.next(int n)。
每次调用 RLEIterator.next(int n) 都有 1 <= n <= 10^9 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rle-iterator
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
import bisect
'''
思路：前缀和数组 二分查找
设数组nums为所有的可能序列数字，nums[0]=encoding[1],nums[1]=encoding[3]...
设前缀和数组prefixs[i] = encoding[i*2]+prefixs[i-1]
设当前指针p初始为-1，每次next，将p+n，然后在prefixs中二分查找p，找到的索引i在nums中的元素即为next的值

时间复杂度：每次next均为O(logn)
空间复杂度：O(n)
'''


class RLEIterator:
    def __init__(self, encoding: List[int]):
        n = len(encoding)
        self.nums, self.prefixs = [0] * (n // 2), [0] * (n // 2)
        for i in range(0, n, 2):
            self.nums[i >> 1] = encoding[i + 1]
            self.prefixs[i >> 1] = self.prefixs[(i >> 1) - 1] + encoding[i]
        self.p = 0

    def next(self, n: int) -> int:
        self.p += n
        if self.p <= self.prefixs[-1]:
            return self.nums[bisect.bisect_left(self.prefixs, self.p)]
        return -1


s = RLEIterator([3, 8, 0, 9, 2, 5])
print(s.next(2))
print(s.next(1))
print(s.next(1))
print(s.next(2))
