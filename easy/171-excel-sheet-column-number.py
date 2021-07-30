'''
Excel表列序号
给定一个Excel表格中的列名称，返回其相应的列序号。

例如，

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
示例 1:

输入: "A"
输出: 1
示例 2:

输入: "AB"
输出: 28
示例 3:

输入: "ZY"
输出: 701

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/excel-sheet-column-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
思路：数学
从左到右遍历每个字符，
当前字符值为val = ascii(char)-ascii('a')+1
总计值为ans*26+val。其中ans初始为0

时间复杂度：O(n)，n为columnTitle.length
空间复杂度：O(1)
'''


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        for c in columnTitle:
            ans = ans * 26 + ord(c) - ord('A') + 1
        return ans


s = Solution()
print(s.titleToNumber('A'))
print(s.titleToNumber('AB'))
print(s.titleToNumber('ZY'))
