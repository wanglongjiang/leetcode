'''
604. 迭代压缩字符串
对于一个压缩字符串，设计一个数据结构，它支持如下两种操作： next 和 hasNext。

给定的压缩字符串格式为：每个字母后面紧跟一个正整数，这个整数表示该字母在解压后的字符串里连续出现的次数。

next() - 如果压缩字符串仍然有字母未被解压，则返回下一个字母，否则返回一个空格。
hasNext() - 判断是否还有字母仍然没被解压。

注意：

请记得将你的类在 StringIterator 中 初始化 ，因为静态变量或类变量在多组测试数据中不会被自动清空。更多细节请访问 这里 。

示例：

StringIterator iterator = new StringIterator("L1e2t1C1o1d1e1");

iterator.next(); // 返回 'L'
iterator.next(); // 返回 'e'
iterator.next(); // 返回 'e'
iterator.next(); // 返回 't'
iterator.next(); // 返回 'C'
iterator.next(); // 返回 'o'
iterator.next(); // 返回 'd'
iterator.hasNext(); // 返回 true
iterator.next(); // 返回 'e'
iterator.hasNext(); // 返回 false
iterator.next(); // 返回 ' '
'''
'''
思路：设计
设1个指针，指向下一个待遍历字符索引
设1个变量char，保存当前字符
设1个计数器，指向当前字符剩余的字符
详细算法见代码

时间复杂度：O(1)
'''


class StringIterator:
    def __init__(self, compressedString: str):
        self.compressedString = compressedString
        self.i = 0
        self.count = 0
        self.char = ' '

    def next(self) -> str:
        if not self.hasNext():
            return ' '
        if self.count == 0:
            self.char = self.compressedString[self.i]
            self.i += 1
            j = self.i
            while self.i < len(self.compressedString) and self.compressedString[self.i].isdigit():
                self.i += 1
            self.count = int(self.compressedString[j:self.i])
        self.count -= 1
        return self.char

    def hasNext(self) -> bool:
        if self.i == len(self.compressedString) and self.count == 0:
            return False
        return True


iterator = StringIterator('L1e2t1C1o1d1e1')
print(iterator.next())  # 返回 'L'
print(iterator.next())  # 返回 'e'
print(iterator.next())  # 返回 'e'
print(iterator.next())  # 返回 't'
print(iterator.next())  # 返回 'C'
print(iterator.next())  # 返回 'o'
print(iterator.next())  # 返回 'd'
print(iterator.hasNext())  # 返回 true
print(iterator.next())  # 返回 'e'
print(iterator.hasNext())  # 返回 false
print(iterator.next())  # 返回 ' '
