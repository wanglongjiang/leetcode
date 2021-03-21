'''
顶端迭代器
给定一个迭代器类的接口，接口包含两个方法： next() 和 hasNext()。
设计并实现一个支持 peek() 操作的顶端迭代器 -- 其本质就是把原本应由 next() 方法返回的元素 peek() 出来。
'''


class Iterator:
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """
        pass

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """
        pass

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """
        pass


'''
思路：设置一个变量peeked用于暂存peek的结果，当发生peek时执行iterator的next，结果保存到peeked中。
    在执行next，或者 hasNext时都需要先查看peeked中有没有变量。
时间复杂度：O(1)
空间复杂度：O(1)
'''


class PeekingIterator:
    def __init__(self, iterator):
        self.iter = iterator
        self.peeked = None

    def peek(self):
        if self.peeked is not None:
            return self.peeked
        self.peeked = self.iter.next()
        return self.peeked

    def next(self):
        if self.peeked is not None:
            ans = self.peeked
            self.peeked = None
            return ans
        return self.iter.next()

    def hasNext(self):
        if self.peeked is not None:
            return True
        else:
            return self.iter.hasNext()
