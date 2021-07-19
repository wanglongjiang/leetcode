'''
最多能完成排序的块 II
这个问题和“最多能完成排序的块”相似，但给定数组中的元素可以重复，输入数组最大长度为2000，其中的元素最大为10**8。

arr是一个可能包含重复元素的整数数组，我们将这个数组分割成几个“块”，并将这些块分别进行排序。之后再连接起来，使得连接的结果和按升序排序后的原数组相同。

我们最多能将数组分成多少块？

示例 1:

输入: arr = [5,4,3,2,1]
输出: 1
解释:
将数组分成2块或者更多块，都无法得到所需的结果。
例如，分成 [5, 4], [3, 2, 1] 的结果是 [4, 5, 1, 2, 3]，这不是有序的数组。
示例 2:

输入: arr = [2,1,3,4,4]
输出: 4
解释:
我们可以把它分成两块，例如 [2, 1], [3, 4, 4]。
然而，分成 [2, 1], [3], [4], [4] 可以得到最多的块数。
注意:

arr的长度在[1, 2000]之间。
arr[i]的大小在[0, 10**8]之间。
'''
from typing import List
'''
思路：单调栈
如果2块数组a、b能够连结成排序数组，那么a、b自身内部可以乱序，但是必须有max(a)<=min(b)
可以用一个单调栈stack辅助处理：
遍历arr中所有元素，对于当前元素arr[i]:
> 如果arr[i]大于栈顶元素，stack出栈，直至栈顶元素大于等于arr[i]或者栈为空。当栈为空的时候，说明之前遍历过的数组元素全部小于arr[i]，它们可以单独构成1个块。
> 如果arr[i]小于栈顶元素，入栈。

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        stack = []
        ans = 0
        for num in arr:
            while stack and stack[-1] <= num:
                stack.pop()
            if not stack:
                ans += 1
            stack.append(num)
        return ans


s = Solution()
print(s.maxChunksToSorted([5, 4, 3, 2, 1]) == 1)
print(s.maxChunksToSorted([2, 1, 3, 4, 4]) == 4)
print(s.maxChunksToSorted([1, 2, 4, 4]) == 4)
print(s.maxChunksToSorted([2, 1, 4, 4]) == 3)
