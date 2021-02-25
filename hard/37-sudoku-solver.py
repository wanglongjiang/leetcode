'''
解数独
编写一个程序，通过填充空格来解决数独问题。

一个数独的解法需遵循如下规则：

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
空白格用 '.' 表示。
'''
from typing import List
'''
思路：回溯
1、求出每个空格的可选数字列表：
    a、求每一行、每一列、每一9格的已有数字，分别记录到1个整数的1bit中。
    b、每个空格的可选list为该行、该列、9格3个整数数求或，为0的位
2、遍历每个空格s1，从可选列表中选中1个数字a，其余放到待选，
    再遍历跟此空格同行、同列、同9格的空格，将a从可选中删除，如果可行列表为空。回到s1,选择下一个可选。直至所有空格都变成已选
    每个空格有2种状态，已选、待选。
    每个可选状态的空格有1个列表存放可选列表、另外1个存放排除列表。
'''


class Item:
    def __init__(self):
        super().__init__()
        self.selected = 0
        self.optional = 0
        self.exclude = []
        self.row = 0
        self.col = 0
        self.nine = 0


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 设置了4个数组用于从行、列、9宫格3个维度分类所有空格。最后一个存放所有的空格
        rows, cols, nine, items = [[] for i in range(9)], [[] for i in range(9)], [[] for i in range(9)], []
        # 一、遍历数独求出每个空格的可选数字列表
        rowsOptional, colsOptional, nineOptional = [0x1ff] * 9, [0x1ff] * 9, [0x1ff] * 9
        for i in range(9):
            for j in range(9):
                if board[i][j].isdigit():
                    n = int(board[i][j])
                    exclude = 1 << (n - 1)
                    rowsOptional[i] ^= exclude
                    colsOptional[j] ^= exclude
                    nineOptional[i // 3 * 3 + j // 3] ^= exclude
                else:  # 创建空格，并进行分类
                    item = Item()
                    item.row, item.col, item.nine = i, j, i // 3 * 3 + j // 3
                    rows[i].append(item)
                    cols[j].append(item)
                    nine[item.nine].append(item)
                    items.append(item)
        for item in items:
            # 每个空格的可选数字为同行、同列、同9宫的可选数字交集
            item.optional = rowsOptional[item.row] & colsOptional[item.col] & nineOptional[item.nine]
        # 二、遍历每个空格s1，从可选列表中选中1个数字a，
        #   再遍历跟此空格同行、同列、同9格的空格，将a从可选中排除：
        #       如果可行列表为空，说明此选择不可行，需要回到s1,选择下一个可选。
        #   直至所有空格都变成已选，得到解
        from functools import reduce

        def appendExclude(arr, item, num):
            for other in arr:
                if other is not item and other.selected == 0:
                    other.exclude.append(num)

        def removeExclude(arr, item, num):
            for other in arr:
                if other is not item and other.selected == 0:
                    other.exclude.remove(num)

        def backtrack(index: int):
            item = items[index]
            # 对可选数字进行更新
            optional = item.optional & ~(reduce(lambda a, b: a | b, item.exclude, 0x0))
            if optional == 0:
                return False
            for i in range(9):
                if optional & 1 == 1:  # 遍历可选数字
                    item.selected = i + 1  # 选中一个数字
                    if index == len(items) - 1:  # 最后一个空格被选中，找到解
                        return True
                    # 不是最后一个，选中数字后对同行、同列、同9宫的造成影响
                    appendExclude(rows[item.row], item, 1 << i)
                    appendExclude(cols[item.col], item, 1 << i)
                    appendExclude(nine[item.nine], item, 1 << i)
                    # 回溯
                    if backtrack(index + 1):
                        return True
                    # 恢复对同行、同列、同9宫的影响
                    removeExclude(rows[item.row], item, 1 << i)
                    removeExclude(cols[item.col], item, 1 << i)
                    removeExclude(nine[item.nine], item, 1 << i)
                optional >>= 1
                if optional == 0:
                    break
            item.selected = 0
            return False

        backtrack(0)
        # 三、根据解，写入原数独
        for item in items:
            if item.selected > 0:
                board[item.row][item.col] = str(item.selected)


s = Solution()
s1 = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."],
      ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
      [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
s.solveSudoku(s1)
print(s1)
