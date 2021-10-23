'''
2007. 从双倍数组中还原原数组
一个整数数组 original 可以转变成一个 双倍 数组 changed ，转变方式为将 original 中每个元素 值乘以 2 加入数组中，然后将所有元素 随机打乱 。

给你一个数组 changed ，如果 change 是 双倍 数组，那么请你返回 original数组，否则请返回空数组。original 的元素可以以 任意 顺序返回。



示例 1：

输入：changed = [1,3,4,2,6,8]
输出：[1,3,4]
解释：一个可能的 original 数组为 [1,3,4] :
- 将 1 乘以 2 ，得到 1 * 2 = 2 。
- 将 3 乘以 2 ，得到 3 * 2 = 6 。
- 将 4 乘以 2 ，得到 4 * 2 = 8 。
其他可能的原数组方案为 [4,3,1] 或者 [3,1,4] 。
示例 2：

输入：changed = [6,3,0,1]
输出：[]
解释：changed 不是一个双倍数组。
示例 3：

输入：changed = [1]
输出：[]
解释：changed 不是一个双倍数组。


提示：

1 <= changed.length <= 10^5
0 <= changed[i] <= 10^5
'''
from typing import List
from collections import defaultdict
'''
思路：排序 哈希
1. 将数组进行排序
2. 从大到小遍历数组，
> 如果当前数值*2在哈希表中存在，则找到一对数，将其2倍在哈希表中删除，当前数值不用加入数组
> 如果当前数组*2在哈希表中不存在，将当前数值加入哈希表
3. 最后，哈希表中应该为空

时间复杂度：O(nlog)，排序需要O(nlogn)
空间复杂度：O(n)
'''


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2:
            return []
        counter = defaultdict(int)
        ans = []
        changed.sort(reverse=True)
        for num in changed:
            if num << 1 in counter:
                ans.append(num)
                counter[num << 1] -= 1
                if counter[num << 1] == 0:
                    del counter[num << 1]
            else:
                counter[num] += 1
        return ans if len(counter) == 0 else []


s = Solution()
print(s.findOriginalArray([1, 3, 4, 2, 6, 8]))
print(s.findOriginalArray([6, 3, 0, 1]))
print(s.findOriginalArray([1]))
print(s.findOriginalArray([6, 3, 2, 1]))
