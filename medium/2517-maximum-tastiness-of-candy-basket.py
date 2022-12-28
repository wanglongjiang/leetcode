'''
2517. 礼盒的最大甜蜜度
中等
13
相关企业
给你一个正整数数组 price ，其中 price[i] 表示第 i 类糖果的价格，另给你一个正整数 k 。

商店组合 k 类 不同 糖果打包成礼盒出售。礼盒的 甜蜜度 是礼盒中任意两种糖果 价格 绝对差的最小值。

返回礼盒的 最大 甜蜜度。

 

示例 1：

输入：price = [13,5,1,8,21,2], k = 3
输出：8
解释：选出价格分别为 [13,5,21] 的三类糖果。
礼盒的甜蜜度为 min(|13 - 5|, |13 - 21|, |5 - 21|) = min(8, 8, 16) = 8 。
可以证明能够取得的最大甜蜜度就是 8 。
示例 2：

输入：price = [1,3,1], k = 2
输出：2
解释：选出价格分别为 [1,3] 的两类糖果。 
礼盒的甜蜜度为 min(|1 - 3|) = min(2) = 2 。
可以证明能够取得的最大甜蜜度就是 2 。
示例 3：

输入：price = [7,7,7,7], k = 2
输出：0
解释：从现有的糖果中任选两类糖果，甜蜜度都会是 0 。
 

提示：

1 <= price.length <= 105
1 <= price[i] <= 109
2 <= k <= price.length
'''
from typing import List
'''
[TOC]

# 思路
二分查找

# 解题方法
设绝对差为x，遍历一次price，可以得到此时满足条件的糖果数量y。

如果y>=k，则x可以增大
如果y<k，则x必须缩小

# 复杂度
- 时间复杂度: 
> $O(n)$ 

- 空间复杂度: 
> $O(1)$
'''


class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        low, high = 0, price[-1] - price[0]
        ans = low
        while low <= high:
            x = (high + low) // 2
            y, cur = 1, price[0]
            for val in price:
                if val >= cur + x:
                    y += 1
                    cur = val
            if y >= k:
                ans = x
                low = x + 1
            else:
                high = x - 1
        return ans


s = Solution()
assert s.maximumTastiness(price=[1, 3, 1], k=2) == 2
assert s.maximumTastiness(price=[13, 5, 1, 8, 21, 2], k=3) == 8
assert s.maximumTastiness(price=[7, 7, 7, 7], k=2) == 0
