'''
最多能完成排序的块
数组arr是[0, 1, ..., arr.length - 1]的一种排列，我们将这个数组分割成几个“块”，并将这些块分别进行排序。之后再连接起来，使得连接的结果和按升序排序后的原数组相同。

我们最多能将数组分成多少块？

示例 1:

输入: arr = [4,3,2,1,0]
输出: 1
解释:
将数组分成2块或者更多块，都无法得到所需的结果。
例如，分成 [4, 3], [2, 1, 0] 的结果是 [3, 4, 0, 1, 2]，这不是有序的数组。
示例 2:

输入: arr = [1,0,2,3,4]
输出: 4
解释:
我们可以把它分成两块，例如 [1, 0], [2, 3, 4]。
然而，分成 [1, 0], [2], [3], [4] 可以得到最多的块数。
注意:

arr 的长度在 [1, 10] 之间。
arr[i]是 [0, 1, ..., arr.length - 1]的一种排列。
'''
from typing import List
'''
思路：单调栈
如果2块数组a、b能够连结成排序数组，那么a、b自身内部可以乱序，但是必须有max(a)<min(b)
可以用一个单调栈stack辅助处理：
遍历arr中所有元素，对于当前元素arr[i]:
> 如果arr[i]大于栈顶元素，stack出栈，直至栈顶元素大于arr[i]或者栈为空。当栈为空的时候，说明之前遍历过的数组元素全部小于arr[i]，它们可以单独构成1个块。
> 如果arr[i]小于栈顶元素，入栈。

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        stack = []
        ans = 0
        for num in arr:
            while stack and stack[-1] < num:
                stack.pop()
            if not stack:
                ans += 1
            stack.append(num)
        return ans
