'''
迷你语法分析器
给定一个用字符串表示的整数的嵌套列表，实现一个解析它的语法分析器。

列表中的每个元素只可能是整数或整数嵌套列表

提示：你可以假定这些字符串都是格式良好的：

字符串非空
字符串不包含空格
字符串只包含数字0-9、[、-、,、]
 

示例 1：

给定 s = "324",

你应该返回一个 NestedInteger 对象，其中只包含整数值 324。
示例 2：

给定 s = "[123,[456,[789]]]",

返回一个 NestedInteger 对象包含一个有两个元素的嵌套列表：

1. 一个 integer 包含值 123
2. 一个包含两个元素的嵌套列表：
    i.  一个 integer 包含值 456
    ii. 一个包含一个元素的嵌套列表
         a. 一个 integer 包含值 789
'''


class NestedInteger:
    pass


'''
思路：栈
依次读入字符，如果是[，创建list integer，入栈
    如果是整数（有可能是负数），加入栈顶的list 内，如果栈为空，直接返回
    如果是]，出栈，将出栈的list，加入新栈顶的list内，如果栈为空，返回
时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        i, n = 0, len(s)
        stack = []
        while i < n:
            if s[i] == '[':
                stack.append(NestedInteger())
                i += 1
            elif s[i] == ']':
                li = stack.pop()
                if stack:
                    stack[-1].add(li)
                    i += 1
                else:
                    return li
            elif s[i] == ',':
                i += 1
            else:
                neg = False
                if s[i] == '-':
                    neg = True
                    i += 1
                num = ''
                while i < n and s[i].isdigit():
                    num += s[i]
                    i += 1
                num = int(num)
                if neg:
                    num = -num
                integer = NestedInteger(num)
                if stack:
                    stack[-1].add(integer)
                else:
                    return integer


s = Solution()
print(s.deserialize("324"))
print(s.deserialize("[123,[456,[789]]]"))
