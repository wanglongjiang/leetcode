'''
数组中的最长山脉

我们把数组 A 中符合下列属性的任意连续子数组 B 称为 “山脉”：

B.length >= 3
存在 0 < i < B.length - 1 使得 B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
（注意：B 可以是 A 的任意子数组，包括整个数组 A。）

给出一个整数数组 A，返回最长 “山脉” 的长度。

如果不含有 “山脉” 则返回 0。

 

示例 1：

输入：[2,1,4,7,3,2,5]
输出：5
解释：最长的 “山脉” 是 [1,4,7,3,2]，长度为 5。
示例 2：

输入：[2,2,2]
输出：0
解释：不含 “山脉”。
 

提示：

0 <= A.length <= 10000
0 <= A[i] <= 10000
'''
from typing import List
'''
思路：双指针
设3个指针left,mid,right，left指向左边山脚，mid指向山顶，right指向右边山脚，算法如下：
> 1. 从左往右遍历数组，找到的第1个arr[i]<arr[i+1]，设置为left
> 2. 然后mid指针从left+1开始，找到的第1个arr[i]>arr[i+1]，设置为mid。如果中途出现arr[i]==arr[i+1]中断执行，left设置为i，从上面的1开始执行
> 3. right从mid+1开始，找到的第1个arr[i]<=arr[i+1]，设置为right。此时right-left即为山脉长度
> 4. 重复上面1..3，直至数组遍历完成。

复杂度：
> 时间复杂度：O(n)
> 空间复杂度：O(1)
'''


class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        ans = 0
        n = len(arr)
        left, mid, right = 0, 0, 0
        while left < n and mid < n and right < n:
            while left < n - 1 and arr[left] >= arr[left + 1]:  # 移动left指针，直至遇到第1个上坡
                left += 1
            mid = left + 1
            while mid < n - 1 and arr[mid] < arr[mid + 1]:  # 移动mid指针，直至上坡全部完成
                mid += 1
            if mid >= n - 1 or arr[mid] == arr[mid + 1]:  # 如果出现平地，从left开始肯定不是山脉，需要重新界定left
                left = mid + 1
                continue
            right = mid + 1
            while right < n and arr[right - 1] > arr[right]:  # 移动right指针，直至下坡全部完成
                right += 1
            ans = max(ans, right - left)
            left = right - 1
        return ans


s = Solution()
print(
    s.longestMountain(
        [0, 0, 0, 1, 0, 2, 1, 2, 2, 1, 0, 0, 1, 0, 2, 0, 0, 0, 2, 1, 0, 1, 2, 1, 0, 1, 0, 2, 1, 0, 2, 0, 2, 1, 1, 2, 0, 1, 0, 1, 1, 1, 1, 2, 1, 2, 2, 2, 0]))
print(s.longestMountain([875, 884, 239, 731, 723, 685]) == 4)
print(s.longestMountain([2, 1, 4, 7, 3, 2, 5]) == 5)
print(s.longestMountain([2, 2, 2]) == 0)
