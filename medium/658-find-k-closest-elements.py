'''
658. 找到 K 个最接近的元素
给定一个排序好的数组 arr ，两个整数 k 和 x ，从数组中找到最靠近 x（两数之差最小）的 k 个数。返回的结果必须要是按升序排好的。

整数 a 比整数 b 更接近 x 需要满足：

|a - x| < |b - x| 或者
|a - x| == |b - x| 且 a < b


示例 1：

输入：arr = [1,2,3,4,5], k = 4, x = 3
输出：[1,2,3,4]
示例 2：

输入：arr = [1,2,3,4,5], k = 4, x = -1
输出：[1,2,3,4]


提示：

1 <= k <= arr.length
1 <= arr.length <= 10^4
数组里的每个元素与 x 的绝对值不超过 10^4
'''
from typing import List
import bisect
'''
思路：二分查找 双指针
首先在arr中查找x，设x在arr中的插入位置是i
然后设left,right指针初始都指向i，然后2个指针向外移动，移动过程中读入最接近x的k个数值，加入数组ans
最后排序ans

时间复杂度：O($log^n$+$k*logk$)
空间复杂度：O($klog^k$)
'''
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        size = len(arr)
        left = 0
        right = size - k

        while left < right:
            # mid = left + (right - left) // 2
            mid = (left + right) >> 1
            # 尝试从长度为 k + 1 的连续子区间删除一个元素
            # 从而定位左区间端点的边界值
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left:left + k]


s = Solution()
print(s.findClosestElements([0, 0, 1, 2, 3, 3, 4, 7, 7, 8], 3, 5) == [3, 3, 4])  # TODO
print(s.findClosestElements(arr=[1, 2, 3, 4, 5], k=4, x=3))
print(s.findClosestElements(arr=[1, 2, 3, 4, 5], k=4, x=-1))
