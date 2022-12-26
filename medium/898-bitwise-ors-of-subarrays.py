'''
898. 子数组按位或操作
我们有一个非负整数数组 arr 。

对于每个（连续的）子数组 sub = [arr[i], arr[i + 1], ..., arr[j]] （ i <= j），
我们对 sub 中的每个元素进行按位或操作，获得结果 arr[i] | arr[i + 1] | ... | arr[j] 。

返回可能结果的数量。 多次出现的结果在最终答案中仅计算一次。

 

示例 1：

输入：arr = [0]
输出：1
解释：
只有一个可能的结果 0 。
示例 2：

输入：arr = [1,1,2]
输出：3
解释：
可能的子数组为 [1]，[1]，[2]，[1, 1]，[1, 2]，[1, 1, 2]。
产生的结果为 1，1，2，1，3，3 。
有三个唯一值，所以答案是 3 。
示例 3：

输入：arr = [1,2,4]
输出：6
解释：
可能的结果是 1，2，3，4，6，以及 7 。
 

提示：

1 <= nums.length <= 5 * 104
0 <= nums[i] <= 109​​​​​​​
'''
from typing import List
'''
思路：位运算 集合
遍历arr，对于每个元素arr[i]将其与前面的所有元素进行或

时间复杂度：O(nlogx)，x为arr中最大值
空间复杂度：O(nlogx)
'''


class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        ans, cur = {arr[0]}, {arr[0]}
        for i in range(1, len(arr)):
            cur = {arr[i] | x for x in cur} | {arr[i]}
            ans |= cur
        return len(ans)


s = Solution()
assert s.subarrayBitwiseORs([1, 2, 4]) == 6
assert s.subarrayBitwiseORs([1, 1, 2]) == 3
assert s.subarrayBitwiseORs([0]) == 1
