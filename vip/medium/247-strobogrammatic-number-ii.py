'''
247. 中心对称数 II
中心对称数是指一个数字在旋转了 180 度之后看起来依旧相同的数字（或者上下颠倒地看）。

找到所有长度为 n 的中心对称数。

示例 :

输入:  n = 2
输出: ["11","69","88","96"]
'''
from typing import List
'''
思路：组合 回溯
回溯生成对称数的组合，特别的，如果n为奇数，中间的数字只能是1或8

时间复杂度：O($5^(n/2)$)
'''


class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        numMap = {'1': '1', '8': '8', '6': '9', '9': '6', '0': '0'}
        ans = []

        def addToAns(li):  # 将前一半的数字拼接上后一半的对称数加入结果list
            s = li.copy()
            for i in range(n // 2 - 1, -1, -1):
                s.append(numMap[li[i]])
            ans.append(''.join(s))

        def backtrack(i, li):  # 回溯生成前一半数字的组合
            if n % 2 and i == (n // 2):  # 长度为奇数，中间的对称数字只能是0，1，8
                li.append('0')
                addToAns(li)
                li.pop()
                li.append('1')
                addToAns(li)
                li.pop()
                li.append('8')
                addToAns(li)
                li.pop()
            elif n % 2 == 0 and i == (n // 2):  # 长度为偶数，到达终点，根据一半的数字组合生成完整的对称数
                addToAns(li)
            elif i < (n // 2):  # 未到达终点
                nums = ['1', '6', '8', '9']
                if i > 0:
                    nums = ['0', '1', '6', '8', '9']
                for num in nums:
                    li.append(num)
                    backtrack(i + 1, li)
                    li.pop()

        backtrack(0, [])
        return ans


s = Solution()
print(s.findStrobogrammatic(1))
print(s.findStrobogrammatic(2))
print(s.findStrobogrammatic(3))
print(s.findStrobogrammatic(4))
print(s.findStrobogrammatic(5))
