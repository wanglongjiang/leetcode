'''
字符串相加
给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。

 

提示：

num1 和num2 的长度都小于 5100
num1 和num2 都只包含数字 0-9
num1 和num2 都不包含任何前导零
你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
思路：模拟
模拟加法，从低到高做加法

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)
        ans = [0] * max(m, n)
        carry = 0
        p, p1, p2 = len(ans) - 1, m - 1, n - 1
        while p1 >= 0 or p2 >= 0:
            ans[p] = carry
            if p1 >= 0:
                ans[p] += int(num1[p1])
            if p2 >= 0:
                ans[p] += int(num2[p2])
            if ans[p] >= 10:
                ans[p] -= 10
                carry = 1
            else:
                carry = 0
            p -= 1
            p1 -= 1
            p2 -= 1
        return ('1' if carry else '') + ''.join(map(str, ans))


s = Solution()
print(s.addStrings('1', '9'))
