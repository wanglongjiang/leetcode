'''
单词搜索
给定一个二维网格和一个单词，找出该单词是否存在于网格中。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。
同一个单元格内的字母不允许被重复使用。
'''
from typing import List
'''
思路1：遍历矩阵每个位置，然后回溯搜索
时间复杂度：遍历矩阵m*n，回溯搜索3^k，总计m*n*3^k
会超出时间限制

'''


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        pass
