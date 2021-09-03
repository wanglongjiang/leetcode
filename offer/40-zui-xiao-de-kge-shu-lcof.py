'''
剑指 Offer 40. 最小的k个数

输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

 

示例 1：

输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]
示例 2：

输入：arr = [0,1,2,1], k = 1
输出：[0]
 

限制：

0 <= k <= arr.length <= 10000
0 <= arr[i] <= 10000
'''
from typing import List
import heapq
'''
思路：快速选择+堆
1. 使用快排里面的分区，随机选择一个pivot，将数组分成>=pivot和<pivot2部分
2. 如果<pivot的分区大小lsize<k，则该部分可以加入结果，继续对>=pivot的部分继续分区，尝试提取最小的k-lsize；如果<pivot的部分>k，继续分区<pivot部分
重复上面1.2

嗯，算法是有漏洞的，如果一个全部都一样的数组，用快速选择无法分区，会陷入死循环。
再补加一个堆吧，如果3次分区出现无法分成2部分，将调用堆，添加剩余元素

时间复杂度：O(n)，最坏情况下O(nlogk)
空间复杂度：O(1)
'''


class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        import random
        start, end = 0, len(arr) - 1
        ans = []
        paritionErrorCount = 0
        while k > 0:
            pIndex = random.randint(start, end)
            arr[pIndex], arr[start] = arr[start], arr[pIndex]
            pivot = arr[start]  # 使用随机的pivot将数组分成2部分
            i, j = start, end
            while i < j:
                while i < j and arr[j] >= pivot:
                    j -= 1
                arr[i] = arr[j]
                while i < j and arr[i] < pivot:
                    i += 1
                arr[j] = arr[i]
            arr[i] = pivot
            lowSize = i - start
            if lowSize == 0:
                paritionErrorCount += 1
                if paritionErrorCount > 3:  # 超过3次无法分区，调用堆
                    ans.extend(heapq.nsmallest(k, arr[start:end + 1]))
                    return ans
            elif lowSize == k:
                ans.extend(arr[start:i])
                return ans
            elif lowSize < k:  # 不够k个数，将lowSize个数加入结果，然后继续对高区进行分区
                ans.extend(arr[start:i])
                k -= lowSize
                start = i
                paritionErrorCount = 0
            else:  # 超过k个数，将
                end = i - 1
                paritionErrorCount = 0
        return ans


s = Solution()
print(s.getLeastNumbers(arr=[3, 2, 1], k=2))
print(s.getLeastNumbers(arr=[0, 1, 2, 1], k=1))
