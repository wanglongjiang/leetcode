'''
字符串的最大公因子
对于字符串 S 和 T，只有在 S = T + ... + T（T 自身连接 1 次或多次）时，我们才认定 “T 能除尽 S”。

返回最长字符串 X，要求满足 X 能除尽 str1 且 X 能除尽 str2。

 

示例 1：

输入：str1 = "ABCABC", str2 = "ABC"
输出："ABC"
示例 2：

输入：str1 = "ABABAB", str2 = "ABAB"
输出："AB"
示例 3：

输入：str1 = "LEET", str2 = "CODE"
输出：""
 

提示：

1 <= str1.length <= 1000
1 <= str2.length <= 1000
str1[i] 和 str2[i] 为大写英文字母

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/greatest-common-divisor-of-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
思路：模拟数学中的gcd
首先确保str1较长，str2较短
1. 从索引0开始，匹配str1，str2的每个字符，如果中途有不相同的字符，返回False
2. 如果str2匹配完成，str1未匹配完成，str2需要从索引0开始，继续匹配str1
3. 如果str1匹配完成，str2未匹配完成，str2赋值给str1, str2剩余部分赋值给str2，重复上面1.2
4. 如果2个字符串同时匹配完成，那么str2即为最大公因子

时间复杂度：O(nlogn)
空间复杂度：O(n)
'''


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) < len(str2):
            str2, str1 = str1, str2
        i, j = 0, 0
        m, n = len(str1), len(str2)
        while i < m and j < n:
            while i < m and j < n and str1[i] == str2[j]:
                i += 1
                j += 1
            if i < m and j < n and str1[i] != str2[j]:  # 遇到不相同的字符，没有公因子
                return ''
            if i == m and j == n:  # 两个字符串都遍历到了最后，str2就是最大公因子
                return str2
            if i < m:  # str1未遍历完，str2遍历完，str2需要从0开始继续与str1对比
                j = 0
            else:
                return self.gcdOfStrings(str2, str2[j:])  # str1遍历完，str2未遍历完，str2与str2剩余的部分的公因子即为公因子
