'''
1481. 不同整数的最少数目
给你一个整数数组 arr 和一个整数 k 。现需要从数组中恰好移除 k 个元素，请找出移除后数组中不同整数的最少数目。

 

示例 1：

输入：arr = [5,5,4], k = 1
输出：1
解释：移除 1 个 4 ，数组中只剩下 5 一种整数。
示例 2：

输入：arr = [4,3,1,1,3,3,2], k = 3
输出：2
解释：先移除 4、2 ，然后再移除两个 1 中的任意 1 个或者三个 3 中的任意 1 个，最后剩下 1 和 3 两种整数。
 

提示：

1 <= arr.length <= 10^5
1 <= arr[i] <= 10^9
0 <= k <= arr.length
'''
from typing import Counter, List
'''
思路：哈希 排序 贪心
用哈希表对所有元素进行计数，很明显，移除个数最少的元素收益最高。
对计数进行排序，从k中依次减掉，直至k<=0

时间复杂度：O(nlogn)
空间复杂度：O(n)
'''


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = Counter(arr)
        for i, cnt in enumerate(sorted(count.values())):
            k -= cnt
            if k == 0:
                return len(count) - (i + 1)
            elif k < 0:
                return len(count) - i
        return 0


s = Solution()
print(s.findLeastNumOfUniqueInts(arr=[5, 5, 4], k=1))
