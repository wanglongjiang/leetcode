'''
2232. 向表达式添加括号后的最小结果
给你一个下标从 0 开始的字符串 expression ，格式为 "<num1>+<num2>" ，其中 <num1> 和 <num2> 表示正整数。

请你向 expression 中添加一对括号，使得在添加之后， expression 仍然是一个有效的数学表达式，
并且计算后可以得到 最小 可能值。左括号 必须 添加在 '+' 的左侧，而右括号必须添加在 '+' 的右侧。

返回添加一对括号后形成的表达式 expression ，且满足 expression 计算得到 最小 可能值。
如果存在多个答案都能产生相同结果，返回任意一个答案。

生成的输入满足：expression 的原始值和添加满足要求的任一对括号之后 expression 的值，都符合 32-bit 带符号整数范围。

 

示例 1：

输入：expression = "247+38"
输出："2(47+38)"
解释：表达式计算得到 2 * (47 + 38) = 2 * 85 = 170 。
注意 "2(4)7+38" 不是有效的结果，因为右括号必须添加在 '+' 的右侧。
可以证明 170 是最小可能值。
示例 2：

输入：expression = "12+34"
输出："1(2+3)4"
解释：表达式计算得到 1 * (2 + 3) * 4 = 1 * 5 * 4 = 20 。
示例 3：

输入：expression = "999+999"
输出："(999+999)"
解释：表达式计算得到 999 + 999 = 1998 。
 

提示：

3 <= expression.length <= 10
expression 仅由数字 '1' 到 '9' 和 '+' 组成
expression 由数字开始和结束
expression 恰好仅含有一个 '+'.
expression 的原始值和添加满足要求的任一对括号之后 expression 的值，都符合 32-bit 带符号整数范围
'''
'''
思路：暴力组合
字符串总长度最大是10，可以暴力迭代“+”两边所有数字的组合，找到结果最小的

时间复杂度：O((n/2)^2)
空间复杂度：O(n)
'''


class Solution:
    def minimizeResult(self, expression: str) -> str:
        left, right = expression.split('+')
        minVal, ans = float('inf'), ''
        for i in range(len(left)):
            for j in range(1, len(right) + 1):
                val = (int(left[i:]) + int(right[:j])) * (1 if i == 0 else int(left[:i])) * (1 if j == len(right) else int(right[j:]))
                if minVal > val:
                    minVal = val
                    ans = left[:i] + '(' + left[i:] + '+' + right[:j] + ')' + right[j:]
        return ans


s = Solution()
print(s.minimizeResult("12+34"))
print(s.minimizeResult("247+38"))
print(s.minimizeResult("999+999"))
