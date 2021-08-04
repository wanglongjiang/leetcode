'''
自除数
自除数 是指可以被它包含的每一位数除尽的数。

例如，128 是一个自除数，因为 128 % 1 == 0，128 % 2 == 0，128 % 8 == 0。

还有，自除数不允许包含 0 。

给定上边界和下边界数字，输出一个列表，列表的元素是边界（含边界）内所有的自除数。

示例 1：

输入：
上边界left = 1, 下边界right = 22
输出： [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
注意：

每个输入参数的边界满足 1 <= left <= right <= 10000。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/self-dividing-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from collections import List
'''
思路：按照题意进行模拟计算
遍历从left到right的所有数值，按照题意判断是否是自除数，如果是，加入list

时间复杂度：O(nlogn)，n==right-left+1，每个自除数的判断需要时间复杂度是O(logn)
空间复杂度：O(1)
'''


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for num in range(left, right + 1):
            d = num
            while d:
                d, r = divmod(d, 10)
                if r == 0 or num % r != 0:  # 自除数的每一位不能是0，除以每一位能除尽
                    break
            else:
                ans.append(num)
        return ans
