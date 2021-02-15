'''
公平的糖果棒交换

爱丽丝和鲍勃有不同大小的糖果棒：A[i] 是爱丽丝拥有的第 i 根糖果棒的大小，B[j] 是鲍勃拥有的第 j 根糖果棒的大小。

因为他们是朋友，所以他们想交换一根糖果棒，这样交换后，他们都有相同的糖果总量。（一个人拥有的糖果总量是他们拥有的糖果棒大小的总和。）

返回一个整数数组 ans，其中 ans[0] 是爱丽丝必须交换的糖果棒的大小，ans[1] 是 Bob 必须交换的糖果棒的大小。

如果有多个答案，你可以返回其中任何一个。保证答案存在。
'''
from typing import List
'''
思路：求2个数组的总和，然后求和之差，从两个数组中找两个数，使2个数的差*2为数组和之差
查找2个数的方法，从第1个数组里面找1个数，然后二分查找第2个数组找a-diff
'''


class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        def binarySearch(li, n):
            start = 0
            end = len(li) - 1
            while start <= end:
                mid = (start + end) // 2
                if li[mid] == n:
                    return mid
                elif li[mid] < n:
                    start = mid + 1
                else:
                    end = mid - 1
            return -1

        diff = (sum(A) - sum(B)) // 2
        A.sort()
        B.sort()
        for aIndex in range(len(A)):
            # 跳过A数组中重复的元素
            if aIndex > 0 and A[aIndex] == A[aIndex - 1]:
                continue
            target = A[aIndex] - diff
            bIndex = binarySearch(B, target)
            if bIndex >= 0:
                return [A[aIndex], target]
        return []


s = Solution()
print(s.fairCandySwap([35, 17, 4, 24, 10], [63, 21]))
print(s.fairCandySwap([1, 1], [2, 2]))
print(s.fairCandySwap([1, 2], [2, 3]))
print(s.fairCandySwap([2], [1, 3]))
print(s.fairCandySwap([1, 2, 5], [2, 4]))
