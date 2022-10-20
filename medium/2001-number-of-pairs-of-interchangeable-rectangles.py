'''
2001. 可互换矩形的组数
用一个下标从 0 开始的二维整数数组 rectangles 来表示 n 个矩形，其中 rectangles[i] = [widthi, heighti] 表示第 i 个矩形的宽度和高度。

如果两个矩形 i 和 j（i < j）的宽高比相同，则认为这两个矩形 可互换 。更规范的说法是，两个矩形满足 widthi/heighti == widthj/heightj（使用实数除法而非整数除法），则认为这两个矩形 可互换 。

计算并返回 rectangles 中有多少对 可互换 矩形。

 

示例 1：

输入：rectangles = [[4,8],[3,6],[10,20],[15,30]]
输出：6
解释：下面按下标（从 0 开始）列出可互换矩形的配对情况：
- 矩形 0 和矩形 1 ：4/8 == 3/6
- 矩形 0 和矩形 2 ：4/8 == 10/20
- 矩形 0 和矩形 3 ：4/8 == 15/30
- 矩形 1 和矩形 2 ：3/6 == 10/20
- 矩形 1 和矩形 3 ：3/6 == 15/30
- 矩形 2 和矩形 3 ：10/20 == 15/30
示例 2：

输入：rectangles = [[4,5],[7,8]]
输出：0
解释：不存在成对的可互换矩形。
 

提示：

n == rectangles.length
1 <= n <= 105
rectangles[i].length == 2
1 <= widthi, heighti <= 105
'''
import math
from typing import Counter, List
'''
思路：哈希
用哈希表统计相同宽高比的矩形个数。
具有相同宽高比的矩形个数如果为n(n>=2)，转换成组合数学问题，也即n个元素中选择2个，
计数公式为n!/(2*(n-2)!)

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        whCounter = Counter(r[0] / r[1] for r in rectangles)  # 统计宽高比
        return sum(map(lambda n: math.factorial(n) // (2 * math.factorial(n - 2)), filter(lambda cnt: cnt > 1, whCounter.values())))  # 用排列组合公式计算组合数
