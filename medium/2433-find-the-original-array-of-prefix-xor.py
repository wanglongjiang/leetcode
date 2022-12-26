'''
2433. 找出前缀异或的原始数组
给你一个长度为 n 的 整数 数组 pref 。找出并返回满足下述条件且长度为 n 的数组 arr ：

pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i].
注意 ^ 表示 按位异或（bitwise-xor）运算。

可以证明答案是 唯一 的。

 

示例 1：

输入：pref = [5,2,0,3,1]
输出：[5,7,2,3,2]
解释：从数组 [5,7,2,3,2] 可以得到如下结果：
- pref[0] = 5
- pref[1] = 5 ^ 7 = 2
- pref[2] = 5 ^ 7 ^ 2 = 0
- pref[3] = 5 ^ 7 ^ 2 ^ 3 = 3
- pref[4] = 5 ^ 7 ^ 2 ^ 3 ^ 2 = 1
示例 2：

输入：pref = [13]
输出：[13]
解释：pref[0] = arr[0] = 13
 

提示：

1 <= pref.length <= 105
0 <= pref[i] <= 106
'''
from typing import List
'''
思路：位运算
根据异或的性质：a^b^a=b
pref[i]=pref[i-1]^arr[i]
那么arr[i]=pref[i]^pref[i-1]

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        arr = [0] * len(pref)
        arr[0] = pref[0]
        for i in range(1, len(pref)):
            arr[i] = pref[i] ^ pref[i - 1]
        return arr
