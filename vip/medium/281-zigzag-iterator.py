'''
281. 锯齿迭代器
给出两个一维的向量，请你实现一个迭代器，交替返回它们中间的元素。

示例:

输入:
v1 = [1,2]
v2 = [3,4,5,6]

输出: [1,3,2,4,5,6]

解析: 通过连续调用 next 函数直到 hasNext 函数返回 false，
     next 函数返回值的次序应依次为: [1,3,2,4,5,6]。
拓展：假如给你 k 个一维向量呢？你的代码在这种情况下的扩展性又会如何呢?

拓展声明：
 “锯齿” 顺序对于 k > 2 的情况定义可能会有些歧义。所以，假如你觉得 “锯齿” 这个表述不妥，也可以认为这是一种 “循环”。例如：

输入:
[1,2,3]
[4,5,6,7]
[8,9]

输出: [1,4,8,2,5,9,3,6,7].
'''
from typing import List
'''
思路：设计一个能扩展到k个一维向量的迭代器
将向量保存到矩阵中。
设变量i,j为当前未遍历的元素坐标，初始为0，0
next函数返回i,j指向的元素，并移动到下一个位置
hasNext判断是否为有效坐标
'''


class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int], v3=[]):
        self.mat = [v1, v2]
        if v3:
            self.mat.append(v3)
        self.i, self.j = 0, 0

    def next(self) -> int:
        val = self.mat[self.i][self.j]
        self.i = (self.i + 1) % len(self.mat)
        self.j += 1 if self.i == 0 else 0  # 如果发生了换行，列索引也要+1
        step = 1  # 记录为查找下一个元素一共移动了多少步
        while len(self.mat[self.i]) <= self.j and step <= len(self.mat):  # 如果该向量的长度小于等于j，需要移动到下一个位置
            self.i = (self.i + 1) % len(self.mat)
            self.j += 1 if self.i == 0 else 0  # 如果发生了换行，列索引也要+1
            step += 1
        return val

    def hasNext(self) -> bool:
        return len(self.mat[self.i]) > self.j


s = ZigzagIterator([1, 2, 3], [4, 5, 6, 7], [8, 9])
while s.hasNext():
    print(s.next())
