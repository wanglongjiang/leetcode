'''
查找和最小的K对数字
给定两个以升序排列的整数数组 nums1 和 nums2 , 以及一个整数 k 。

定义一对值 (u,v)，其中第一个元素来自 nums1，第二个元素来自 nums2 。

请找到和最小的 k 个数对 (u1,v1),  (u2,v2)  ...  (uk,vk) 。

 

示例 1:

输入: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
输出: [1,2],[1,4],[1,6]
解释: 返回序列中的前 3 对数：
     [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
示例 2:

输入: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
输出: [1,1],[1,1]
解释: 返回序列中的前 2 对数：
     [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
示例 3:

输入: nums1 = [1,2], nums2 = [3], k = 3
输出: [1,3],[2,3]
解释: 也可能序列中所有的数对都被返回:[1,3],[2,3]
 

提示:

1 <= nums1.length, nums2.length <= 10^4
-10^9 <= nums1[i], nums2[i] <= 10^9
nums1, nums2 均为升序排列
1 <= k <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-k-pairs-with-smallest-sums
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
import heapq
'''
思路：堆
将2个数组任意2个元素的和加入堆，找出最小的k个

时间复杂度：O(n^2)
空间复杂度：O(1)
'''


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        for a in nums1:
            for b in nums2:
                if len(heap) < k:
                    heapq.heappush(heap, (-(a + b), a, b))
                elif -(a + b) > heap[0][0]:
                    heapq.heappushpop(heap, (-(a + b), a, b))
                else:  # 因为nums2是递增的，如果a+b大于最大值，可以停止遍历nums2后面的元素
                    break
        ans = []
        while heap:
            t = heapq.heappop(heap, )
            ans.append([t[1], t[2]])
        ans.reverse()
        return ans


s = Solution()
print(s.kSmallestPairs(nums1=[1, 1, 2], nums2=[1, 2, 3], k=2))
print(s.kSmallestPairs(nums1=[1, 7, 11], nums2=[2, 4, 6], k=3))
print(s.kSmallestPairs([-10, -4, 0, 0, 6], [3, 5, 6, 7, 8, 100], 10))
print(s.kSmallestPairs(nums1=[1, 2], nums2=[3], k=3))
