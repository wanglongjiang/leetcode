'''
数组的相对排序
给你两个数组，arr1 和 arr2，

arr2 中的元素各不相同
arr2 中的每个元素都出现在 arr1 中
对 arr1 中的元素进行排序，使 arr1 中项的相对顺序和 arr2 中的相对顺序相同。未在 arr2 中出现过的元素需要按照升序放在 arr1 的末尾。

 

示例：

输入：arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
输出：[2,2,2,1,4,3,3,9,6,7,19]
 

提示：

1 <= arr1.length, arr2.length <= 1000
0 <= arr1[i], arr2[i] <= 1000
arr2 中的元素 arr2[i] 各不相同
arr2 中的每个元素 arr2[i] 都出现在 arr1 中

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/relative-sort-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
from collections import Counter
'''
思路：计数排序
1. 首先对arr1中的所有元素进行计数，保存到counter中
2. 然后遍历arr2，对于arr2[i]
> 查看在counter中的计数，假设有a个，那么需要在ans中输出n个arr2[i]，然后删除counter中的arr2[i]
3. counter中剩余的元素添加到ans后面

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counter = Counter(arr1)
        ans = []
        for num in arr2:
            for i in range(counter[num]):
                ans.append(num)
            del counter[num]
        for num, count in counter.items():
            for i in range(count):
                ans.append(num)
        return ans
