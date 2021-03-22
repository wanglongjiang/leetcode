'''
距离相等的条形码
在一个仓库里，有一排条形码，其中第 i 个条形码为 barcodes[i]。

请你重新排列这些条形码，使其中两个相邻的条形码 不能 相等。 你可以返回任何满足该要求的答案，此题保证存在答案。
提示：
1 <= barcodes.length <= 10000
1 <= barcodes[i] <= 10000
'''
from typing import List
'''
思路1，计数。
从提示中知道1 <= barcodes[i] <= 10000，可以用1个哈希表或大小为10000的数组对数字进行计数，
然后首先输出出现次数最多的数字c，然后再输出其他数字。
输出分成2步，第1步只输出到barcodes的偶数下标，第2次只输出到barcodes的奇数下标
时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        n = len(barcodes)
        counter = {}
        maxCount, maxNum = 0, 0
        # 统计各个数字的个数
        for v in barcodes:
            if v in counter:
                counter[v] += 1
                if counter[v] > maxCount:
                    maxCount = counter[v]
                    maxNum = v
            else:
                counter[v] = 1
        i = 0
        # 输出最多的数字（如果n为奇数，最多的数字可能出现n/2+1次，必须第1个输出）
        while i < n:
            barcodes[i] = maxNum
            maxCount -= 1
            i += 2
            if maxCount == 0:
                break
        counter.pop(maxNum)
        count = 0
        # 输出剩余的数字
        while len(counter) > 0:
            if i >= n:  # 偶数下标输出完，切换成奇数下标
                i = 1
            if count == 0:
                num, count = counter.popitem()
            while count > 0 and i < n:
                barcodes[i] = num
                count -= 1
                i += 2
        return barcodes


s = Solution()
print(s.rearrangeBarcodes([1, 1, 1, 2, 2, 2]))
print(s.rearrangeBarcodes([1, 1, 1, 1, 2, 2, 3, 3]))
