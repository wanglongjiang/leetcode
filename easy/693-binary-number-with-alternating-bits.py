'''
交替位二进制数
给定一个正整数，检查它的二进制表示是否总是 0、1 交替出现：换句话说，就是二进制表示中相邻两位的数字永不相同。

 

示例 1：

输入：n = 5
输出：true
解释：5 的二进制表示是：101
示例 2：

输入：n = 7
输出：false
解释：7 的二进制表示是：111.
示例 3：

输入：n = 11
输出：false
解释：11 的二进制表示是：1011.
示例 4：

输入：n = 10
输出：true
解释：10 的二进制表示是：1010.
示例 5：

输入：n = 3
输出：false
 

提示：

1 <= n <= 2^31 - 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-number-with-alternating-bits
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
思路：位运算
设变量bit初始值为n的第0位，
然后遍历n的每一位：
> 如果bit与n的当前位不相同，返回false
> 如果相同，将bit取反
依次检查每位的值

时间复杂度：O(1)，最大32位
空间复杂度：O(1)
'''


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bit = n & 0x1
        while n > 0:
            if bit != (n & 0x1):
                return False
            bit ^= 0x1
            n >>= 1
        return True
