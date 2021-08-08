'''
剑指 Offer II 002. 二进制加法
给定两个 01 字符串 a 和 b ，请计算它们的和，并以二进制字符串的形式输出。

输入为 非空 字符串且只包含数字 1 和 0。

 

示例 1:

输入: a = "11", b = "10"
输出: "101"
示例 2:

输入: a = "1010", b = "1011"
输出: "10101"
 

提示：

每个字符串仅由字符 '0' 或 '1' 组成。
1 <= a.length, b.length <= 10^4
字符串如果不是 "0" ，就都不含前导零。
 

注意：本题与主站 67 题相同：https://leetcode-cn.com/problems/add-binary/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/JFETK5
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
思路：数学
从右往左遍历2个字符串，做加法，进位

时间复杂度：O(n)
'''


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        longStr, shortStr = None, None
        if len(a) > len(b):
            longStr = list(a[i] for i in range(len(a)))
            shortStr = b
        else:
            longStr = list(b[i] for i in range(len(b)))
            shortStr = a
        n = len(longStr)
        m = len(shortStr)
        carry = 0
        for i in range(n):
            if i < m:
                carry += int(shortStr[m - i - 1])
            if carry == 0 and i >= m:
                break
            carry += int(longStr[n - i - 1])
            carry, remainder = divmod(carry, 2)
            longStr[n - i - 1] = str(remainder)
        if carry > 0:
            return '1' + ''.join(longStr)
        else:
            return ''.join(longStr)
