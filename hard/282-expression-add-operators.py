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
思路1，DFS

'''


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)
        ans = []

        def dfs(index, val, preVal, expr):
            if index == n and val == target:
                ans.append(expr)
            for i in range(index + 1, n + 1):
                v = int(num[index:i])
                if i - index > 1 and num[index:index + 1] == '0':
                    continue
                if index == 0:
                    dfs(i, val + v, v, expr + num[index:i])
                    continue
                dfs(i, val + v, v, expr + '+' + num[index:i])
                dfs(i, val - v, -v, expr + '-' + num[index:i])
                dfs(i, val - preVal + preVal * v, preVal * v, expr + '*' + num[index:i])

        dfs(0, 0, 0, '')
        return ans


s = Solution()
print(s.addOperators("123456789", 45))
print(s.addOperators(num="00", target=0))
print(s.addOperators(num="123", target=6))
print(s.addOperators(num="232", target=8))
print(s.addOperators(num="105", target=5))
print(s.addOperators(num="3456237490", target=9191))
