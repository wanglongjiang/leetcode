'''
找出和为指定值的下标对
给你两个整数数组 nums1 和 nums2 ，请你实现一个支持下述两类查询的数据结构：

累加 ，将一个正整数加到 nums2 中指定下标对应元素上。
计数 ，统计满足 nums1[i] + nums2[j] 等于指定值的下标对 (i, j) 数目（0 <= i < nums1.length 且 0 <= j < nums2.length）。
实现 FindSumPairs 类：

FindSumPairs(int[] nums1, int[] nums2) 使用整数数组 nums1 和 nums2 初始化 FindSumPairs 对象。
void add(int index, int val) 将 val 加到 nums2[index] 上，即，执行 nums2[index] += val 。
int count(int tot) 返回满足 nums1[i] + nums2[j] == tot 的下标对 (i, j) 数目。
 

示例：

输入：
["FindSumPairs", "count", "add", "count", "count", "add", "add", "count"]
[[[1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4]], [7], [3, 2], [8], [4], [0, 1], [1, 1], [7]]
输出：
[null, 8, null, 2, 1, null, null, 11]

解释：
FindSumPairs findSumPairs = new FindSumPairs([1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4])
findSumPairs.count(7)  # 返回 8  下标对 (2,2), (3,2), (4,2), (2,4), (3,4), (4,4) 满足 2 + 5 = 7 ，
下标对 (5,1), (5,5) 满足 3 + 4 = 7
findSumPairs.add(3, 2) # 此时 nums2 = [1,4,5,4,5,4]
findSumPairs.count(8)  # 返回 2 ；下标对 (5,2), (5,4) 满足 3 + 5 = 8
findSumPairs.count(4)  # 返回 1 ；下标对 (5,0) 满足 3 + 1 = 4
findSumPairs.add(0, 1) # 此时 nums2 = [2,4,5,4,5,4]
findSumPairs.add(1, 1) # 此时 nums2 = [2,5,5,4,5,4]
findSumPairs.count(7)  # 返回 11 ；下标对 (2,1), (2,2), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,4)
满足 2 + 5 = 7 ，下标对 (5,3), (5,5) 满足 3 + 4 = 7
 

提示：

1 <= nums1.length <= 1000
1 <= nums2.length <= 10^5
1 <= nums1[i] <= 10^9
1 <= nums2[i] <= 10^5
0 <= index < nums2.length
1 <= val <= 10^5
1 <= tot <= 10^9
最多调用 add 和 count 函数各 1000 次
'''
import bisect
from sortedcontainers import SortedDict
from typing import List
'''
思路：OrderedMap + 哈希
1. 初始化函数中：
> 将nums1按照值的大小排序
> 对nums2所有的value，index加入treemap，index存入集合中
2. add函数中：
> 将treemap中原nums2[index]删除，然后将nums2[index]+val加入treemap
3. count函数中：
> 查询treemap中最小值minVal，遍历nums1中<=tot-minVal的所有元素，在treemap中查找等于tot-nums1[i]的元素，如果能找到，将其下标对数量加上下标集合数量

时间复杂度：初始化O(nlogn+mlogm)，add:O(logn),count:O(logn)
'''


class FindSumPairs:
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums1.sort()
        self.nums2 = nums2
        self.sorted2 = SortedDict()
        for i in range(len(nums2)):
            if nums2[i] in self.sorted2:
                self.sorted2[nums2[i]].add(i)
            else:
                st = set()
                st.add(i)
                self.sorted2[nums2[i]] = st

    def add(self, index: int, val: int) -> None:
        oldVal = self.nums2[index]
        newVal = oldVal + val
        self.nums2[index] = newVal
        self.sorted2[oldVal].remove(index)
        if len(self.sorted2[oldVal]) == 0:
            del self.sorted2[oldVal]
        if newVal in self.sorted2:
            self.sorted2[newVal].add(index)
        else:
            st = set()
            st.add(index)
            self.sorted2[newVal] = st

    def count(self, tot: int) -> int:
        ans = 0
        minVal2 = self.sorted2.peekitem(0)[0]  # 取得nums2中最小值
        end = bisect.bisect_right(self.nums1, tot - minVal2)  # 取得nums1中<=tot-minVal的边界
        for i in range(end):  # 遍历nums1中<=tot-minVal的所有元素，
            if (tot - self.nums1[i]) in self.sorted2:
                ans += len(self.sorted2[tot - self.nums1[i]])
        return ans


findSumPairs = FindSumPairs([1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4])
print(findSumPairs.count(7))  # 返回 8  下标对 (2,2), (3,2), (4,2), (2,4), (3,4), (4,4) 满足 2 + 5 = 7 ，下标对 (5,1), (5,5) 满足 3 + 4 = 7
findSumPairs.add(3, 2)  # 此时 nums2 = [1,4,5,4,5,4]
print(findSumPairs.count(8))  # 返回 2 ；下标对 (5,2), (5,4) 满足 3 + 5 = 8
print(findSumPairs.count(4))  # 返回 1 ；下标对 (5,0) 满足 3 + 1 = 4
findSumPairs.add(0, 1)  # 此时 nums2 = [2,4,5,4,5,4]
findSumPairs.add(1, 1)  # 此时 nums2 = [2,5,5,4,5,4]
print(findSumPairs.count(7))  # 返回 11 ；下标对 (2,1), (2,2), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,4) 满足 2 + 5 = 7 ，下标对 (5,3), (5,5) 满足 3 + 4 = 7

findSumPairs = FindSumPairs([9, 70, 14, 9, 76], [26, 26, 58, 23, 74, 68, 68, 78, 58, 26])
print(findSumPairs.add(6, 10))
print(findSumPairs.add(5, 6))
print(findSumPairs.count(32))
print(findSumPairs.add(3, 55))
print(findSumPairs.add(9, 32))
print(findSumPairs.add(9, 16))
print(findSumPairs.add(1, 48))
print(findSumPairs.add(1, 4))
print(findSumPairs.add(0, 52))
print(findSumPairs.add(8, 20))
print(findSumPairs.add(9, 4))
print(findSumPairs.count(88))
