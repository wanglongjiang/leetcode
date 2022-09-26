'''
1653. 使字符串平衡的最少删除次数
给你一个字符串 s ，它仅包含字符 'a' 和 'b'​​​​ 。

你可以删除 s 中任意数目的字符，使得 s 平衡 。我们称 s 平衡的 当不存在下标对 (i,j) 满足 i < j 且 s[i] = 'b' 同时 s[j]= 'a' 。

请你返回使 s 平衡 的 最少 删除次数。

 

示例 1：

输入：s = "aababbab"
输出：2
解释：你可以选择以下任意一种方案：
下标从 0 开始，删除第 2 和第 6 个字符（"aababbab" -> "aaabbb"），
下标从 0 开始，删除第 3 和第 6 个字符（"aababbab" -> "aabbbb"）。
示例 2：

输入：s = "bbaaaaabb"
输出：2
解释：唯一的最优解是删除最前面两个字符。
 

提示：

1 <= s.length <= 105
s[i] 要么是 'a' 要么是 'b'​ 。​
'''
'''
思路：前缀和
计算每个索引处前面'b'的个数和后面'a'的个数，找到需要删除最少的索引

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def minimumDeletions(self, s: str) -> int:
        bcount = 0
        acount = sum(1 for char in s if char == 'a')
        ans = float('inf')
        for char in s:
            if char == 'a':
                acount -= 1
                ans = min(ans, acount + bcount)
            else:
                ans = min(ans, acount + bcount)
                bcount += 1
        return ans


s = Solution()
assert s.minimumDeletions("aababbab") == 2
assert s.minimumDeletions("bbaaaaabb") == 2
