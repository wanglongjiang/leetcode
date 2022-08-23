'''
822. 翻转卡片游戏
在桌子上有 N 张卡片，每张卡片的正面和背面都写着一个正数（正面与背面上的数有可能不一样）。

我们可以先翻转任意张卡片，然后选择其中一张卡片。

如果选中的那张卡片背面的数字 X 与任意一张卡片的正面的数字都不同，那么这个数字是我们想要的数字。

哪个数是这些想要的数字中最小的数（找到这些数中的最小值）呢？如果没有一个数字符合要求的，输出 0。

其中, fronts[i] 和 backs[i] 分别代表第 i 张卡片的正面和背面的数字。

如果我们通过翻转卡片来交换正面与背面上的数，那么当初在正面的数就变成背面的数，背面的数就变成正面的数。

示例：

输入：fronts = [1,2,4,4,7], backs = [1,3,4,1,3]
输出：2
解释：假设我们翻转第二张卡片，那么在正面的数变成了 [1,3,4,4,7] ， 背面的数变成了 [1,2,4,1,3]。
接着我们选择第二张卡片，因为现在该卡片的背面的数是 2，2 与任意卡片上正面的数都不同，所以 2 就是我们想要的数字。


提示：

1 <= fronts.length == backs.length <= 1000
1 <= fronts[i] <= 2000
1 <= backs[i] <= 2000
'''
from typing import List
from functools import reduce
'''
思路：看题意有点迷糊，用哈希尝试一把
用哈希统计2个数组相同的所有数值，然后找到剩余的数值里最小的一个。

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        ans = float('inf')
        hashset = set(map(lambda x: x[0], filter(lambda x: x[0] == x[1], zip(fronts, backs))))  # 找到正面、背面相同的数字
        ans = reduce(min, filter(lambda x: x not in hashset, fronts), ans)  # 找到正面最小的
        ans = reduce(min, filter(lambda x: x not in hashset, backs), ans)  # 找到背面最小的
        return ans if ans != float('inf') else 0


s = Solution()
print(s.flipgame(fronts=[1, 2, 4, 4, 7], backs=[1, 3, 4, 1, 3]))