'''
扁平化嵌套列表迭代器

给你一个嵌套的整型列表。请你设计一个迭代器，使其能够遍历这个整型列表中的所有整数。

列表中的每一项或者为一个整数，或者是另一个列表。其中列表的元素也可能是整数或是其他列表。
'''


class NestedInteger:
    def __init__(self, val):
        self.val = val

    def isInteger(self) -> bool:
        return isinstance(self.val, int)

    def getInteger(self) -> int:
        return self.val

    def getList(self):
        return self.val


'''
思路：栈。因为嵌套深度不确定，每层都需要维护指针，通过栈来保存指针和嵌套list。
时间复杂度：next和hasNext都是O(1)
空间复杂度：
'''


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.lists = []
        self.indexs = []
        self.list = nestedList
        self.index = 0
        self.nextVal = None
        self.next()  # 取到第1个值

    def next(self) -> int:
        val = self.nextVal  # 已经取到的值暂存，待取完下一个值之后返回
        # 取下一个值，保存到self.nextVal
        while self.index < len(self.list) or len(self.lists) > 0:
            item = None
            if self.index < len(self.list):
                item = self.list[self.index]
                self.index += 1
            else:  # 当前list已经遍历完成，从栈中弹出上一层的list进行遍历
                self.index = self.indexs.pop()
                self.list = self.lists.pop()
            while item and not item.isInteger():  # 如果不是整数，需要入栈，保存当前list的迭代进度
                item = item.getList()
                if len(item) == 0:
                    if self.index < len(self.list):
                        item = self.list[self.index]
                        self.index += 1
                    else:
                        item = None
                        break  # 当前列表已经为空
                    continue  # 空list，跳过
                # 非空list，保存当前list的执行现场
                self.indexs.append(self.index)
                self.lists.append(self.list)
                # 当前list修改为新的
                self.index = 0
                self.list = item
                item = None
            if item and item.isInteger():
                self.nextVal = item.getInteger()
                break
        else:  # 没有可以供遍历的list，下一个值为空
            self.nextVal = None
        return val

    def hasNext(self) -> bool:
        return self.nextVal is not None


n = [NestedInteger([NestedInteger(1), NestedInteger(1)]), NestedInteger(2), NestedInteger([NestedInteger(1), NestedInteger(1)])]
s = NestedIterator(n)
while s.hasNext():
    print(s.next())
