'''
优势洗牌
给定两个大小相等的数组 A 和 B，A 相对于 B 的优势可以用满足 A[i] > B[i] 的索引 i 的数目来描述。

返回 A 的任意排列，使其相对于 B 的优势最大化。

 

示例 1：

输入：A = [2,7,11,15], B = [1,10,4,11]
输出：[2,11,7,15]
示例 2：

输入：A = [12,24,8,32], B = [13,25,32,11]
输出：[24,32,8,12]
 

提示：

1 <= A.length = B.length <= 10000
0 <= A[i] <= 10^9
0 <= B[i] <= 10^9
'''
from typing import List
'''
思路：排序+贪心算法
类似于田忌赛马，找到nums1中刚刚大于nums2中的元素输出。
具体算法：
1. 对nums1排序，对nums2的值，索引构成的对按值进行排序
2. 从大到小遍历nums2，
> 如果nums1的最大值大于nums2的最大值，将2者的最大值全部pop，结果输出
> 如果不大于，则跳过该元素
3. 最后将结果list中未设置的元素，依次用nums1中剩余的元素填充

时间复杂度：O(nlogn)
空间复杂度：O(n)
'''


class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        nums1.sort()
        nums2 = [(nums2[i], i) for i in range(n)]
        nums2.sort(key=lambda item: item[0])
        ans = [-1] * n
        while nums2:
            item = nums2.pop()
            if item[0] < nums1[-1]:
                ans[item[1]] = nums1.pop()
        if nums1:
            for i in range(n):
                if ans[i] < 0:
                    ans[i] = nums1.pop()
                    if not nums1:
                        break
        return ans


s = Solution()
print(s.advantageCount([2, 7, 11, 15], [1, 10, 4, 11]))
print(s.advantageCount([12, 24, 8, 32], [13, 25, 32, 11]))
