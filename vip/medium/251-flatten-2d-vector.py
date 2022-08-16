'''
251. 展开二维向量
请设计并实现一个能够展开二维向量的迭代器。该迭代器需要支持 next 和 hasNext 两种操作。



示例：

Vector2D iterator = new Vector2D([[1,2],[3],[4]]);

iterator.next(); // 返回 1
iterator.next(); // 返回 2
iterator.next(); // 返回 3
iterator.hasNext(); // 返回 true
iterator.hasNext(); // 返回 true
iterator.next(); // 返回 4
iterator.hasNext(); // 返回 false


注意：

请记得 重置 在 Vector2D 中声明的类变量（静态变量），因为类变量会 在多个测试用例中保持不变，影响判题准确。请 查阅 这里。
你可以假定 next() 的调用总是合法的，即当 next() 被调用时，二维向量总是存在至少一个后续元素。


进阶：尝试在代码中仅使用 C++ 提供的迭代器 或 Java 提供的迭代器。
'''

from typing import List
'''
思路：设计
设计2个指针，p1指向第1维，p2指向第2维

时间复杂度：所有操作都是O(1)
'''


class Vector2D:
    def __init__(self, vec: List[List[int]]):
        self.vec = vec
        self.p1, self.p2 = 0, 0

    def next(self) -> int:
        val = self.vec[self.p1][self.p2]
        self.p2 += 1
        if self.p2 == len(self.vec[self.p1]):
            self.p2 = 0
            self.p1 += 1
        return val

    def hasNext(self) -> bool:
        return self.p1 < len(self.vec)


iterator = Vector2D([[1, 2], [3], [4]])

print(iterator.next())  # 返回 1
print(iterator.next())  # 返回 2
print(iterator.next())  # 返回 3
print(iterator.hasNext())  # 返回 true
print(iterator.hasNext())  # 返回 true
print(iterator.next())  # 返回 4
print(iterator.hasNext())  # 返回 false
