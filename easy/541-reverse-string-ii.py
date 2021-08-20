'''
反转字符串 II
给定一个字符串 s 和一个整数 k，从字符串开头算起，每 2k 个字符反转前 k 个字符。

如果剩余字符少于 k 个，则将剩余字符全部反转。
如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。
 

示例 1：

输入：s = "abcdefg", k = 2
输出："bacdfeg"
示例 2：

输入：s = "abcd", k = 2
输出："bacd"
 

提示：

1 <= s.length <= 10^4
s 仅由小写英文组成
1 <= k <= 10^4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-string-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
思路：模拟字符串遍历
模拟题意，进行字符串遍历

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        ans = [None] * n
        i = 0
        while i < n:
            for j in range(min(i + k, n) - 1, i - 1, -1):  # 遍历前k个字符
                ans[i] = s[j]
                i += 1
            for j in range(i, min(i + k, n)):  # 遍历后k个字符
                ans[i] = s[j]
                i += 1
        return ''.join(ans)


s = Solution()
print(s.reverseStr(s="abcdefg", k=2) == 'bacdfeg')
print(s.reverseStr(s="abcd", k=2) == 'bacd')
