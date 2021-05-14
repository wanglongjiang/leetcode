'''
最长湍流子数组
当 A 的子数组 A[i], A[i+1], ..., A[j] 满足下列条件时，我们称其为湍流子数组：

若 i <= k < j，当 k 为奇数时， A[k] > A[k+1]，且当 k 为偶数时，A[k] < A[k+1]；
或 若 i <= k < j，当 k 为偶数时，A[k] > A[k+1] ，且当 k 为奇数时， A[k] < A[k+1]。
也就是说，如果比较符号在子数组中的每个相邻元素对之间翻转，则该子数组是湍流子数组。

返回 A 的最大湍流子数组的长度。

 

示例 1：

输入：[9,4,2,10,7,8,8,1,9]
输出：5
解释：(A[1] > A[2] < A[3] > A[4] < A[5])

示例 2：
输入：[4,8,12,16]
输出：2

示例 3：
输入：[100]
输出：1
 

提示：

1 <= A.length <= 40000
0 <= A[i] <= 10^9
'''
from typing import List
'''
思路：滑动窗口
left,right2个指针包括的滑动窗口初始为0，然后向右移动right指针，扩大窗口范围，直至窗口内子数组不满足湍流性质
然后向右移动left指针至right-1。

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        left, right, n = 0, 1, len(arr)
        ans = 1

        # 判断子数组是否满足湍流性质，因为窗口是逐步扩大的，所以每次只需要对比开头、结尾的2组元素
        def isTurbulence(left, right):
            if right - left == 1:
                return arr[right] != arr[left]
            sublen = right - left + 1
            if sublen % 2:  # 子数组长度为奇数，left与left+1, right-1与right的大于小于性质相反
                if arr[left] > arr[left + 1] and arr[right - 1] < arr[right]:
                    return True
                if arr[left] < arr[left + 1] and arr[right - 1] > arr[right]:
                    return True
            else:  # 子数组长度为偶数，left与left+1, right-1与right的大于小于性质相同
                if arr[left] > arr[left + 1] and arr[right - 1] > arr[right]:
                    return True
                if arr[left] < arr[left + 1] and arr[right - 1] < arr[right]:
                    return True
            return False

        while right < n:
            while right < n and isTurbulence(left, right):  # 扩大窗口范围，直至不满足湍流性质
                right += 1
            if right - left == 1:
                right += 1
                left += 1
            ans = max(ans, right - left)
            left = right - 1
        return ans


s = Solution()
print(s.maxTurbulenceSize([9, 9]))
print(s.maxTurbulenceSize([9, 4, 2, 10, 7, 8, 8, 1, 9]))
print(s.maxTurbulenceSize([4, 8, 12, 16]))
print(s.maxTurbulenceSize([100]))
