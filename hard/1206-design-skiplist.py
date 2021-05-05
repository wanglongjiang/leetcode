'''
设计跳表

不使用任何库函数，设计一个跳表。

跳表是在 O(log(n)) 时间内完成增加、删除、搜索操作的数据结构。跳表相比于树堆与红黑树，其功能与性能相当，
并且跳表的代码长度相较下更短，其设计思想与链表相似。

例如，一个跳表包含 [30, 40, 50, 60, 70, 90]，然后增加 80、45 到跳表中，以下图的方式操作：


Artyom Kalinin [CC BY-SA 3.0], via Wikimedia Commons

跳表中有很多层，每一层是一个短的链表。在第一层的作用下，增加、删除和搜索操作的时间复杂度不超过 O(n)。
跳表的每一个操作的平均时间复杂度是 O(log(n))，空间复杂度是 O(n)。

在本题中，你的设计应该要包含这些函数：

bool search(int target) : 返回target是否存在于跳表中。
void add(int num): 插入一个元素到跳表。
bool erase(int num): 在跳表中删除一个值，如果 num 不存在，直接返回false. 如果存在多个 num ，删除其中任意一个即可。
了解更多 : https:#en.wikipedia.org/wiki/Skip_list

注意，跳表中可能存在多个相同的值，你的代码需要处理这种情况。

样例:

Skiplist skiplist = new Skiplist()

skiplist.add(1)
skiplist.add(2)
skiplist.add(3)
skiplist.search(0)   # 返回 false
skiplist.add(4)
skiplist.search(1)   # 返回 true
skiplist.erase(0)    # 返回 false，0 不在跳表中
skiplist.erase(1)    # 返回 true
skiplist.search(1)   # 返回 false，1 已被擦除
约束条件:

0 <= num, target <= 20000
最多调用 50000 次 search, add, 以及 erase操作。
'''
'''
思路：使用随机、多级链表实现跳表
使用单向链表节点Node，它有2个指针，next指向同级的下一个节点，down指向下级节点
输入最大是50000次，可以使用16级的索引
为避免插入、删除操作造成2个索引间隔过大，使用randomLevel，50%的几率只在原表中插入，50%几率生成1级索引，25%几率生成2级索引，。。。

'''


class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next
        self.down = None


class Skiplist:
    def __init__(self):
        self.maxLvl = 16  # 最大层数为16，可以支持10万级的数据search、add、erase时间复杂度为O(logn)
        self.heads = [None] * self.maxLvl
        for i in range(self.maxLvl):
            self.heads[i] = Node(-1, Node(float('inf'), None))
        for i in range(self.maxLvl - 1):
            self.heads[i].down = self.heads[i + 1]

    def search(self, target: int) -> bool:
        p = self.heads[0]
        for lv in range(self.maxLvl):
            while p.next.val < target:  # 在这一层查找目标，找到>=目标后，进入下一层
                p = p.next
            if p.next.val == target:
                return True
            p = p.down
        return False

    def add(self, num: int) -> None:
        lvls = self.randomLevel()
        p = self.heads[0]
        needDInsPrev = []
        # 查找
        for lv in range(self.maxLvl):
            while p.next.val < num:
                p = p.next
            if (self.maxLvl - lv) <= lvls:  # 加入待插入list
                needDInsPrev.append(p)
            p = p.down
        # 插入
        for prev in needDInsPrev:
            prev.next = Node(num, prev.next)
        # 维护向下的指针
        for i in range(len(needDInsPrev) - 1):
            needDInsPrev[i].next.down = needDInsPrev[i + 1].next

    def erase(self, num: int) -> bool:
        p = self.heads[0]
        needDelPrev = []
        # 查找
        for lv in range(self.maxLvl):
            while p.next.val < num:
                p = p.next
            if p.next.val == num:  # 在该层找到目标，加入待删除list
                needDelPrev.append(p)
            p = p.down
        # 删除
        if len(needDelPrev) == 0:
            return False
        for prev in needDelPrev:
            prev.next = prev.next.next
        return True

    def randomLevel(self):
        import random
        lvl = 1
        for i in range(self.maxLvl - 1):
            if random.randint(0, 99) % 2:
                lvl += 1
            else:
                break
        return lvl


skiplist = Skiplist()

skiplist.add(1)
skiplist.add(2)
skiplist.add(3)
print(skiplist.search(0))  # 返回 false
skiplist.add(4)
print(skiplist.search(1))  # 返回 true
print(skiplist.erase(0))  # 返回 false，0 不在跳表中
print(skiplist.erase(1))  # 返回 true
print(skiplist.search(1))  # 返回 false，1 已被擦除
