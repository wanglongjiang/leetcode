'''
剑指 Offer II 020. 回文子字符串的个数
给定一个字符串 s ，请计算这个字符串中有多少个回文子字符串。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。

 

示例 1：

输入：s = "abc"
输出：3
解释：三个回文子串: "a", "b", "c"
示例 2：

输入：s = "aaa"
输出：6
解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"
 

提示：

1 <= s.length <= 1000
s 由小写英文字母组成
 

注意：本题与主站 647 题相同：https://leetcode-cn.com/problems/palindromic-substrings/ 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/a7VOhD
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
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
        m = [[1] * n for _ in range(n)]  # 默认所有单个字符构成的子串都是回文
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if not (s[i] == s[j] and m[i + 1][j - 1]):
                    m[i][j] = 0
        return sum([sum(a) for a in m]) - ((n * n - n) // 2)  # 返回所有的回文串数量，因为只有i<=j才是合法的坐标，所以需要减掉矩阵的对角线一半
