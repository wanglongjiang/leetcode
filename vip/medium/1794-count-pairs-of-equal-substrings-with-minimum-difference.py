'''
1794. 统计距离最小的子串对个数
输入数据为两个字符串firstString 和 secondString，两个字符串下标均从0开始，且均只包含小写的英文字符，请计算满足下列要求的下标四元组(i,j,a,b)的个数：

0 <= i <= j < firstString.length
0 <= a <= b < secondString.length
firstString字符串中从i位置到j位置的子串(包括j位置的字符)和secondString字符串从a位置到b位置的子串(包括b位置字符)相等
j-a的数值是所有符合前面三个条件的四元组中可能的最小值
返回符合上述 4 个条件的四元组的 个数 。



示例1：

输入：firstString = "abcd", secondString = "bccda"
输出：1
解释：(0,0,4,4)是唯一符合条件的四元组且其j-a的数值是最小的.
示例 2：

输入：firstString = "ab", secondString = "cd"
输出：0
解释：没有任何一个四元组能满足上述4个要求.


提示：

1 <= firstString.length, secondString.length <= 2 * 105
两个输入字符串均只包含小写英文字符.
'''
'''
思路：TODO
'''


class Solution:
    def countQuadruples(self, firstString: str, secondString: str) -> int:
        pass
