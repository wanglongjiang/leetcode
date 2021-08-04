'''
有效括号的嵌套深度
有效括号字符串 定义：对于每个左括号，都能找到与之对应的右括号，反之亦然。详情参见题末「有效括号字符串」部分。

嵌套深度 depth 定义：即有效括号字符串嵌套的层数，depth(A) 表示有效括号字符串 A 的嵌套深度。详情参见题末「嵌套深度」部分。

有效括号字符串类型与对应的嵌套深度计算方法如下图所示：



 

给你一个「有效括号字符串」 seq，请你将其分成两个不相交的有效括号字符串，A 和 B，并使这两个字符串的深度最小。

不相交：每个 seq[i] 只能分给 A 和 B 二者中的一个，不能既属于 A 也属于 B 。
A 或 B 中的元素在原字符串中可以不连续。
A.length + B.length = seq.length
深度最小：max(depth(A), depth(B)) 的可能取值最小。 
划分方案用一个长度为 seq.length 的答案数组 answer 表示，编码规则如下：

answer[i] = 0，seq[i] 分给 A 。
answer[i] = 1，seq[i] 分给 B 。
如果存在多个满足要求的答案，只需返回其中任意 一个 即可。

 

示例 1：

输入：seq = "(()())"
输出：[0,1,1,1,1,0]
示例 2：

输入：seq = "()(())()"
输出：[0,0,0,1,1,0,1,1]
解释：本示例答案不唯一。
按此输出 A = "()()", B = "()()", max(depth(A), depth(B)) = 1，它们的深度最小。
像 [1,1,1,0,0,1,1,1]，也是正确结果，其中 A = "()()()", B = "()", max(depth(A), depth(B)) = 1 。
 

提示：

1 < seq.size <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
'''
思路：计数
需要2次遍历seq，
1. 第1次遍历的目的是计算出最大深度maxDepth：
> 设遍历depth为括号深度，初始为0
> 如果当前字符seq[i]=='('，depth+1
> 如果当前字符seq[i]==')',depth-1
执行上述过程，过程中记录最大深度maxDepth。

2. 第2次遍历目的是将括号进行分配，深度不超过maxDepth/2的分配给A，深度超过maxDepth/2的括号分配给B：
> 设遍历depth为括号深度，初始为0
> 如果当前字符seq[i]=='('，depth+1，当depth>maxDepth/2，分配给B，否则分配给A
> 如果当前字符seq[i]==')',，当depth>maxDepth/2，分配给B，否则分配给A，然后修改depth=depth-1
执行上述过程，过程中记录最大深度maxDepth。

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        maxDepth, depth = 0, 0
        for c in seq:
            if c == '(':
                depth += 1
                maxDepth = max(maxDepth, depth)
            else:
                depth -= 1
        ans = [0] * len(seq)
        half = maxDepth // 2 + maxDepth % 2
        for i, c in enumerate(seq):
            if c == '(':
                depth += 1
                if depth > half:
                    ans[i] = 1
            else:
                if depth > half:
                    ans[i] = 1
                depth -= 1
        return ans


s = Solution()
print(s.maxDepthAfterSplit("(()())"))
print(s.maxDepthAfterSplit("()(())()"))
print(s.maxDepthAfterSplit(''))
