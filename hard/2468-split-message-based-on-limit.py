'''
2468. 根据限制分割消息
困难
3
相关企业
给你一个字符串 message 和一个正整数 limit 。

你需要根据 limit 将 message 分割 成一个或多个 部分 。每个部分的结尾都是 "<a/b>" ，其中 "b" 用分割出来的总数 替换， "a" 用当前部分所在的编号 替换 ，编号从 1 到 b 依次编号。
除此以外，除了最后一部分长度 小于等于 limit 以外，其他每一部分（包括结尾部分）的长度都应该 等于 limit 。

你需要确保分割后的结果数组，删掉每部分的结尾并 按顺序 连起来后，能够得到 message 。同时，结果数组越短越好。

请你返回 message  分割后得到的结果数组。如果无法按要求分割 message ，返回一个空数组。

 

示例 1：

输入：message = "this is really a very awesome message", limit = 9
输出：["thi<1/14>","s i<2/14>","s r<3/14>","eal<4/14>","ly <5/14>","a v<6/14>","ery<7/14>"," aw<8/14>","eso<9/14>","me<10/14>"," m<11/14>","es<12/14>","sa<13/14>",
"ge<14/14>"]
解释：
前面 9 个部分分别从 message 中得到 3 个字符。
接下来的 5 个部分分别从 message 中得到 2 个字符。
这个例子中，包含最后一个部分在内，每个部分的长度都为 9 。
可以证明没有办法分割成少于 14 个部分。
示例 2：

输入：message = "short message", limit = 15
输出：["short mess<1/2>","age<2/2>"]
解释：
在给定限制下，字符串可以分成两个部分：
- 第一个部分包含 10 个字符，长度为 15 。
- 第二个部分包含 3 个字符，长度为 8 。
 

提示：

1 <= message.length <= 104
message 只包含小写英文字母和 ' ' 。
1 <= limit <= 104
'''
from typing import List
'''
[TOC]

# 思路
枚举

# 解题方法
message最大能分成多少份呢，因为份数越多，结尾部分越长，有可能结尾部分>=limit，此时已不能切割。
最大份数的候选有可能为9、99、999、9999，
9的结尾部分长度为5，99的结尾部分长度为6-7，999的结尾部分长度为7-9，9999的结尾部分长度为8-11。

枚举从1到9999，计算这种切分是否能够容纳所有字符，如果能容纳，输出结果

# 复杂度
- 时间复杂度: 
> $O(n)$

- 空间复杂度: 
> $O(1)$
'''


class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        n = len(message)
        minPart = 0
        aNums = {1: 9, 2: 90, 3: 900, 4: 9000}  # 结尾中<a/b>中a部分位数与数量的关系，比如a为1位数，一共9个，如果a为2位数，一共有90个
        for part in range(1, n + 1):
            tmp = part
            capacity, bSize = 0, len(str(part))
            for aSize in range(1, bSize + 1):  # 遍历a的位数
                tailSize = 3 + aSize + bSize  # 计算结尾大小
                if tailSize >= limit:
                    break
                capacity += (limit - tailSize) * min(aNums[aSize], tmp)
                tmp -= aNums[aSize]
            if capacity >= n:
                minPart = part
                break
        else:
            return []
        # 输出结果
        ans = []
        i, a, b, bSize = 0, 1, str(minPart), len(str(minPart))
        while i < n:
            size = limit - 3 - bSize - len(str(a))
            ans.append(message[i:i + size] + "<" + str(a) + "/" + b + ">")
            i += size
            a += 1
        return ans


s = Solution()
print(s.splitMessage('p', 7))
assert s.splitMessage(message="short message", limit=15) == ["short mess<1/2>", "age<2/2>"]
print(s.splitMessage("zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz", 10))
assert s.splitMessage(message="this is really a very awesome message", limit=9) == [
    "thi<1/14>", "s i<2/14>", "s r<3/14>", "eal<4/14>", "ly <5/14>", "a v<6/14>", "ery<7/14>", " aw<8/14>", "eso<9/14>", "me<10/14>", " m<11/14>", "es<12/14>",
    "sa<13/14>", "ge<14/14>"
]
