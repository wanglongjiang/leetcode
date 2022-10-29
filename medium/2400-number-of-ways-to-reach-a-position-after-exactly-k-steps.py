'''
2400. 恰好移动 k 步到达某一位置的方法数目
给你两个 正 整数 startPos 和 endPos 。最初，你站在 无限 数轴上位置 startPos 处。在一步移动中，你可以向左或者向右移动一个位置。

给你一个正整数 k ，返回从 startPos 出发、恰好 移动 k 步并到达 endPos 的 不同 方法数目。由于答案可能会很大，返回对 109 + 7 取余 的结果。

如果所执行移动的顺序不完全相同，则认为两种方法不同。

注意：数轴包含负整数。

 

示例 1：

输入：startPos = 1, endPos = 2, k = 3
输出：3
解释：存在 3 种从 1 到 2 且恰好移动 3 步的方法：
- 1 -> 2 -> 3 -> 2.
- 1 -> 2 -> 1 -> 2.
- 1 -> 0 -> 1 -> 2.
可以证明不存在其他方法，所以返回 3 。
示例 2：

输入：startPos = 2, endPos = 5, k = 10
输出：0
解释：不存在从 2 到 5 且恰好移动 10 步的方法。
 

提示：

1 <= startPos, endPos, k <= 1000
'''

from functools import cache
'''
定义 f(x, \textit{left})f(x,left) 表示当前在 xx，还剩 \textit{left}left 步时，走到终点的方案数。

枚举下一步往左或者往右，累加即为答案。

注意在递归过程中如果 |x-\textit{endPos}| > \textit{left}∣x−endPos∣>left，由于无法到达 \textit{endPos}endPos，可以直接返回 00，表示无效方案。

'''


class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        MOD = 10**9 + 7

        @cache
        def f(x: int, left: int) -> int:
            if abs(x - endPos) > left:
                return 0
            if left == 0:
                return 1  # 成功到达终点，算一种方案
            return (f(x - 1, left - 1) + f(x + 1, left - 1)) % MOD

        return f(startPos, k)
