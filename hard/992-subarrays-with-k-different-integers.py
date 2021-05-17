'''
K 个不同整数的子数组
给定一个正整数数组 A，如果 A 的某个子数组中不同整数的个数恰好为 K，则称 A 的这个连续、不一定不同的子数组为好子数组。

（例如，[1,2,3,1,2] 中有 3 个不同的整数：1，2，以及 3。）

返回 A 中好子数组的数目。

 

示例 1：

输入：A = [1,2,1,2,3], K = 2
输出：7
解释：恰好由 2 个不同整数组成的子数组：[1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
示例 2：

输入：A = [1,2,1,3,4], K = 3
输出：3
解释：恰好由 3 个不同整数组成的子数组：[1,2,1,3], [2,1,3], [1,3,4].
 

提示：

1 <= A.length <= 20000
1 <= A[i] <= A.length
1 <= K <= A.length
'''
from typing import List
'''
思路：双指针+哈希计数
设left,right指针为外层最大的满足k个不同整数的数组
1. 扩大right指针，直至将要超过k个不同整数，此时left、right区间内有k个不同整数，且最大化
2. 设innerLeft，innerRight指针，在left，right内滑动，使其满足最小的要求(有k个不同整数)。
innerLeft每向右移动一次，innerRight也定位到满足k个整数，然后innerRight..right返回都是合法的子数组。
累加right-innerRight+1
3. 第2步所有的inner指针移动完成后，将right指针右移，left指针右移，直至达到新的最大k数组
4. 重复上面1..3，直至数组被遍历完

复杂度：
> 时间复杂度：O(n)，4个指针每个遍历一次数组
> 空间复杂度：O(1)
'''


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        n = len(nums)
        counter = {}
        left, right = 0, 0
        ans = 0
        while right < n:
            innerCnt = None
            innerL, innerR = left, left  # 这2个指针在left和right内部滑动
            while right < n:  # 移动right指针，直至满足条件的子数组达到最大长度
                if len(counter) < k:  # 还不够k个数，可以添加新的整数或已有的整数增加计数
                    if nums[right] not in counter:
                        counter[nums[right]] = 1
                    else:
                        counter[nums[right]] += 1
                elif nums[right] in counter:  # 已经够了k个数，只能对已有的整数增加计数
                    counter[nums[right]] += 1
                else:  # 已经够了k个数，不能增加新的整数
                    break
                if len(counter) == k and not innerCnt:  # 优化inner指针定位，直接使用外层双指针定位
                    innerCnt = counter.copy()
                    innerR = right + 1
                right += 1
            if len(counter) < k:  # 不够k个数，退出
                break
            while innerR <= right:
                if innerL != left:  # inner指针第1次定位已经在上面做好，跳过第1次
                    if innerR == right:  # 剪枝，如果内部right和外部right指针相同，内部窗口无法再找到k个整数
                        break
                    while innerR < right and len(innerCnt) < k:  # 移动innerR指针，直至满足k个整数
                        if nums[innerR] not in innerCnt:
                            innerCnt[nums[innerR]] = 1
                        else:
                            innerCnt[nums[innerR]] += 1
                        innerR += 1
                if len(innerCnt) == k:
                    ans += right - innerR + 1
                while len(innerCnt) == k:  # 移动innerL，缩小窗口
                    innerCnt[nums[innerL]] -= 1
                    if innerCnt[nums[innerL]] == 0:
                        del innerCnt[nums[innerL]]
                    else:  # 如果内部窗口仍然满足k个整数，就需要累计一次子数组数量
                        ans += right - innerR + 1
                    innerL += 1
            while len(counter) == k:  # 移动left，直至不满足k个整数
                counter[nums[left]] -= 1
                if counter[nums[left]] == 0:
                    del counter[nums[left]]
                left += 1
        return ans


s = Solution()
print(s.subarraysWithKDistinct([1, 2, 1, 2, 3], 2))
print(s.subarraysWithKDistinct([1, 2, 1, 3, 4], 3))
print(s.subarraysWithKDistinct([2, 2, 1, 2, 2, 2, 1, 1], 2))
