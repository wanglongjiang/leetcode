'''
按奇偶排序数组 II
给定一个非负整数数组 A， A 中一半整数是奇数，一半整数是偶数。

对数组进行排序，以便当 A[i] 为奇数时，i 也是奇数；当 A[i] 为偶数时， i 也是偶数。

你可以返回任何满足上述条件的数组作为答案。

 

示例：

输入：[4,2,5,7]
输出：[4,5,2,7]
解释：[4,7,2,5]，[2,5,4,7]，[2,7,4,5] 也会被接受。
 

提示：

2 <= A.length <= 20000
A.length % 2 == 0
0 <= A[i] <= 1000
 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-array-by-parity-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
'''
思路：双指针
设even,odd2个指针，
even指向偶数下标，单次移动需要移动2个下标，初始指向0
odd指向奇数下标，单次移动需要移动2个下标，初始指向1
1. 向右移动even指针，直至遇到奇数
2. 向右移动odd指针，直至遇到偶数
3. 交换2个指针指向的元素
4. 重复1~3，直至2个指针移动到末尾

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even, odd, n = 0, 1, len(nums)
        while even < n and odd < n:
            while even < n and nums[even] % 2 == 0:
                even += 2
            while odd < n and nums[odd] % 2 == 1:
                odd += 2
            if even < n and odd < n:
                nums[even], nums[odd] = nums[odd], nums[even]
                even += 2
                odd += 2
        return nums
