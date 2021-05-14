'''
解码异或后的数组

未知 整数数组 arr 由 n 个非负整数组成。

经编码后变为长度为 n - 1 的另一个整数数组 encoded ，其中 encoded[i] = arr[i] XOR arr[i + 1] 。
例如，arr = [1,0,2,1] 经编码后得到 encoded = [1,2,3] 。

给你编码后的数组 encoded 和原数组 arr 的第一个元素 first（arr[0]）。

请解码返回原数组 arr 。可以证明答案存在并且是唯一的。

示例 1：

输入：encoded = [1,2,3], first = 1
输出：[1,0,2,1]
解释：若 arr = [1,0,2,1] ，那么 first = 1 且 encoded = [1 XOR 0, 0 XOR 2, 2 XOR 1] = [1,2,3]
示例 2：

输入：encoded = [6,2,7,3], first = 4
输出：[4,2,0,7,4]
 

提示：

2 <= n <= 104
encoded.length == n - 1
0 <= encoded[i] <= 105
0 <= first <= 105
'''
from typing import List
'''
思路：位运算
可以使用a^a^b=b的特性，将nums[1..n-1]的原值进行恢复
时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ans = [first]
        for num in encoded:
            ans.append(ans[-1] ^ num)
        return ans


s = Solution()
print(s.decode(encoded=[1, 2, 3], first=1))
print(s.decode(encoded=[6, 2, 7, 3], first=4))