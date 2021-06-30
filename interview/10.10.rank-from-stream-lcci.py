'''
面试题 10.10. 数字流的秩
假设你正在读取一串整数。每隔一段时间，你希望能找出数字 x 的秩(小于或等于 x 的值的个数)。请实现数据结构和算法来支持这些操作，也就是说：

实现 track(int x) 方法，每读入一个数字都会调用该方法；

实现 getRankOfNumber(int x) 方法，返回小于或等于 x 的值的个数。

注意：本题相对原题稍作改动

示例:

输入:
["StreamRank", "getRankOfNumber", "track", "getRankOfNumber"]
[[], [1], [0], [0]]
输出:
[null,0,null,1]
提示：

x <= 50000
track 和 getRankOfNumber 方法的调用次数均不超过 2000 次
'''
'''
思路：树状数组
该题目就是为树状数组而诞生的。。。
track将x..n区间的所有计数+1
getRankOfNumber累计0..x区间的所有计数
注意x从0开始，需要做一下偏移，将x+1，使其从1开始

时间复杂度：track，getRankOfNumber时间复杂度都是O(logx)
空间复杂度：O(n)
'''


class StreamRank:
    def __init__(self):
        self.n = 50001
        self.c = [0] * (self.n + 1)

    def lowbit(self, x):
        return x & -x

    def track(self, x: int) -> None:
        x += 1
        while x <= self.n:
            self.c[x] += 1
            x += self.lowbit(x)

    def getRankOfNumber(self, x: int) -> int:
        x += 1
        ans = 0
        while x > 0:
            ans += self.c[x]
            x -= self.lowbit(x)
        return ans


s = StreamRank()
print(s.getRankOfNumber(1))
s.track(0)
print(s.getRankOfNumber(0))
