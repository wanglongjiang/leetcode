'''
二倍数对数组
给定一个长度为偶数的整数数组 arr，只有对 arr 进行重组后可以满足 “对于每个 0 <= i < len(arr) / 2，
都有 arr[2 * i + 1] = 2 * arr[2 * i]” 时，返回 true；否则，返回 false。

 

示例 1：

输入：arr = [3,1,3,6]
输出：false
示例 2：

输入：arr = [2,1,2,6]
输出：false
示例 3：

输入：arr = [4,-2,2,-4]
输出：true
解释：可以用 [-2,-4] 和 [2,4] 这两组组成 [-2,-4,2,4] 或是 [2,4,-2,-4]
示例 4：

输入：arr = [1,2,4,16,8,4]
输出：false
 

提示：

0 <= arr.length <= 3 * 10^4
arr.length 是偶数
-10^5 <= arr[i] <= 10^5

'''
from typing import List
from collections import Counter
'''
思路：排序+哈希
题目时间上是求数组中所有元素能否分成n/2组，每组里面2个元素，1个元素是另外一个元素的2倍
可以将数组进行排序，并加入哈希表中，从小到大遍历所有元素。
对于负数，是求其1/2是否在哈希表中，如果不在，返回false，如果在，将其加入已遍历hash表中，下次如果遇到在已遍历哈希表的整数，需要跳过；
对于0，需要有偶数个0；
对于非负数，是求其2倍整数是否在哈希表中，如果不在，返回false,如果在，将其加入已遍历hash表中，下次如果遇到在已遍历哈希表的整数，需要跳过；

时间复杂度：O(nlogn)
空间复杂度：O(n)
'''


class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        hashmap, needSkip = Counter(arr), Counter()
        arr.sort()
        i, n = 0, len(arr)
        while i < n:
            if needSkip[arr[i]] > 0:  # 该整数在前面的数进行配对时已经使用，需要跳过
                val = arr[i]
                j = i + needSkip[val]
                needSkip[val] = 0
                if j > n:
                    return False
                while i < j:
                    if arr[i] != val:
                        return False
                    i += 1
            elif arr[i] < 0:
                p = arr[i] / 2  # 对于小于0的数，需要查找其1/2
                if p not in hashmap:
                    return False
                needSkip[int(p)] += 1
                i += 1
            elif arr[i] == 0:
                j = i
                while i < n and arr[i] == 0:  # 跳过所有的0
                    i += 1
                if (i - j) % 2:  # 0的个数不是偶数个，无法凑成一对
                    return False
            else:
                p = arr[i] * 2  # 对于大于0的数，需要在哈希表中查找其2倍
                if p not in hashmap:
                    return False
                needSkip[p] += 1
                i += 1
        return True


s = Solution()
print(s.canReorderDoubled([-4, -6, -1, -2, -1, -1, -3, -8]))
print(s.canReorderDoubled([0, 0]))
