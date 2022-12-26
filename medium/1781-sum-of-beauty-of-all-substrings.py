'''
1781. 所有子字符串美丽值之和
一个字符串的 美丽值 定义为：出现频率最高字符与出现频率最低字符的出现次数之差。

比方说，"abaacc" 的美丽值为 3 - 1 = 2 。
给你一个字符串 s ，请你返回它所有子字符串的 美丽值 之和。

 

示例 1：

输入：s = "aabcb"
输出：5
解释：美丽值不为零的字符串包括 ["aab","aabc","aabcb","abcb","bcb"] ，每一个字符串的美丽值都为 1 。
示例 2：

输入：s = "aabcbaa"
输出：17
 

提示：

1 <= s.length <= 500
s 只包含小写英文字母。
'''
'''
思路：前缀和
首先，统计截止每个下标的字符计数前缀和
然后，用二重循环遍历所有的子串下标组合，然后利用上面的前缀和计算出子串的字符数，进一步计算出美丽值

时间复杂度：O(n^2)
空间复杂度：O(n)
'''


class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        # 计算前缀和
        pre = [None] * (n + 1)
        pre[0] = [0] * 26
        for i in range(n):
            pre[i + 1] = pre[i].copy()
            pre[i + 1][ord(s[i]) - ord('a')] += 1
        # 遍历所有子串下标组合，计算美丽值
        ans = 0
        for i in range(n):
            for j in range(i + 2, n + 1):
                mx, mi = 0, float('inf')
                for cnt in [pre[j][k] - pre[i][k] for k in range(26)]:
                    if cnt > 0:
                        if cnt > mx:
                            mx = cnt
                        if cnt < mi:
                            mi = cnt
                if mi != float('inf'):
                    ans += mx - mi
        return ans


s = Solution()
print(s.beautySum("aabcb"))
print(s.beautySum("aabcbaa"))
