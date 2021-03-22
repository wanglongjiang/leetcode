'''
LCP 25. 古董键盘

小扣在秋日市集购买了一个古董键盘。由于古董键盘年久失修，键盘上只有 26 个字母 a~z 可以按下，且每个字母最多仅能被按 k 次。

小扣随机按了 n 次按键，请返回小扣总共有可能按出多少种内容。由于数字较大，最终答案需要对 1000000007 (1e9 + 7) 取模。

提示：

1 <= k <= 5
1 <= n <= 26*k
'''
'''
思路：重复排列问题。完全重复排列的公式为26^n，因这里每个字符最多出现k次，故当n>k时，后续需要底的数量。
'''


class Solution:
    def keyboard(self, k: int, n: int) -> int:
        base = 26
        ans = 1
        while n > 0:
            ans *= base**(k if n > k else n)
            base -= 1
            n -= k
        return ans % (10**9 + 7)


s = Solution()
print(s.keyboard(1, 2))
print(s.keyboard(1, 1))
