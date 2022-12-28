'''
2516. 每种字符至少取 K 个
中等
15
相关企业
给你一个由字符 'a'、'b'、'c' 组成的字符串 s 和一个非负整数 k 。每分钟，你可以选择取走 s 最左侧 还是 最右侧 的那个字符。

你必须取走每种字符 至少 k 个，返回需要的 最少 分钟数；如果无法取到，则返回 -1 。

 

示例 1：

输入：s = "aabaaaacaabc", k = 2
输出：8
解释：
从 s 的左侧取三个字符，现在共取到两个字符 'a' 、一个字符 'b' 。
从 s 的右侧取五个字符，现在共取到四个字符 'a' 、两个字符 'b' 和两个字符 'c' 。
共需要 3 + 5 = 8 分钟。
可以证明需要的最少分钟数是 8 。
示例 2：

输入：s = "a", k = 1
输出：-1
解释：无法取到一个字符 'b' 或者 'c'，所以返回 -1 。
 

提示：

1 <= s.length <= 105
s 仅由字母 'a'、'b'、'c' 组成
0 <= k <= s.length
'''
from collections import Counter
'''
[TOC]

# 思路
双指针

# 解题方法
从左向右遍历s，统计3个字符个数，
- 如果能够找到k个3种字符
- 如果不能找到k个3种字符，返回-1

# 复杂度
- 时间复杂度: 
> $O(n)$ 

- 空间复杂度: 
> $O(1)$
'''


class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        j = n = len(s)
        c = Counter()
        while c['a'] < k or c['b'] < k or c['c'] < k:
            if j == 0:
                return -1  # 所有字母都取也无法满足要求
            j -= 1
            c[s[j]] += 1
        ans = n - j  # 左侧没有取字符
        for i, ch in enumerate(s):
            c[ch] += 1
            while j < n and c[s[j]] > k:  # 维护 j 的最大下标
                c[s[j]] -= 1
                j += 1
            ans = min(ans, i + 1 + n - j)
            if j == n:
                break
        return ans
