'''
最长和谐子序列
和谐数组是指一个数组里元素的最大值和最小值之间的差别 正好是 1 。

现在，给你一个整数数组 nums ，请你在所有可能的子序列中找到最长的和谐子序列的长度。

数组的子序列是一个由数组派生出来的序列，它可以通过删除一些元素或不删除元素、且不改变其余元素的顺序而得到。

 

示例 1：

输入：nums = [1,3,2,2,5,2,3,7]
输出：5
解释：最长的和谐子序列是 [3,2,2,2,3]
示例 2：

输入：nums = [1,2,3,4]
输出：2
示例 3：

输入：nums = [1,1,1,1]
输出：0
 

提示：

1 <= nums.length <= 2 * 10^4
-10^9 <= nums[i] <= 10^9
'''
from typing import List
from collections import defaultdict
'''
思路：哈希计数 排序
用哈希表对nums中数字进行计数
然后对哈希表中的key,val进行排序，如果2个key相差正好是1，计算最大长度

时间复杂度：O(nlogn)
空间复杂度：O(n)
'''


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        ans = 0
        prev = float('-inf')
        for num, count in sorted(counter.items()):
            if num - prev == 1:
                ans = max(ans, count + counter[prev])
            prev = num
        return ans


s = Solution()
print(s.findLHS([1, 3, 2, 2, 5, 2, 3, 7]))
print(s.findLHS([1, 2, 3, 4]))
print(s.findLHS([1, 1, 1, 1]))
