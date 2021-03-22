'''
矩形面积
在二维平面上计算出两个由直线构成的矩形重叠后形成的总面积。

每个矩形由其左下顶点和右上顶点坐标表示，如图所示。
'''
'''
思路：假设2个矩形总有重叠。重叠部分的左下角为2个左下角的较大值，右上角为2个右上角的较小值。
如果测试用例中有不重叠的部分，需要判断是否重叠。
时间复杂度：O(1)
空间复杂度：O(1)
'''


class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        areaC = 0
        areaA, areaB = (C - A) * (D - B), (G - E) * (H - F)
        if not (A > G or B > H or C < E or D < F):  # 判断是否重叠
            areaC = (min(C, G) - max(A, E)) * (min(D, H) - max(B, F))
        return areaA + areaB - areaC


s = Solution()
print(s.computeArea(-3, 0, 3, 4, 0, -1, 9, 2))
