'''
816. 模糊坐标
我们有一些二维坐标，如 "(1, 3)" 或 "(2, 0.5)"，然后我们移除所有逗号，小数点和空格，得到一个字符串S。返回所有可能的原始字符串到一个列表中。

原始的坐标表示法不会存在多余的零，所以不会出现类似于"00", "0.0", "0.00", "1.0", "001", "00.01"或一些其他更小的数来表示坐标。
此外，一个小数点前至少存在一个数，所以也不会出现“.1”形式的数字。

最后返回的列表可以是任意顺序的。而且注意返回的两个数字中间（逗号之后）都有一个空格。



示例 1:
输入: "(123)"
输出: ["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"]
示例 2:
输入: "(00011)"
输出:  ["(0.001, 1)", "(0, 0.011)"]
解释:
0.0, 00, 0001 或 00.01 是不被允许的。
示例 3:
输入: "(0123)"
输出: ["(0, 123)", "(0, 12.3)", "(0, 1.23)", "(0.1, 23)", "(0.1, 2.3)", "(0.12, 3)"]
示例 4:
输入: "(100)"
输出: [(10, 0)]
解释:
1.0 是不被允许的。


提示:

4 <= S.length <= 12.
S[0] = "(", S[S.length - 1] = ")", 且字符串 S 中的其他元素都是数字。
'''
from typing import List
from itertools import product
'''
思路：数学 组合
将数字拆分成2个数字，然后尝试在数字里面添加小数点

时间复杂度：O(n*(n/2)!)
空间复杂度：O(1)
'''


class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        s = s[1:-1]  # 去掉括弧
        ans = []
        for i in range(1, len(s)):  # 分割数字
            first = s[:i]
            if len(first) > 1 and first[0] == '0' and first[-1] == '0':  # 0开头的数字，不能以0结尾
                continue
            second = s[i:]
            if len(second) > 1 and second[0] == '0' and second[-1] == '0':  # 0开头的数字，不能以0结尾
                continue
            comps = product("(", self.numComp(first), [', '], self.numComp(second), ")")  # 组合生成的数字
            ans.extend(map(lambda t: ''.join(t), comps))
        return ans

    def numComp(self, s):  # 生成数值组合
        if len(s) == 1:
            return [s]
        if s[0] == '0':  # 0开头的，肯定只有1种选择
            return ['0.' + s[1:]]
        ans = [s]
        for i in range(1, len(s)):  # 尝试添加小数点
            if int(s[i:]) == 0:  # 小数点后面是0的，不是合法数字
                break
            ans.append(s[:i] + '.' + s[i:])
        return ans


s = Solution()
print(s.ambiguousCoordinates('(123)'))
print(s.ambiguousCoordinates('(00011)'))
print(s.ambiguousCoordinates('(0123)'))
print(s.ambiguousCoordinates('(100)'))
