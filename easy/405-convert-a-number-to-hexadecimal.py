'''
数字转换为十六进制数
给定一个整数，编写一个算法将这个数转换为十六进制数。对于负整数，我们通常使用 补码运算 方法。

注意:

十六进制中所有字母(a-f)都必须是小写。
十六进制字符串中不能包含多余的前导零。如果要转化的数为0，那么以单个字符'0'来表示；对于其他情况，
十六进制字符串中的第一个字符将不会是0字符。 
给定的数确保在32位有符号整数范围内。
不能使用任何由库提供的将数字直接转换或格式化为十六进制的方法。
示例 1：

输入:
26

输出:
"1a"
示例 2：

输入:
-1

输出:
"ffffffff"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/convert-a-number-to-hexadecimal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
思路：数学
将0..F的10进制写入字符串hex
遍历num，用最低4位作为索引查询hex，将字符添加到结果中

时间复杂度：O(1)
'''


class Solution:
    def toHex(self, num: int) -> str:
        hex = '0123456789abcdef'
        ans, mask = '', 15
        for i in range(8):
            if num != 0:
                ans = hex[num & mask] + ans
                num >>= 4
            else:
                break
        if ans:
            return ans
        return '0'


s = Solution()
print(s.toHex(26))
print(s.toHex(-1))
