'''
面试题 01.05. 一次编辑
字符串有三种编辑操作:插入一个字符、删除一个字符或者替换一个字符。 给定两个字符串，编写一个函数判定它们是否只需要一次(或者零次)编辑。

 

示例 1:

输入:
first = "pale"
second = "ple"
输出: True
 

示例 2:

输入:
first = "pales"
second = "pal"
输出: False
'''
'''
思路：字符串
两个字符串的长度差不能超过1
对于长度相同的字符串：判断是否只有1个或0个字符不同
对于长度相差1的字符串：判断是否只有1个字符不同

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        if abs(len(first) - len(second)) > 1:
            return False
        if len(first) == len(second):  # 同长度字符串对比
            diff = 0
            i, n = 0, len(first)
            while i < n:
                if first[i] != second[i]:
                    diff += 1
                    if diff > 1:
                        return False
                i += 1
            return True
        if len(first) > len(second):  # 交换2个字符串，确保first是长度较小的那个
            first, second = second, first
        diff, i, j, n = 0, 0, 0, len(first)
        while i < n:
            if first[i] != second[j]:  # 不同长度字符串对比，如果出行不同，较长的字符串指针向后移动一个
                j += 1
                diff += 1
                if diff > 1:
                    return False
            else:
                i += 1
                j += 1
        return True
