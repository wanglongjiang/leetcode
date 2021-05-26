'''
给表达式添加运算符
给定一个仅包含数字 0-9 的字符串和一个目标值，在数字之间添加 二元 运算符（不是一元）+、- 或 * ，返回所有能够得到目标值的表达式。


示例 1:

输入: num = "123", target = 6
输出: ["1+2+3", "1*2*3"]
示例 2:

输入: num = "232", target = 8
输出: ["2*3+2", "2+3*2"]
示例 3:

输入: num = "105", target = 5
输出: ["1*0+5","10-5"]
示例 4:

输入: num = "00", target = 0
输出: ["0+0", "0-0", "0*0"]
示例 5:

输入: num = "3456237490", target = 9191
输出: []
 

提示：

0 <= num.length <= 10
num 仅含数字
'''
from typing import List
'''
思路1，暴力回溯
一个长度为n的数字字符串，可供插入运算符的位置有n-1个，运算符有3种，再加上没有运算符，故所有可能的表达式有4^(n-1)个。
根据提示，n最大是10，所有可能的表达式约2.6*10^5个，可以尝试暴力计算一下。

时间复杂度：O(4^(n-1)*20)，共生成4^(n-1)个表达式，每个表达式计算时间按长度计算约20
空间复杂度：O(n)
'''


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)
        if n == 0:
            return []
        if n == 1:
            if int(num) == target:
                return [num]
            else:
                return []

        # 判断表达式计算结果是否为target
        def isTarget(ops):
            nstk, opstk = [], []
            i, m = 0, len(ops)
            while i < m:
                if ops[i] == '+' or ops[i] == '-':
                    opstk.append(ops[i])
                elif ops[i] == '*':
                    i += 1
                    nstk.append(nstk.pop() * int(ops[i]))
                else:
                    nstk.append(int(ops[i]))
                i += 1
            while opstk:
                if opstk.pop() == '-':
                    nstk.append(-nstk.pop() + nstk.pop())
                else:
                    nstk.append(nstk.pop() + nstk.pop())
            return nstk[0] == target

        # 回溯所有可能的表达式
        def backtrack(index, ops):
            for op in ('+', '-', '*'):
                ops.append(op)
                if num[index] == '0':  # 第index个字符为0，不能与后面的字符组合成整数
                    ops.append('0')
                    if index == n - 1:
                        if isTarget(ops):
                            ans.append(''.join(ops))
                    else:
                        backtrack(index + 1, ops)
                    ops.pop()
                else:
                    for i in range(index, n):  # 当前操作数的长度从index一直到末尾
                        if i == n - 1:
                            ops.append(num[index:])
                            if isTarget(ops):
                                ans.append(''.join(ops))
                            ops.pop()
                        else:
                            ops.append(num[index:i + 1])
                            backtrack(i + 1, ops)
                            ops.pop()
                ops.pop()

        ans = []
        if num[0] == '0':  # 第1个数字是0，只能将第1个操作数设置为0
            backtrack(1, ['0'])
        else:
            if int(num) == target:
                ans.append(num)
            for i in range(1, n):  # 将数字切分成任意数字，作为第1个操作数
                backtrack(i, [num[:i]])
        return ans


s = Solution()
print(s.addOperators(num="00", target=0))
print(s.addOperators(num="123", target=6))
print(s.addOperators(num="232", target=8))
print(s.addOperators(num="105", target=5))
print(s.addOperators(num="3456237490", target=9191))
