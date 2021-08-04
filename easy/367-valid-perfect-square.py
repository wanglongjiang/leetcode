'''
有效的完全平方数
给定一个 正整数 num ，编写一个函数，如果 num 是一个完全平方数，则返回 true ，否则返回 false 。

进阶：不要 使用任何内置的库函数，如  sqrt 。

 

示例 1：

输入：num = 16
输出：true
示例 2：

输入：num = 14
输出：false
 

提示：

1 <= num <= 2^31 - 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-perfect-square
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
思路：数学 暴力计算
从1开始依次计算平方，判断是否与num相同，直至平方>num停止

时间复杂度：O(sqrt(num))
空间复杂度：O(1)
'''


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i, t = 1, 1
        while t < num:
            i += 1
            t = i * i
        return t == num
