'''
验证栈序列
给定 pushed 和 popped 两个序列，每个序列中的 值都不重复，只有当它们可能是在最初空栈上进行的推入 push 和弹出 pop 操作序列的结果时，
返回 true；否则，返回 false 。
提示：

0 <= pushed.length == popped.length <= 1000
0 <= pushed[i], popped[i] < 1000
pushed 是 popped 的排列。
'''
from typing import List
'''
思路：栈
设置1个堆栈stack，执行push、pop过程；设置1个集合numset，保存当前已入栈过的所有元素。
对于pushed、popped，2个指针分别是i,j，初始都是0。
1、遍历pushed，每个元素都入栈，和加入numset，直至popped[j]出现在numset中，这种情况下说明发生了出栈，停止入栈。
2、遍历popped，开始执行出栈，直至遇到没有出现在numset中的元素，说明出栈执行完毕。
    在执行2出栈过程中，stack出栈的顺序必然与popped中的顺序一样，否则是非法出栈。
时间复杂度：O(n)，数组遍历一次，每个最多入栈1次
空间复杂度：O(n)，栈、集合最大需要O(n)空间
'''


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        n = len(pushed)
        stack = []
        numset = set()
        i, j = 0, 0
        while i < n or j < n:
            while i < n and popped[j] not in numset:  # 执行入栈，直至遇到popped[j]出现在已入栈的元素中，说明需要出栈
                stack.append(pushed[i])
                numset.add(pushed[i])
                i += 1
            while j < n and popped[j] in numset:  # 执行出栈，直至遇到没有入栈的元素
                if stack[-1] == popped[j]:  # 已出栈的元素顺序必然与stack出栈顺序相同
                    stack.pop()
                    j += 1
                else:  # 如果出栈顺序对不上，是非法
                    return False
        return True
