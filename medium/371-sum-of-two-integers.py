'''
两整数之和
不使用运算符 + 和 - ​​​​​​​，计算两整数 ​​​​​​​a 、b ​​​​​​​之和。

示例 1:

输入: a = 1, b = 2
输出: 3
示例 2:

输入: a = -2, b = 3
输出: 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sum-of-two-integers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
位运算
andOp = a&b是所有同时为1的位运算结果，如果相加需要进位，结果为向左移位(a&b)<<1
xorOp = a^b是任意1个有1的位运算结果。
递归执行上面运算，直至2者之一为0，返回另外一个数即可

时间复杂度：O(1)
空间复杂度：O(1)
'''


class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0x100000000
        while a & b:
            a, b = ((a & b) << 1) % mask, (a ^ b) % mask
        return a | b


s = Solution()
print(s.getSum(-1, 1))
