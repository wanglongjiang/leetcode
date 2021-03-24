'''
大样本统计
我们对 0 到 255 之间的整数进行采样，并将结果存储在数组 count 中：count[k] 就是整数 k 的采样个数。

我们以 浮点数 数组的形式，分别返回样本的最小值、最大值、平均值、中位数和众数。其中，众数是保证唯一的。

我们先来回顾一下中位数的知识：

如果样本中的元素有序，并且元素数量为奇数时，中位数为最中间的那个元素；
如果样本中的元素有序，并且元素数量为偶数时，中位数为中间的两个元素的平均值。
'''
from typing import List
'''
思路：
1、最小值，值不为0的最小坐标
2、最大值，值不为0的最大坐标
3、平均值，所有不为0的sum(下标*值)/元素数，元素数=sum(值)
4、中位数，元素数量为奇数时，中位数为最中间的那个元素；元素数量为偶数时，中位数为中间的两个元素的平均值。
5、众数，具有最大值的下标
'''


class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        minVal = -1  # 最小值
        maxVal = -1  # 最大值
        itemCount = 0  # 元素数
        totalVal = 0  # 所有元素合计
        modeNum, modeCount = -1, 0  # 众数，众数个数
        # 第1次遍历，求出最大值、最小值、元素数、所有元素合计、众数
        for num in range(len(count)):
            if count[num] > 0:
                if minVal < 0:  # 记录最小值
                    minVal = num
                maxVal = num  # 记录最大值
                itemCount += count[num]  # 累计元素数
                totalVal += count[num] * num  # 累计元素合计
                if modeCount < count[num]:  # 记录众数
                    modeCount = count[num]
                    modeNum = num
        avg = totalVal / itemCount
        midVal = 0
        # 第2次遍历，求中位数
        if itemCount & 1:
            # 元素数为奇数，最中间坐标的元素为中位数
            midIndex = itemCount // 2
            itemCount = 0
            for num in range(len(count)):
                if count[num] > 0:
                    itemCount += count[num]
                    if itemCount > midIndex:
                        midVal = num
                        break
        else:
            # 元素数为偶数，最中间2个元素的平均值为中位数
            leftIndex, rightIndex = itemCount // 2 - 1, itemCount // 2
            left, right = -1, -1
            itemCount = 0
            for num in range(len(count)):
                if count[num] > 0:
                    itemCount += count[num]
                    if itemCount > leftIndex and left < 0:
                        left = num
                    if itemCount > rightIndex and right < 0:
                        right = num
                        break
            midVal = (left + right) / 2
        return [float(minVal), float(maxVal), float(avg), float(midVal), float(modeNum)]


s = Solution()
print(
    s.sampleStats([
        0, 1, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0
    ]))
print(
    s.sampleStats([
        0, 4, 3, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0
    ]))
