'''
等价多米诺骨牌对的数量
给你一个由一些多米诺骨牌组成的列表 dominoes。

如果其中某一张多米诺骨牌可以通过旋转 0 度或 180 度得到另一张多米诺骨牌，我们就认为这两张牌是等价的。

形式上，dominoes[i] = [a, b] 和 dominoes[j] = [c, d] 等价的前提是 a==c 且 b==d，或是 a==d 且 b==c。

在 0 <= i < j < dominoes.length 的前提下，找出满足 dominoes[i] 和 dominoes[j] 等价的骨牌对 (i, j) 的数量。

示例：

输入：dominoes = [[1,2],[2,1],[3,4],[5,6]]
输出：1
 

提示：

1 <= dominoes.length <= 40000
1 <= dominoes[i][j] <= 9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-equivalent-domino-pairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
'''
思路：哈希 计数
因为1 <= dominoes[i][j] <= 9，可以将dominoes[i][0]*10+dominoes[i][1] 放入哈希表
遍历dominoes中的每一对数，如果dominoes[i][0]*10+dominoes[i][1]或者dominoes[i][1]*10+dominoes[i][0]在哈希表中，
在哈希表中的所有数对可以与当前数对形成等价

时间复杂度：O(n)
空间复杂度：O(1)，最多有99个数字
'''


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        hashmap = {}
        ans = 0
        for d in dominoes:
            if (val := d[0] * 10 + d[1]) in hashmap:
                ans += hashmap[val]
                hashmap[val] += 1
            elif (val := d[1] * 10 + d[0]) in hashmap:
                ans += hashmap[val]
                hashmap[val] += 1
            else:
                hashmap[val] = 1
        return ans
