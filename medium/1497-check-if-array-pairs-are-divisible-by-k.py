'''
1497. 检查数组对是否可以被 k 整除
给你一个整数数组 arr 和一个整数 k ，其中数组长度是偶数，值为 n 。

现在需要把数组恰好分成 n / 2 对，以使每对数字的和都能够被 k 整除。

如果存在这样的分法，请返回 True ；否则，返回 False 。

 

示例 1：

输入：arr = [1,2,3,4,5,10,6,7,8,9], k = 5
输出：true
解释：划分后的数字对为 (1,9),(2,8),(3,7),(4,6) 以及 (5,10) 。
示例 2：

输入：arr = [1,2,3,4,5,6], k = 7
输出：true
解释：划分后的数字对为 (1,6),(2,5) 以及 (3,4) 。
示例 3：

输入：arr = [1,2,3,4,5,6], k = 10
输出：false
解释：无法在将数组中的数字分为三对的同时满足每对数字和能够被 10 整除的条件。
 

提示：

arr.length == n
1 <= n <= 105
n 为偶数
-109 <= arr[i] <= 109
1 <= k <= 105
'''
from typing import Counter, List
'''
思路：哈希 数学
利用同余原理，将arr所有的元素arr[i]%k，加入哈希表计数
然后依次遍历哈希表中所有余数，当余数a的个数为m，k-a的个数也为m时，此时这2组数可以构成合法的数对，否则不可以

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainders = Counter(num % k for num in arr)
        for r, count in remainders.items():
            if r:
                if r != k - r and count != remainders[k - r]:
                    return False
                if r == k - r and count % 2:
                    return False
        return True
