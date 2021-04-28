'''
回文子串
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。

提示：

输入的字符串长度不会超过 1000 。
'''
'''
思路1，暴力搜索
判断任意2个坐标的组合内的子字符串是否为回文，需要3重循环
第1、2重用于生成坐标组合，第3重判断回文
时间复杂度：O(n^3)
空间复杂度：O(1)

思路2，动态规划
设一个二维数组m[0..n-1][0..n-1]，对于其中的元素m[i][j]代表s[i..j]是否为回文
如果s[i..j]已经判断出是否为回文，则s[i-1..j+1]可以通过m[i][j] and s[i-1]==s[j+1]来判断
时间复杂度：O(n^2)
空间复杂度：O(n^2)
'''


class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        m = [[1] * n for _ in range(n)]  # 默认所有子串都是回文，是为了使单个字符都是回文
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if not (s[i] == s[j] and m[i + 1][j - 1]):
                    m[i][j] = 0
        return sum([sum(a) for a in m]) - ((n * n - n) // 2)  # 返回所有的回文串数量，因为只有i<=j才是合法的坐标，所以需要减掉矩阵的对角线一半


s = Solution()
print(s.countSubstrings("abc"))
print(s.countSubstrings("aaa"))
