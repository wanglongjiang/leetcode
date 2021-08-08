'''
得到子序列的最少操作次数
给你一个数组 target ，包含若干 互不相同 的整数，以及另一个整数数组 arr ，arr 可能 包含重复元素。

每一次操作中，你可以在 arr 的任意位置插入任一整数。比方说，如果 arr = [1,4,1,2] ，那么你可以在中间添加 3 得到 [1,4,3,1,2] 。
你可以在数组最开始或最后面添加整数。

请你返回 最少 操作次数，使得 target 成为 arr 的一个子序列。

一个数组的 子序列 指的是删除原数组的某些元素（可能一个元素都不删除），同时不改变其余元素的相对顺序得到的数组。
比方说，[2,7,4] 是 [4,2,3,7,2,1,4] 的子序列（加粗元素），但 [2,4,2] 不是子序列。

 

示例 1：

输入：target = [5,1,3], arr = [9,4,2,3,4]
输出：2
解释：你可以添加 5 和 1 ，使得 arr 变为 [5,9,4,1,2,3,4] ，target 为 arr 的子序列。
示例 2：

输入：target = [6,4,8,1,3,2], arr = [4,7,6,2,3,8,6,1]
输出：3
 

提示：

1 <= target.length, arr.length <= 10^5
1 <= target[i], arr[i] <= 109
target 不包含任何重复元素。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-operations-to-make-a-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
import bisect
'''
思路：求最长递增子序列 贪心 二分查找
问题可以简化为求2个数组的最长公共子序列，然后将arr中的元素替换为在target中的索引，又可以转化为求arr的最长递增子序列

求最长递增子序列如下，也可以看第300题 [最长递增子序列](medium/300-longest-increasing-subsequence.py)
设一个dp数组，其为有序数组，用于保存最长子序列。
遍历indexs每个元素，将其尝试加入dp数组：
> 如果indexs[i]大于dp数组中所有元素，说明最长子序列可以变长，需要扩大dp大小。
> 如果indexs[i]不大于dp中所有元素，需要定位其在有序数组dp中应该所处的位置，替换原先的元素。
这么做的目的是在保持最长子序列长度不变的情况下，减小以往保存的元素大小，以便新的元素加入时，能够出现上面的情况：大于dp中所有元素，可以扩展最长子序列

时间复杂度：O(nlogn)
空间复杂度：O(n)
'''


class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        # 得到targe每个值得索引
        indexMap = {}
        for i, v in enumerate(target):
            indexMap[v] = i
        # 将Arr转化为索引数组
        indexs = []
        for num in arr:
            if num in indexMap:
                indexs.append(indexMap[num])
        # 求最长递增子序列
        dp = []
        for idx in indexs:
            i = bisect.bisect_left(dp, idx)
            if i == len(dp):
                dp.append(idx)
            else:
                dp[i] = idx
        return len(target) - len(dp)  # 结果为target的长度减去公共子序列的长度
