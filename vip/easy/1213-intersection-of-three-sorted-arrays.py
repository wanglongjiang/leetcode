'''
1213. 三个有序数组的交集
给出三个均为 严格递增排列 的整数数组 arr1，arr2 和 arr3。

返回一个由 仅 在这三个数组中 同时出现 的整数所构成的有序数组。



示例：

输入: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
输出: [1,5]
解释: 只有 1 和 5 同时在这三个数组中出现.


提示：

1 <= arr1.length, arr2.length, arr3.length <= 1000
1 <= arr1[i], arr2[i], arr3[i] <= 2000
'''
from typing import List
'''
思路：双指针
设3个指针，分别指向3个数组，初始指向0
对比3个指针指向的数值，如果全都一样，加入结果list
否则将最小元素的指针向后移动

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        ans = []
        m, n, o = len(arr1), len(arr2), len(arr3)
        i, j, k = 0, 0, 0
        while i < m and j < n and k < o:
            if arr1[i] == arr2[j] == arr3[k]:
                ans.append(arr1[i])
                i += 1
                j += 1
                k += 1
            else:
                minVal = min(arr1[i], arr2[j], arr3[k])
                if arr1[i] == minVal:
                    i += 1
                if arr2[j] == minVal:
                    j += 1
                if arr3[k] == minVal:
                    k += 1
        return ans


s = Solution()
print(s.arraysIntersection([1, 2, 3, 4, 5], arr2=[1, 2, 5, 7, 9], arr3=[1, 3, 4, 5, 8]))
