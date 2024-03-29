'''
面试题 17.14. 最小K个数
设计一个算法，找出数组中最小的k个数。以任意顺序返回这k个数均可。

示例：

输入： arr = [1,3,5,7,2,4,6,8], k = 4
输出： [1,2,3,4]
提示：

0 <= len(arr) <= 100000
0 <= k <= min(100000, len(arr))
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
print(
    s.smallestK([
        -14850, 4457, 7, -2845, -91, -62041, 185, 3, -40380, 9, 8089, 11, -319, -370, 394, 0, 3, -563, 3, 13, 89, 1471, 3832, 27, -2, -15551, 60, -28331, -655,
        -9685, 190, 7454, 23649, -13386, -38, -1669, 41114, -2, -35533, 12908, -48, 630, 27480, 44135, 21, 3698, 5632, 22, -38186, -37, 6, -2, -41119, -53284,
        -5064, -513, -4749, 16963, -51288, 0, 42383, 2804, 6753, 793, -962, 83, -6105, -72, -8, -4, 9, 740, 47, -68, -8419, -9, 15463, 0, -4, -78, -57022, -7,
        -38, 0, -22987, 32, 6, 50, 9821, 6, -789, -15, -7528, -553, 11567, 7870, 3627, -522, -455, -7169, 55, 120, -826, -43, 1257, 2810, -24, 2, -7, 0, -8,
        -55, -5, -7374, -3, -32904, -8140, 29, -460, -9, 21607, 8, -4819, 44564, 48, -92, -9014, 8, 5, -37, -9358, -6537, 183, -81, 21, 0, -298, -9877, -670,
        -6, -19, 97, -1923, 889, -38777, -10657, -1838, -6, 9, -8, -279, -2, -55950, -82, -696, -6, 51, 7440, 52096, -48555, -501, 4, -497, 4, -1, 69, 15, 1, 9,
        -4, 54, 6, -78, -55, 61863, 642, 0, 7, 0, -29988, 7278, 49, 42865, -992, 6, -216, 877, 735, 24612, -71, -62, 8208, -154, 30886, 39, -6685, 7, 8925,
        -62397, 3, 7636, 7, -37, -957, -864, 59468, -3, 9781, 117, 43, -6, 870, 0, -686, -6620, -5519, -14917, -88, -891, 1, 89, -38789, 7528, 6, -23608, 9089,
        -3703, -93, 61030, 400, -942, -3185, -633, 45, -614, -5899, -47, -252, -8240, 59, 9, -152, 6, -51035, -11, -89, 38478, 15483, -119, -2, 64389, 5739, 0,
        9870, -5716, -3, 8977, 43512, -915, -40, -6, 42, -133, -2, -8122, 4, -3876, 23683, 6, -42982, -6, 4, 55666, -2, 47143, 61, -8, 62296, -6, 30, -9,
        -45678, -296, -5053, 26893, -470, 52002, 78, -3, 51, 93, -24361, 363, 484, -2, -5937, 6833, -386, -3501, 59, 4, -4410, -141, 963, -42466, -7940, -57199,
        -65, 198, -53, -38141, 6, 4294, -98, 3832, 89, -430, -58, 22073, 23004, -25, 10856, 392, 4, 18, -37396, 19, -87, -60, 87, 4977, 2, 88, 27008, 34390,
        -640, -94, 4616, 48602, -8022, -66, 785, 0, 40367, -7114, 68, -41276, 23635, -24442, 1, 9389, 604, 4342, -864, -23812, -7, 4997, 74, 3669, -42503, -662,
        -9, 4891, 51093, -92, -2, 67, -42, 8, -6, 315, 36827, 4238, -35, 588, 46, 10670, 30669, 52630, 9859, 3298, -50, -4121, -2407, -110, -84, 954, -7, 816,
        852, 440, 0, -86, 830, -916, 3, -62, -927, 6, -808, -39, 27300, -2, 54, 65418, 52211, 61, -55531, 26, 55115, -14, 460, 99, -7, 6069, -7980, -6731,
        -4041, 4, 7, -1, 3, 7364, -65348, 37, -5, 1, -52, -6, 33, 979, -2298, 4582, -4, -7035, 9464, -62, -58316, 809, 6395, -48, -34, 50372, -84, -1, 17316,
        39634, 8060, -73, -29120, -9, 97, 8975, -57397, 44122, 3, 5, -77, 37196, 10, 44910, 80, -2, -56, -22, 6826, -14072, -5, -791, -912, 5827, 55038, 6, 25,
        70, 53, -392, 9346, 7168, -1, 39449, -934, -92, 8586, 73, -374, 6767, 57350, -98, -4522, -2, 7120, 8, 9, -45621, -408, -12, -6653, 976, -308, -41051,
        -37224, -988, -1, 5706, 30985, -30, 62, 7522, 19, -69, -47, -108, -25, -856, 2002, -2, 2817, -762, -136, -1515, 672, -867, -46, 63531, 2, -6293, -3743,
        4, 51803, -9835, -9, 1, -2464, 55, -8734, 11, -8713, 9438, -8414, 0, 54, -7, -9, -3, -30, -3, 48231, -8557, -6965, 96, -2, 93, 27, 3261, -9297, -7948,
        -5589, 95, -1576, 61289, 4564, 8246, 825, -46, 256
    ], 402))
print(s.smallestK(arr=[1, 3, 5, 7, 2, 4, 6, 8], k=4))
