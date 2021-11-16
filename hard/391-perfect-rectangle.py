'''
给你一个数组 rectangles ，其中 rectangles[i] = [xi, yi, ai, bi] 表示一个坐标轴平行的矩形。这个矩形的左下顶点是 (xi, yi) ，右上顶点是 (ai, bi) 。

如果所有矩形一起精确覆盖了某个矩形区域，则返回 true ；否则，返回 false 。

 
示例 1：


输入：rectangles = [[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]
输出：true
解释：5 个矩形一起可以精确地覆盖一个矩形区域。 
示例 2：


输入：rectangles = [[1,1,2,3],[1,3,2,4],[3,1,4,2],[3,2,4,4]]
输出：false
解释：两个矩形之间有间隔，无法覆盖成一个矩形。
示例 3：


输入：rectangles = [[1,1,3,3],[3,1,4,2],[1,3,2,4],[3,2,4,4]]
输出：false
解释：图形顶端留有空缺，无法覆盖成一个矩形。
示例 4：


输入：rectangles = [[1,1,3,3],[3,1,4,2],[1,3,2,4],[2,2,4,4]]
输出：false
解释：因为中间有相交区域，虽然形成了矩形，但不是精确覆盖。
 

提示：

1 <= rectangles.length <= 2 * 10^4
rectangles[i].length == 4
-10^5 <= xi, yi, ai, bi <= 10^5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/perfect-rectangle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
思路：扫描线

'''


class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        # 保存所有矩形的四个点
        lookup = set()
        # 最大矩形的 左下角 右上角
        x1 = float("inf")
        y1 = float("inf")
        x2 = float("-inf")
        y2 = float("-inf")
        area = 0
        for x, y, s, t in rectangles:

            x1 = min(x1, x)
            y1 = min(y1, y)
            x2 = max(x2, s)
            y2 = max(y2, t)

            area += (t - y) * (s - x)
            # 每个矩形的四个点
            for item in [(x, y), (x, t), (s, y), (s, t)]:
                if item not in lookup:
                    lookup.add(item)
                else:
                    lookup.remove(item)
        # 只剩下四个点并且是最大矩形的左下角和右上角
        if len(lookup) != 4 or \
                (x1, y1) not in lookup or (x1, y2) not in lookup or (x2, y1) not in lookup or (x2, y2) not in lookup:
            return False
        # 面积是否满足
        return (x2 - x1) * (y2 - y1) == area
