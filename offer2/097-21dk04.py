'''
剑指 Offer II 097. 子序列的数目
给定一个字符串 s 和一个字符串 t ，计算在 s 的子序列中 t 出现的个数。

字符串的一个 子序列 是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE" 是 "ABCDE" 的一个子序列，而 "AEC" 不是）

题目数据保证答案符合 32 位带符号整数范围。

 

示例 1：

输入：s = "rabbbit", t = "rabbit"
输出：3
解释：
如下图所示, 有 3 种可以从 s 中得到 "rabbit" 的方案。
rabbbit
rabbbit
rabbbit
示例 2：

输入：s = "babgbag", t = "bag"
输出：5
解释：
如下图所示, 有 5 种可以从 s 中得到 "bag" 的方案.
babgbag
babgbag
babgbag
babgbag
babgbag
 

提示：

0 <= s.length, t.length <= 1000
s 和 t 由英文字母组成
 

注意：本题与主站 115 题相同： https://leetcode-cn.com/problems/distinct-subsequences/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/21dk04
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
思路1，回溯+记忆表
    1、首先t匹配s最左侧的子序列。
    2、从t的最右边字符开始，依次向右寻找下一个匹配位置，如果找到，回溯调用左边字符的向右搜索。
'''


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        lens, lent = len(s), len(t)
        count = 0
        # 先找到第1个匹配子序列,并将所匹配的s中的索引记录下来
        ps, pt = 0, 0
        sindexs = [0] * lent
        while ps < lens and pt < lent:
            while ps < lens and pt < lent and s[ps] == t[pt]:
                sindexs[pt] = ps
                ps += 1
                pt += 1
            ps += 1
        if pt == lent:  # 找到了第1个匹配位置，将数量设置为1
            count = 1
        else:
            return 0
        # 记忆数组
        dp = [[-1] * (lens + 1) for i in range(lens + 1)]

        # 回溯查找所有可能的匹配组合,先在s中查找t的最右边字符，查找方向为从目前已匹配位置到右侧边界。然后查找次右边字符
        def backtrack(index, end):
            if dp[index][end] >= 0:  # 如果记忆数组中已经有结果，直接返回
                return dp[index][end]
            cnt = 0
            for i in range(sindexs[index] + 1, end):
                if s[i] == t[index]:  # 找到一个匹配
                    cnt += 1
                    if index > 0:  # 如果不是t的第1个字符，需要继续搜索
                        cnt += backtrack(index - 1, i)
            if index > 0:  # 该字符不动，尝试移动前面的字符进行匹配
                cnt += backtrack(index - 1, sindexs[index])
            dp[index][end] = cnt
            return cnt

        return count + backtrack(lent - 1, lens)
