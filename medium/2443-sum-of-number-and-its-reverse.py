'''
2443. 反转之后的数字和
给你一个 非负 整数 num 。如果存在某个 非负 整数 k 满足 k + reverse(k) = num  ，则返回 true ；否则，返回 false 。

reverse(k) 表示 k 反转每个数位后得到的数字。

 

示例 1：

输入：num = 443
输出：true
解释：172 + 271 = 443 ，所以返回 true 。
示例 2：

输入：num = 63
输出：false
解释：63 不能表示为非负整数及其反转后数字之和，返回 false 。
示例 3：

输入：num = 181
输出：true
解释：140 + 041 = 181 ，所以返回 true 。注意，反转后的数字可能包含前导零。
 

提示：

0 <= num <= 105
'''
'''
思路：枚举
从0枚举到num/2，得到num分解后的2个数字a、b，如果b的反转是a，返回true

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        for a in range(num // 2 + 1):
            b = num - a
            if int(str(b)[::-1]) == a:
                return True
        return False
