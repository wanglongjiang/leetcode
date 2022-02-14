'''
有序数组中的单一元素
给定一个只包含整数的有序数组，每个元素都会出现两次，唯有一个数只会出现一次，找出这个数。

 

示例 1:

输入: nums = [1,1,2,3,3,4,4,8,8]
输出: 2
示例 2:

输入: nums =  [3,3,7,7,10,11,11]
输出: 10
 

提示:

1 <= nums.length <= 10^5
0 <= nums[i] <= 10^5
 

进阶: 采用的方案可以在 O(log n) 时间复杂度和 O(1) 空间复杂度中运行吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/single-element-in-a-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
'''
思路：二分查找
取数组中部坐标mid=(start+end)/2
> 如果子数组长度==1，则目标即为唯一的元素
> 如果nums[mid]==nums[mid+1]，
>> 如果mid-start为偶数，说明目标在mid+1后面，需要查找mid+2..end
>> 如果mid-start为奇数，说明目标在mid前面，需要查找start..mid
> 如果nums[mid]==nums[mid-1]，
>> 如果mid-start为偶数，说明目标在mid-1前面
>> 如果mid-start为奇数，说明目标在mid后面
> 如果nums[mid]与两侧值都不同，则目标就是nums[mid]

重复上面过程

时间复杂度：O(logn)
空间复杂度：O(1)
'''


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        start, end = 0, len(nums)
        while end - start > 1:
            mid = (start + end) // 2
            if nums[mid] == nums[mid + 1]:
                if (mid - start) % 2 == 0:
                    start = mid + 2
                else:
                    end = mid
            elif nums[mid] == nums[mid - 1]:
                if (mid - start) % 2 == 0:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                return nums[mid]
        return nums[start]
