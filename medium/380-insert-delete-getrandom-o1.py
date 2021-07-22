'''
O(1) 时间插入、删除和获取随机元素
设计一个支持在平均 时间复杂度 O(1) 下，执行以下操作的数据结构。

insert(val)：当元素 val 不存在时，向集合中插入该项。
remove(val)：元素 val 存在时，从集合中移除该项。
getRandom：随机返回现有集合中的一项。每个元素应该有相同的概率被返回。
示例 :

// 初始化一个空的集合。
RandomizedSet randomSet = new RandomizedSet();

// 向集合中插入 1 。返回 true 表示 1 被成功地插入。
randomSet.insert(1);

// 返回 false ，表示集合中不存在 2 。
randomSet.remove(2);

// 向集合中插入 2 。返回 true 。集合现在包含 [1,2] 。
randomSet.insert(2);

// getRandom 应随机返回 1 或 2 。
randomSet.getRandom();

// 从集合中移除 1 ，返回 true 。集合现在包含 [2] 。
randomSet.remove(1);

// 2 已在集合中，所以返回 false 。
randomSet.insert(2);

// 由于 2 是集合中唯一的数字，getRandom 总是返回 2 。
randomSet.getRandom();
'''
from random import choice
'''
思路：哈希+数组
根据官方思路
哈希表中保存val和在数组中的索引
数组中保存val，在insert时每次都保存到最后
在remove时，要把待删除的数据与数组末尾的进行交换，删除末尾

时间复杂度：O(1)
'''


class RandomizedSet:
    def __init__(self):
        self.hashmap = {}
        self.li = []

    def insert(self, val: int) -> bool:
        if val not in self.hashmap:
            self.hashmap[val] = len(self.li)
            self.li.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.hashmap:
            i = self.hashmap[val]
            del self.hashmap[val]
            if i != len(self.li) - 1:
                self.li[i], self.li[-1] = self.li[-1], self.li[i]
                self.hashmap[self.li[i]] = i
            self.li.pop()
            return True
        return False

    def getRandom(self) -> int:
        return choice(self.li)


s = RandomizedSet()
s.insert(0)
s.insert(1)
s.remove(0)
s.insert(2)
s.remove(1)
print(s.getRandom())
