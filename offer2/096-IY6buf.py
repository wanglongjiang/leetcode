'''
剑指 Offer II 096. 字符串交织
给定三个字符串 s1、s2、s3，请判断 s3 能不能由 s1 和 s2 交织（交错） 组成。

两个字符串 s 和 t 交织 的定义与过程如下，其中每个字符串都会被分割成若干 非空 子字符串：

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
交织 是 s1 + t1 + s2 + t2 + s3 + t3 + ... 或者 t1 + s1 + t2 + s2 + t3 + s3 + ...
提示：a + b 意味着字符串 a 和 b 连接。

 

示例 1：



输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
输出：true
示例 2：

输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
输出：false
示例 3：

输入：s1 = "", s2 = "", s3 = ""
输出：true
 

提示：

0 <= s1.length, s2.length <= 100
0 <= s3.length <= 200
s1、s2、和 s3 都由小写英文字母组成
 

注意：本题与主站 97 题相同： https://leetcode-cn.com/problems/interleaving-string/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/IY6buf
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
思路：动态规划
分析一下，s3为s1、s2交错构成，寻找动态规划最优子结构一般是自底向上能构成解。
设二维数组dp[m][n]，m为s1长度,n为s2长度。
那么dp[i][j]的含义是，s3的子串s3[0..i+j]是否由s1[i]和s[j]交替构成
状态转移方程为：
dp[i][j]= True, 如果s3[i+j]==s1[i]，且dp[i-1][j]==True
或者
dp[i][j]= True, 如果s3[i+j]==s2[j]，且dp[i][j-1]==True
如果不满足上面2条，则dp[i][j]=false

初始化：
dp[0][0]=true
dp[1..m][0]=s1[i]==s3[i]且dp[i-1][0]==true
dp[0][1..n]=s2[j]==s3[j]且dp[0][j-1]==true


时间复杂度：O(mn)
空间复杂度：O(mn)
'''


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        # 初始化
        dp[0][0] = True
        for i in range(1, m + 1):
            dp[i][0] = (s1[i - 1] == s3[i - 1]) and dp[i - 1][0]
        for j in range(1, n + 1):
            dp[0][j] = (s2[j - 1] == s3[j - 1]) and dp[0][j - 1]
        # 动态规划
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = (s3[i + j - 1] == s1[i - 1] and dp[i - 1][j]) or (s3[i + j - 1] == s2[j - 1] and dp[i][j - 1])
        return dp[m][n]
