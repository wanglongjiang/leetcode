'''
解码方法
一条包含字母 A-Z 的消息通过以下映射进行了 编码 ：

'A' -> 1
'B' -> 2
...
'Z' -> 26
要 解码 已编码的消息，所有数字必须基于上述映射的方法，反向映射回字母（可能有多种方法）。
例如，"111" 可以将 "1" 中的每个 "1" 映射为 "A" ，从而得到 "AAA" ，
或者可以将 "11" 和 "1"（分别为 "K" 和 "A" ）映射为 "KA" 。注意，"06" 不能映射为 "F" ，因为 "6"和"06" 不同。

给你一个只含数字的 非空 字符串 num ，请计算并返回 解码 方法的 总数 。

题目数据保证答案肯定是一个 32 位 的整数。

'''
'''
解题思路：动态规划
设置一个动态规划数组dp[n]，每个元素dp[i]的代表的意思是字符串截止到s[i]的解码数量
有动态转移方程如下：
dp[0]：如果s[0]==1~9，为1；如果s[0]==0，为0。
dp[1]：如果s[0..1]<=26，为2；否则为1。
dp[i]，i>1：
    如果s[i]==0且s[i-1]==1or2，dp[i]==dp[i-1];如果s[i-1]!=1 or 2，没有合法的解，返回0
    如果s[i]==1且s[i+1]==0，s[i]必须与s[i+1]结合到一起，解码数没有变化，dp[i]=dp[i-1]
        如果s[i+1]!=0 or i+1>=n，且s[i-1]<=2 ，s[i]可以独立或者与前面结合，dp[i]=dp[i-1]+dp[i-2]
        如果s[i+1]!=0 or i+1>=n，且s[i-1]>2，s[i]必须独立，dp[i]=dp[i-1]
    如果s[i]==2且s[i+1]==0，s[i]必须与s[i+1]结合到一起，解码数没有变化，dp[i]=dp[i-1]
        如果s[i+1]!=0 or i+1>=n，且s[i-1]<=2 ，s[i]可以独立或者与前面结合，dp[i]=dp[i-1]+1
        如果s[i+1]!=0 or i+1>=n，且s[i-1]>2，s[i]必须独立，dp[i]=dp[i-1]
    如果s[i]==3~9且s[i-1]==1，或者 s[i]==3~6 且s[i-1]==2 则：dp[i]=dp[i-1]+1
    不满足上面的条件，dp[i]=dp[i-1]
时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [-1] * n
        if s[0] == '0':
            return 0
        dp[0] = 1
        if n == 1:
            return dp[0]
        two = int(s[0:2])
        if two > 26 and s[1] == '0':
            return 0
        elif two == 10 or two == 20 or two > 26:
            dp[1] = 1
        else:
            dp[1] = 2

        for i in range(2, n):
            if s[i] == '0':
                if s[i - 1] == '1' or s[i - 1] == '2':
                    dp[i] = dp[i - 2]
                else:
                    return 0
            elif s[i] == '1' or s[i] == '2':
                if i + 1 < n and s[i + 1] == '0':
                    dp[i] = dp[i - 1]
                else:
                    if s[i - 1] == '1' or s[i - 1] == '2':
                        dp[i] = dp[i - 1] + dp[i - 2]
                    else:
                        dp[i] = dp[i - 1]
            elif s[i] >= '3' and s[i] <= '9' and s[i - 1] == '1':
                dp[i] = dp[i - 1] + +dp[i - 2]
            elif s[i] >= '3' and s[i] <= '6' and s[i - 1] == '2':
                dp[i] = dp[i - 1] + +dp[i - 2]
            else:
                dp[i] = dp[i - 1]

        return dp[n - 1]


s = Solution()
print(s.numDecodings("10"))
print(s.numDecodings("27"))
print(s.numDecodings("1123"))
print(s.numDecodings("12"))
print(s.numDecodings("226"))
print(s.numDecodings("0"))
print(s.numDecodings("06"))
print(s.numDecodings("120"))
print(s.numDecodings("11"))
print(s.numDecodings("111"))
print(s.numDecodings("1111"))
print(s.numDecodings("11111"))
