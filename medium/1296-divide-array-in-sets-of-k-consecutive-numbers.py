'''
划分数组为连续数字的集合

给你一个整数数组 nums 和一个正整数 k，请你判断是否可以把这个数组划分成一些由 k 个连续数字组成的集合。
如果可以，请返回 True；否则，返回 False。


注意：此题目与 846 重复：https://leetcode-cn.com/problems/hand-of-straights/


示例 1：

输入：nums = [1,2,3,3,4,4,5,6], k = 4
输出：true
解释：数组可以分成 [1,2,3,4] 和 [3,4,5,6]。
示例 2：

输入：nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
输出：true
解释：数组可以分成 [1,2,3] , [2,3,4] , [3,4,5] 和 [9,10,11]。
示例 3：

输入：nums = [3,3,2,2,1,1], k = 3
输出：true
示例 4：

输入：nums = [1,2,3,4], k = 3
输出：false
解释：数组不能分成几个大小为 3 的子数组。


提示：

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
1 <= k <= nums.length
'''
from typing import List
from sortedcontainers import SortedDict
'''
思路：Ordered Map
使用treemap(python中的treemap是sortedcontainers.sorteddict)对所有元素进行计数
然后从小到大，k一组从treempa中删除，如果能出尽则返回true

时间复杂度：O(nlogn),红黑树的时间复杂度为nlogn
空间复杂度：O(n)
'''


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k:
            return False
        treemap = SortedDict()
        for num in nums:
            if num in treemap:
                treemap[num] += 1
            else:
                treemap[num] = 1
        # groupSize一组，输出连续的数字
        while treemap:
            num, cnt = treemap.peekitem(0)
            for num in range(num, num + k):
                if num in treemap:
                    treemap[num] -= 1
                    if treemap[num] == 0:
                        del treemap[num]
                else:
                    return False
        return True


s = Solution()
print(s.isPossibleDivide(nums=[3, 2, 1, 2, 3, 4, 3, 4, 5, 9, 10, 11], k=3))
