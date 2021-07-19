'''
判断子序列
给定字符串 s 和 t ，判断 s 是否为 t 的子序列。

字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。

进阶：

如果有大量输入的 S，称作 S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？

致谢：

特别感谢 @pbrother 添加此问题并且创建所有测试用例。

 

示例 1：

输入：s = "abc", t = "ahbgdc"
输出：true
示例 2：

输入：s = "axc", t = "ahbgdc"
输出：false
 

提示：

0 <= s.length <= 100
0 <= t.length <= 10^4
两个字符串都只由小写字符组成。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/is-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
思路：双指针
设置2个指针ps,pt分别指向s[0],t[0]
> 当s[ps]!=t[pt]时，向右移动pt
> 当s[ps]==t[pt]时，向右移动ps和pt
重复以上过程，直至ps==len(s)或者pt==len(t)
当ps==len(s)时，s是t的子序列

时间复杂度：O(mn),m=len(s),n=len(t)
空间复杂度：O(1)
'''


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        ps, pt = 0, 0
        while ps < m and pt < n:
            if s[ps] == t[pt]:
                ps += 1
            pt += 1
        return ps == m


s = Solution()
print(s.isSubsequence('axc', 'ahbgdc'))
