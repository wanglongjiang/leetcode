'''
移掉K位数字
给定一个以字符串表示的非负整数 num，移除这个数中的 k 位数字，使得剩下的数字最小。

注意:

num 的长度小于 10002 且 ≥ k。
num 不会包含任何前导零。

示例 1 :

输入: num = "1432219", k = 3
输出: "1219"
解释: 移除掉三个数字 4, 3, 和 2 形成一个新的最小的数字 1219。
示例 2 :

输入: num = "10200", k = 1
输出: "200"
解释: 移掉首位的 1 剩下的数字为 200. 注意输出不能有任何前导零。
示例 3 :

输入: num = "10", k = 2
输出: "0"
解释: 从原数字移除所有的数字，剩余为空就是0。
'''
'''
思路：栈
如果数字的按照字典序升序，则数字最小
可以用一个单调栈来处理，依次读入每个数字，如果递增或等于则入栈
如果当前值小于栈底元素，需要出栈，每出栈1个，k减一直至k为0
时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = [0]  # 开头设置一个哨兵
        for c in num:
            n = int(c)
            while stack[-1] > n and k > 0:  # 发生递减后，将栈中的数值出栈，出栈的数字即为要丢弃的数字
                stack.pop()
                k -= 1
            if n > 0:  # 不能以0开头，故0不入栈
                stack.append(n)
        while k > 0:  # 从大到小丢弃数字
            stack.pop()
            k -= 1
        return ''.join(map(str, stack[1:]))


s = Solution()
print(s.removeKdigits(num="1432219", k=3))
print(s.removeKdigits(num="10200", k=1))
print(s.removeKdigits(num="10", k=2))
