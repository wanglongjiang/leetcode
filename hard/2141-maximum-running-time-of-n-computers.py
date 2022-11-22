'''
2141. 同时运行 N 台电脑的最长时间
困难
60
相关企业
你有 n 台电脑。给你整数 n 和一个下标从 0 开始的整数数组 batteries ，其中第 i 个电池可以让一台电脑 运行 batteries[i] 分钟。
你想使用这些电池让 全部 n 台电脑 同时 运行。

一开始，你可以给每台电脑连接 至多一个电池 。然后在任意整数时刻，你都可以将一台电脑与它的电池断开连接，并连接另一个电池，
你可以进行这个操作 任意次 。新连接的电池可以是一个全新的电池，也可以是别的电脑用过的电池。断开连接和连接新的电池不会花费任何时间。

注意，你不能给电池充电。

请你返回你可以让 n 台电脑同时运行的 最长 分钟数。

 

示例 1：



输入：n = 2, batteries = [3,3,3]
输出：4
解释：
一开始，将第一台电脑与电池 0 连接，第二台电脑与电池 1 连接。
2 分钟后，将第二台电脑与电池 1 断开连接，并连接电池 2 。注意，电池 0 还可以供电 1 分钟。
在第 3 分钟结尾，你需要将第一台电脑与电池 0 断开连接，然后连接电池 1 。
在第 4 分钟结尾，电池 1 也被耗尽，第一台电脑无法继续运行。
我们最多能同时让两台电脑同时运行 4 分钟，所以我们返回 4 。
示例 2：



输入：n = 2, batteries = [1,1,1,1]
输出：2
解释：
一开始，将第一台电脑与电池 0 连接，第二台电脑与电池 2 连接。
一分钟后，电池 0 和电池 2 同时耗尽，所以你需要将它们断开连接，并将电池 1 和第一台电脑连接，电池 3 和第二台电脑连接。
1 分钟后，电池 1 和电池 3 也耗尽了，所以两台电脑都无法继续运行。
我们最多能让两台电脑同时运行 2 分钟，所以我们返回 2 。
 

提示：

1 <= n <= batteries.length <= 105
1 <= batteries[i] <= 109
'''
from math import inf
from typing import List
'''
[TOC]

# 思路
二分查找

# 解题方法
设最长运行时间为x，电池数量为m
- 如果batteries[i]>=x，这块电池最多消耗掉x，剩余部分会浪费掉
- 如果batteries[i]<x，这块电池可以全部使用掉。所有的<x的电池可以灵活切换，最大化利用。

也就是，如果设运行时间为x，设>=x的电池为a个，这些电池一直挂着利用率最高，然后剩余的m-a块<x的电池可以计算总容量，除以m-a得到运行时间。
- 如果这个运行时间>x，那么可以将x增大。
- 如果运行时间<x，需要将x减小
- 如果运行时间=x，即为答案

使用二分查找进行上述计算过程

# 复杂度
- 时间复杂度: 
> $O(mlog(sum(batteries)/n))$ ，x最小值为1，最大值为sum(batteries)/n，也即所有电池都平均用光的时间

- 空间复杂度: 
> $O(1)$
'''


class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        if len(batteries) == n:  # 特殊情况，电池与电脑数量一样，取决于最小的电池
            return min(batteries)
        low, high = min(batteries), sum(batteries) // n
        while low < high:
            x = (low + high) // 2
            remainder, total = n, 0
            for b in batteries:
                if b >= x:
                    remainder -= 1  # 大电池已经满足一个电脑运行x分钟，需要将这个电脑去掉
                else:
                    total += b  # 累计小电池
            time = inf if remainder <= 0 else total // remainder
            if time == x:
                return x
            if time > x:
                low = x + 1
            else:
                high = x - 1
        return high


s = Solution()
assert s.maxRunTime(n=2, batteries=[3, 3, 3]) == 4
assert s.maxRunTime(n=2, batteries=[1, 1, 1, 1]) == 2
assert s.maxRunTime(n=2, batteries=[4, 3]) == 3
assert s.maxRunTime(n=2, batteries=[4, 4, 2]) == 5
