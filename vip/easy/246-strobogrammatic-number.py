'''
246. 中心对称数
中心对称数是指一个数字在旋转了 180 度之后看起来依旧相同的数字（或者上下颠倒地看）。

请写一个函数来判断该数字是否是中心对称数，其输入将会以一个字符串的形式来表达数字。


示例 1:

输入: num = "69"
输出: true
示例 2:

输入: num = "88"
输出: true
示例 3:

输入: num = "962"
输出: false
示例 4：

输入：num = "1"
输出：true
'''
'''
思路：双指针
类似于回文串，不同的是6和9对称，8和8对称，1和1对称,0和0对称

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        left, right = 0, len(num) - 1
        numMap = {'1': '1', '8': '8', '6': '9', '9': '6', '0': '0'}
        while left < right:
            if num[left] in numMap and num[right] != numMap[num[left]]:
                return False
            left += 1
            right -= 1
        return True if left != right else (num[left] == '1' or num[left] == '8')


s = Solution()
print(s.isStrobogrammatic('69'))
print(s.isStrobogrammatic('88'))
print(s.isStrobogrammatic('962'))
print(s.isStrobogrammatic('898'))
print(s.isStrobogrammatic('1'))
