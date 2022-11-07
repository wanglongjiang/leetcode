'''
LCP 68. 美观的花束
中等
11
相关企业
力扣嘉年华的花店中从左至右摆放了一排鲜花，记录于整型一维矩阵 flowers 中每个数字表示该位置所种鲜花的品种编号。
你可以选择一段区间的鲜花做成插花，且不能丢弃。 在你选择的插花中，如果每一品种的鲜花数量都不超过 cnt 朵，
那么我们认为这束插花是 「美观的」。

例如：[5,5,5,6,6] 中品种为 5 的花有 3 朵， 品种为 6 的花有 2 朵，每一品种 的数量均不超过 3
请返回在这一排鲜花中，共有多少种可选择的区间，使得插花是「美观的」。

注意：

答案需要以 1e9 + 7 (1000000007) 为底取模，如：计算初始结果为：1000000008，请返回 1
示例 1：

输入：flowers = [1,2,3,2], cnt = 1

输出：8

解释：相同的鲜花不超过 1 朵，共有 8 种花束是美观的； 长度为 1 的区间 [1]、[2]、[3]、[2] 均满足条件，
共 4 种可选择区间 长度为 2 的区间 [1,2]、[2,3]、[3,2] 均满足条件，共 3 种可选择区间 长度为 3 的区间 [1,2,3] 满足条件，
共 1 种可选择区间。 区间 [2,3,2],[1,2,3,2] 都包含了 2 朵鲜花 2 ，不满足条件。 返回总数 4+3+1 = 8

示例 2：

输入：flowers = [5,3,3,3], cnt = 2

输出：8

提示：

1 <= flowers.length <= 10^5
1 <= flowers[i] <= 10^5
1 <= cnt <= 10^5
'''
from collections import Counter
from typing import List
'''
[TOC]

# 思路
滑动窗口

# 解题方法
> 设一个滑动窗口，将滑动窗口内的元素加入哈希表进行计数，如果窗口内的某种元素不大于cnt，则扩大窗口大小，否则缩小
> 滑动过程中，用等差序列求和公式计算美观的子数组个数

# 复杂度
- 时间复杂度: 
>  $O(n)$

- 空间复杂度: 
> $O(cnt)$
'''


class Solution:
    def beautifulBouquet(self, flowers: List[int], cnt: int) -> int:
        counter = Counter()
        left, right, n = 0, 0, len(flowers)
        ans, m = 0, 10**9 + 7
        while right < n:
            maxItem = 0
            while right < n:  # 扩大滑动窗口大小，直至窗口内某种元素大于cnt
                counter[flowers[right]] += 1
                right += 1
                if counter[flowers[right - 1]] > cnt:
                    maxItem = flowers[right - 1]
                    break
                ans = (ans + right - left) % m
            while left < right:  # 缩小滑动窗口大小
                counter[flowers[left]] -= 1
                left += 1
                if flowers[left - 1] == maxItem:
                    ans = (ans + right - left) % m
                    break
        return ans


s = Solution()
assert s.beautifulBouquet(flowers=[1, 2, 3, 2], cnt=1) == 8
assert s.beautifulBouquet(flowers=[5, 3, 3, 3], cnt=2) == 8
