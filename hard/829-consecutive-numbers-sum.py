'''
连续整数求和
给定一个正整数 N，试求有多少组连续正整数满足所有数字之和为 N?

示例 1:

输入: 5
输出: 2
解释: 5 = 5 = 2 + 3，共有两组连续整数([5],[2,3])求和后为 5。
示例 2:

输入: 9
输出: 3
解释: 9 = 9 = 4 + 5 = 2 + 3 + 4
示例 3:

输入: 15
输出: 4
解释: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
说明: 1 <= N <= 10 ^ 9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/consecutive-numbers-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
思路：数学 枚举
根据等差序列的性质:
s=(a1+an)*n/2
an=a1+n-1
那么
2s=(2a1+n-1)*n
可以对2s进行因数分解，分解出来的2个因子a=n,b=(2a1+a-1)
a的取值范围为1..sqrt(2s)
(b-a+1)/2=a1，也即(b-a+1)/2为整数时，a1有合法的整数解，能找到连续的数列

时间复杂度：O(sqrt(n))
'''


class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        n *= 2
        ans = 0
        for a in range(1, int(n**0.5) + 1):
            b, r = divmod(n, a)
            if r == 0 and (b - a + 1) % 2 == 0:
                ans += 1
        return ans


s = Solution()
print(s.consecutiveNumbersSum(5))
