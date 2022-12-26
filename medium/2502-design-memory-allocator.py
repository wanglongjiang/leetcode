'''
2502. 设计内存分配器
中等
4
相关企业
给你一个整数 n ，表示下标从 0 开始的内存数组的大小。所有内存单元开始都是空闲的。

请你设计一个具备以下功能的内存分配器：

分配 一块大小为 size 的连续空闲内存单元并赋 id mID 。
释放 给定 id mID 对应的所有内存单元。
注意：

多个块可以被分配到同一个 mID 。
你必须释放 mID 对应的所有内存单元，即便这些内存单元被分配在不同的块中。
实现 Allocator 类：

Allocator(int n) 使用一个大小为 n 的内存数组初始化 Allocator 对象。
int allocate(int size, int mID) 找出大小为 size 个连续空闲内存单元且位于  最左侧 的块，分配并赋 id mID 。返回块的第一个下标。如果不存在这样的块，返回 -1 。
int free(int mID) 释放 id mID 对应的所有内存单元。返回释放的内存单元数目。
 

示例：

输入
["Allocator", "allocate", "allocate", "allocate", "free", "allocate", "allocate", "allocate", "free", "allocate", "free"]
[[10], [1, 1], [1, 2], [1, 3], [2], [3, 4], [1, 1], [1, 1], [1], [10, 2], [7]]
输出
[null, 0, 1, 2, 1, 3, 1, 6, 3, -1, 0]

解释
Allocator loc = new Allocator(10); // 初始化一个大小为 10 的内存数组，所有内存单元都是空闲的。
loc.allocate(1, 1); // 最左侧的块的第一个下标是 0 。内存数组变为 [1, , , , , , , , , ]。返回 0 。
loc.allocate(1, 2); // 最左侧的块的第一个下标是 1 。内存数组变为 [1,2, , , , , , , , ]。返回 1 。
loc.allocate(1, 3); // 最左侧的块的第一个下标是 2 。内存数组变为 [1,2,3, , , , , , , ]。返回 2 。
loc.free(2); // 释放 mID 为 2 的所有内存单元。内存数组变为 [1, ,3, , , , , , , ] 。返回 1 ，因为只有 1 个 mID 为 2 的内存单元。
loc.allocate(3, 4); // 最左侧的块的第一个下标是 3 。内存数组变为 [1, ,3,4,4,4, , , , ]。返回 3 。
loc.allocate(1, 1); // 最左侧的块的第一个下标是 1 。内存数组变为 [1,1,3,4,4,4, , , , ]。返回 1 。
loc.allocate(1, 1); // 最左侧的块的第一个下标是 6 。内存数组变为 [1,1,3,4,4,4,1, , , ]。返回 6 。
loc.free(1); // 释放 mID 为 1 的所有内存单元。内存数组变为 [ , ,3,4,4,4, , , , ] 。返回 3 ，因为有 3 个 mID 为 1 的内存单元。
loc.allocate(10, 2); // 无法找出长度为 10 个连续空闲内存单元的空闲块，所有返回 -1 。
loc.free(7); // 释放 mID 为 7 的所有内存单元。内存数组保持原状，因为不存在 mID 为 7 的内存单元。返回 0 。
 

提示：

1 <= n, size, mID <= 1000
最多调用 allocate 和 free 方法 1000 次
'''
'''
[TOC]

# 思路
设计 哈希表

# 解题方法
- 用哈希表used保存已分配的内存块，key为mId，val为[(开始地址，结束地址),(开始地址，结束地址)...]
- 用大小为n的列表bitmap保存所有的内存块的mID

根据以上的数据结构：
- allocate()逻辑如下
> 遍历bitmap，找到的第1个连续为0的大小为size的内存块分配给mid，将开始地址加入used。

- free()逻辑如下：
> 用key找到所有符合要求的内存块，遍历所有的内存块，将其响应位置置为0

# 复杂度
- 时间复杂度: 
> allocate()因为每次都需要遍历所有内存块，需要$O(n)$ 
> free()，也需要$O(n)$ 

- 空间复杂度: 
> $O(n)$
'''


class Allocator:
    def __init__(self, n: int):
        self.n = n
        self.used = {}
        self.bitmap = [0] * n

    def allocate(self, size: int, mID: int) -> int:
        length = 0
        for i in range(self.n):
            if self.bitmap[i] == 0:
                length += 1
                if length == size:  # 找到连续大小为size的空间
                    if mID not in self.used:
                        self.used[mID] = []
                    self.used[mID].append((i - length + 1, i))
                    for addr in range(i - length + 1, i + 1):
                        self.bitmap[addr] = mID
                    return i - length + 1
            else:
                length = 0
        return -1

    def free(self, mID: int) -> int:
        if mID not in self.used:
            return 0
        ans = 0
        for start, end in self.used[mID]:
            ans += end - start + 1
            for addr in range(start, end + 1):
                self.bitmap[addr] = 0
        del self.used[mID]
        return ans
