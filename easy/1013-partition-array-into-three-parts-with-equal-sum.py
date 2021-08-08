'''
将数组分成和相等的三个部分
给你一个整数数组 arr，只有可以将其划分为三个和相等的 非空 部分时才返回 true，否则返回 false。

形式上，如果可以找出索引 i + 1 < j 且满足 (arr[0] + arr[1] + ... + arr[i] == arr[i + 1] + arr[i + 2] + ... + arr[j - 1]
== arr[j] + arr[j + 1] + ... + arr[arr.length - 1]) 就可以将数组三等分。

 

示例 1：

输入：arr = [0,2,1,-6,6,-7,9,1,2,0,1]
输出：true
解释：0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
示例 2：

输入：arr = [0,2,1,-6,6,7,9,-1,2,0,1]
输出：false
示例 3：

输入：arr = [3,3,6,5,-2,2,5,1,-9,4]
输出：true
解释：3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
 

提示：

3 <= arr.length <= 5 * 10^4
-10^4 <= arr[i] <= 10^4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/partition-array-into-three-parts-with-equal-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
'''
思路：贪心
先求整个数组和total，求其1/3，target=total/3
遍历数组，类似于滑动窗口，使每个窗口内的和为target，正好是3个子窗口

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        target, r = divmod(sum(arr), 3)
        if r > 0:  # 不能被3整除，肯定不能平均分开
            return False
        i, n = 0, len(arr)
        # 找第1个子数组
        sums = 0
        while i < n:
            sums += arr[i]
            i += 1
            if sums == target:
                break
        if sums != target or i == n:
            return False
        # 找第2个子数组
        sums = 0
        while i < n:
            sums += arr[i]
            i += 1
            if sums == target:
                break
        if sums != target or i == n:
            return False
        # 找第3个子数组
        sums = 0
        while i < n:
            sums += arr[i]
            i += 1
        if sums != target or i != n:
            return False
        return True
