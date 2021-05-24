'''
奇怪的打印机
有台奇怪的打印机有以下两个特殊要求：

打印机每次只能打印由 同一个字符 组成的序列。
每次可以在任意起始和结束位置打印新字符，并且会覆盖掉原来已有的字符。
给你一个字符串 s ，你的任务是计算这个打印机打印它需要的最少打印次数。

 
示例 1：

输入：s = "aaabbb"
输出：2
解释：首先打印 "aaa" 然后打印 "bbb"。
示例 2：

输入：s = "aba"
输出：2
解释：首先打印 "aaa" 然后在第二个位置打印 "b" 覆盖掉原来的字符 'a'。
 

提示：

1 <= s.length <= 100
s 由小写英文字母组成
'''
'''
思路：动态规划
连续相同的字符肯定一次能打印
如果当前是第i个字符，前面没有相同的字符，打印次数肯定是s[i-1]之前的字符串打印次数+1
如果当前是第i个字符，前面有s[a]==s[i]，a+1<i（也就是s[i]与s[a]相同，中间有间隔的其他字符），那么怎么计算截止到s[i]最少打印次数呢
可以考虑s[i]与s[a]一次打印，那么s[0]..s[a-1]之间的打印次数+s[a+1]..s[a-1]的打印次数+1即为s[0]..s[i]的打印次数
还有可能s[i]之前还有s[b]==s[i]，那么还要计算s[b]与s[i]同一次打印时的打印次数，算法按照s[a]的方式进行计算。
经过上面的思考，可以得到动态规划状态转移方程。
设二维数组dp，dp[i][j]指字符串s从i到j这个子串的打印次数，设i<j
dp[0][0] = 1
dp[i][j] = 如果s[j]==s[j-1]，那么dp[i][j-1]
dp[i][j] = min(dp[i][j-1]+1, (如果有i<a<j，s[a]==s[j]则:dp[i][a]+dp[a+1][j-1])...)
最后返回值是dp[0][n-1]

时间复杂度：O(n^3)，动态规划数组遍历需要O(n^2)，dp每个元素的计算需要向前搜索相同的字符
空间复杂度：O(n^2)
'''


class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = [[1] * n for _ in range(n)]
        for j in range(n):
            for i in range(j - 1, -1, -1):
                if s[j] == s[j - 1]:  # 当前字符与上一个字符相同，需要打印次数与上一个字符打印次数相同
                    dp[i][j] = dp[i][j - 1]
                else:  # 当前字符与上一个不同，最多需要上一个打印次数+1
                    dp[i][j] = dp[i][j - 1] + 1
                    # 下面搜索所有与s[j]相同的字符，尝试与s[j]同一次打印
                    k = i
                    while k < j:
                        while k < j and s[j] != s[k]:  # 找到与s[j]相同的字符
                            k += 1
                        if k < j:
                            t = dp[i][k]  # s[k]的子串的打印次数
                            while k < j and s[j] == s[k]:  # 跳过所有的与s[j]相同的字符
                                k += 1
                            if k < j:
                                t += dp[k][j - 1]  # 加上s[k]后面的子串的打印次数
                            dp[i][j] = min(dp[i][j], t)
        return dp[0][n - 1]


s = Solution()
print(s.strangePrinter('abaca'))
print(s.strangePrinter("baacdddaaddaaaaccbddbcabdaabdbbcdcbbbacbddcabcaaa"))
print(s.strangePrinter('abcbcba'))
print(s.strangePrinter('abcdefedcb'))
print(s.strangePrinter('aba'))
print(s.strangePrinter('aaabbb'))
