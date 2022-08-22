'''
2384. 最大回文数字
给你一个仅由数字（0 - 9）组成的字符串 num 。

请你找出能够使用 num 中数字形成的 最大回文 整数，并以字符串形式返回。该整数不含 前导零 。

注意：

你 无需 使用 num 中的所有数字，但你必须使用 至少 一个数字。
数字可以重新排序。
 

示例 1：

输入：num = "444947137"
输出："7449447"
解释：
从 "444947137" 中选用数字 "4449477"，可以形成回文整数 "7449447" 。
可以证明 "7449447" 是能够形成的最大回文整数。
示例 2：

输入：num = "00009"
输出："9"
解释：
可以证明 "9" 能够形成的最大回文整数。
注意返回的整数不应含前导零。
 

提示：

1 <= num.length <= 105
num 由数字（0 - 9）组成
'''
'''
思路：贪心 计数
统计所有数字的个数，然后从9开始将个数大于1的数字添加到字符串上，最后将剩余的最大1个奇数各数字添加到字符串

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def largestPalindromic(self, num: str) -> str:
        numCount = [0] * 10
        for i in num:
            numCount[int(i)] += 1
        left = ''
        for i in range(9, 0, -1):
            if numCount[i] > 1:
                left += str(i) * (numCount[i] // 2)
                numCount[i] = numCount[i] % 2
        if numCount[0] > 1 and len(left) > 0:  # 为避免出现前导0，0需要单独处理
            left += '0' * (numCount[0] // 2)
            numCount[0] = numCount[0] % 2
        right = left[::-1]  # 字符串后半部分
        for i in range(9, -1, -1):
            if numCount[i]:
                left += str(i)
                break
        return left + right
