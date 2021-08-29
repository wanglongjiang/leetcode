'''
800. 相似 RGB 颜色
RGB 颜色用十六进制来表示的话，每个大写字母都代表了某个从 0 到 f 的 16 进制数。

RGB 颜色 "#AABBCC" 可以简写成 "#ABC" 。例如，"#15c" 其实是 "#1155cc" 的简写。

现在，假如我们分别定义两个颜色 "#ABCDEF" 和 "#UVWXYZ"，则他们的相似度可以通过这个表达式 -(AB - UV)^2 - (CD - WX)^2 - (EF - YZ)^2 来计算。

那么给定颜色 "#ABCDEF"，请你返回一个与 #ABCDEF 最相似的 7 个字符代表的颜色，并且它是可以被简写形式表达的。（比如，可以表示成类似 "#XYZ" 的形式）

示例 1：
输入：color = "#09f166"
输出："#11ee66"
解释：
因为相似度计算得出 -(0x09 - 0x11)^2 -(0xf1 - 0xee)^2 - (0x66 - 0x66)^2 = -64 -9 -0 = -73
这已经是所有可以简写的颜色中最相似的了
注意：

color 是一个长度为 7 的字符串
color 是一个有效的 RGB 颜色：对于仍和 i > 0，color[i] 都是一个在 0 到 f 范围的 16 进制数
假如答案具有相同的（最大）相似度的话，都是可以被接受的
所有输入、输出都必须使用小写字母，并且输出为 7 个字符
'''
import bisect
'''
思路：数学
可以缩写的数是00..ff
依次查找与3个字节最接近的数值

时间复杂度：O(1)
'''


class Solution:
    def similarRGB(self, color: str) -> str:
        def getClosest(num):
            nums = [
                0,
                int('11', 16),
                int('22', 16),
                int('33', 16),
                int('44', 16),
                int('55', 16),
                int('66', 16),
                int('77', 16),
                int('88', 16),
                int('99', 16),
                int('aa', 16),
                int('bb', 16),
                int('cc', 16),
                int('dd', 16),
                int('ee', 16),
                int('ff', 16)
            ]
            i = bisect.bisect_left(nums, num)
            if i == 0:
                return '00'
            elif i == 16:
                return 'ff'
            else:
                return hex(nums[i - 1])[2:] if num - nums[i - 1] < nums[i] - num else hex(nums[i])[2:]

        return '#' + getClosest(int(color[1:3], 16)) + getClosest(int(color[3:5], 16)) + getClosest(int(color[5:7], 16))


s = Solution()
print(s.similarRGB("#09f166"))
