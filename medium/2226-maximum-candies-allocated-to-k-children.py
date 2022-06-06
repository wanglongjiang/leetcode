'''
2226. 每个小孩最多能分到多少糖果
给你一个 下标从 0 开始 的整数数组 candies 。数组中的每个元素表示大小为 candies[i] 的一堆糖果。你可以将每堆糖果分成任意数量的 子堆 ，
但 无法 再将两堆合并到一起。

另给你一个整数 k 。你需要将这些糖果分配给 k 个小孩，使每个小孩分到 相同 数量的糖果。每个小孩可以拿走 至多一堆 糖果，有些糖果可能会不被分配。

返回每个小孩可以拿走的 最大糖果数目 。

 

示例 1：

输入：candies = [5,8,6], k = 3
输出：5
解释：可以将 candies[1] 分成大小分别为 5 和 3 的两堆，然后把 candies[2] 分成大小分别为 5 和 1 的两堆。现在就有五堆大小分别为 5、5、3、5 和 1 的糖果。
可以把 3 堆大小为 5 的糖果分给 3 个小孩。可以证明无法让每个小孩得到超过 5 颗糖果。
示例 2：

输入：candies = [2,5], k = 11
输出：0
解释：总共有 11 个小孩，但只有 7 颗糖果，但如果要分配糖果的话，必须保证每个小孩至少能得到 1 颗糖果。因此，最后每个小孩都没有得到糖果，答案是 0 。
 

提示：

1 <= candies.length <= 105
1 <= candies[i] <= 107
1 <= k <= 1012
'''
from typing import List
'''
思路：二分查找
设每个小孩能分走的最大糖果数为x，那么candies[i]能够分给candies[i]//x个小孩，遍历整个candies数组可以得到所有糖果可以分给多少个小孩，设这个数字为y。
如果y>=k，糖果能满足需要，可以将x增大
如果y<k，糖果不能满足需要，需要将x减少

将上述过程用二分查找来实现，x的取值范围是1,max(candies)

时间复杂度：O(nlogm)，其中n=candies.length，m=max(candies)
空间复杂度：O(1)
'''


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:  # 排除掉0个的
            return 0
        low, high, ans = 1, max(candies), 1
        while low <= high:
            mid = (low + high) // 2
            if sum(map(lambda num: num // mid, candies)) >= k:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans


s = Solution()
print(s.maximumCandies([1], 1))
