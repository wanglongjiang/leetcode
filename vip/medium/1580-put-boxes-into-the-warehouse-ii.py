'''
1580. 把箱子放进仓库里 II
给定两个正整数数组 boxes 和 warehouse ，分别包含单位宽度的箱子的高度，以及仓库中n个房间各自的高度。仓库的房间分别从0 到 n - 1自左向右编号，warehouse[i]（索引从 0 开始）是第 i 个房间的高度。

箱子放进仓库时遵循下列规则：

箱子不可叠放。
你可以重新调整箱子的顺序。
箱子可以从任意方向（左边或右边）推入仓库中。
如果仓库中某房间的高度小于某箱子的高度，则这个箱子和之后的箱子都会停在这个房间的前面。
你最多可以在仓库中放进多少个箱子？

 

示例 1:


输入: boxes = [1,2,2,3,4], warehouse = [3,4,1,2]
输出: 4
解释:

我们可以按如下顺序推入箱子:
1- 从左边或右边把黄色箱子推入2号房间；
2- 从右边把橙色箱子推入3号房间；
3- 从左边把绿色箱子推入1号房间；
4- 从左边把红色箱子推入0号房间；
还有其他方式推入4个箱子，比如交换红色与绿色箱子，或者交换红色与橙色箱子。
示例 2:


输入: boxes = [3,5,5,2], warehouse = [2,1,3,4,5]
输出: 3
解释:

因为只有一个高度大于等于5的房间，所以无法将两个高度为5的箱子都推入仓库。
还有其他方式推入箱子，比如将绿色箱子推入2号房间，或者在绿色及红色箱子之前将橙色箱子推入2号房间。
示例 3:

输入: boxes = [1,2,3], warehouse = [1,2,3,4]
输出: 3
示例 4:

输入: boxes = [4,5,6], warehouse = [3,3,3,3,3]
输出: 0
 

提示:

n == warehouse.length
1 <= boxes.length, warehouse.length <= 10^5
1 <= boxes[i], warehouse[i] <= 10^9
'''
from typing import List
'''
思路：TODO
'''


class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        pass
