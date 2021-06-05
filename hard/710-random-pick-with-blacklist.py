'''
黑名单中的随机数
给定一个包含 [0，n) 中不重复整数的黑名单 blacklist ，写一个函数从 [0, n) 中返回一个不在 blacklist 中的随机整数。

对它进行优化使其尽量少调用系统方法 Math.random() 。

提示:

1 <= n <= 1000000000
0 <= blacklist.length < min(100000, N)
[0, n) 不包含 n ，详细参见 interval notation 。
示例 1：

输入：
["Solution","pick","pick","pick"]
[[1,[]],[],[],[]]
输出：[null,0,0,0]
示例 2：

输入：
["Solution","pick","pick","pick"]
[[2,[]],[],[],[]]
输出：[null,1,1,1]
示例 3：

输入：
["Solution","pick","pick","pick"]
[[3,[1]],[],[],[]]
输出：[null,0,0,2]
示例 4：

输入：
["Solution","pick","pick","pick"]
[[4,[2]],[],[],[]]
输出：[null,1,3,1]
输入语法说明：

输入是两个列表：调用成员函数名和调用的参数。Solution的构造函数有两个参数，n 和黑名单 blacklist。
pick 没有参数，输入参数是一个列表，即使参数为空，也会输入一个 [] 空列表。

'''
from typing import List
import bisect
import random
'''
思路：排序 随机 二分查找
初始化函数：
1. 将黑名单进行排序，然后遍历黑名单，生成白名单区间list:whitelist
2. 再遍历whitelist，生成白名单区间长度前缀和数组lenPrefixs
3. 白名单的整数总数为m=n-blacklist.length
时间复杂度：O(klogk)，k=blacklist.length

pick函数：
1. 调用系统的random，生成0..m-1的一个随机整数randIdx
2. 在lenPrefixs中二分查找randIdx，定位到白名单区间的索引，然后在白名单区间内定位到一个整数
时间复杂度：O(log(whitelist.length))
'''


class Solution:
    def __init__(self, n: int, blacklist: List[int]):
        self.m = n - len(blacklist)
        blacklist.sort()
        self.whitelist = []
        self.lenPrefis = []
        total = 0
        if blacklist:
            if blacklist[0]:  # 第1个黑名单不是0，需要在最开始添加一个白名单区间
                self.whitelist.append((0, blacklist[0] - 1))
                self.lenPrefis.append(blacklist[0])
                total += blacklist[0]
            pre = blacklist[0]
            for i in range(1, len(blacklist)):
                pre += 1
                if pre != blacklist[i]:  # 当前数不是前数+1，2个黑名单数之间有空洞，需要添加为白名单
                    self.whitelist.append((pre, blacklist[i] - 1))
                    total += blacklist[i] - pre
                    self.lenPrefis.append(total)
                    pre = blacklist[i]
            if blacklist[-1] != n - 1:  # 最后一个黑名单不是n-1，需要追加1个白名单区间
                self.whitelist.append((blacklist[-1] + 1, n - 1))
                total += n - 1 - blacklist[-1]
                self.lenPrefis.append(total)
        else:
            self.whitelist.append((0, n))
            self.lenPrefis.append(n)

    def pick(self) -> int:
        randIdx = random.randint(0, self.m - 1)
        rangeIdx = bisect.bisect_right(self.lenPrefis, randIdx)  # 二分查找定位随机索引处于哪个白名单区间
        if 0 < rangeIdx < len(self.whitelist):
            randIdx -= self.lenPrefis[rangeIdx - 1]  # 定位随机索引在白名单区间内的偏移量
            return self.whitelist[rangeIdx][0] + randIdx
        elif rangeIdx == len(self.whitelist):
            randIdx -= self.lenPrefis[-1]  # 定位随机索引在白名单区间内的偏移量
            return self.whitelist[-1][0] + randIdx
        return self.whitelist[0][0] + randIdx


s = Solution(3, [0])
print(s.pick())
print(s.pick())
print(s.pick())
print(s.pick())
print(s.pick())

s = Solution(4, [2])
print(s.pick())
print(s.pick())
print(s.pick())
print(s.pick())
print(s.pick())
