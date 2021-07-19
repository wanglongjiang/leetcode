'''
强整数
给定两个正整数 x 和 y，如果某一整数等于 x^i + y^j，其中整数 i >= 0 且 j >= 0，那么我们认为该整数是一个强整数。

返回值小于或等于 bound 的所有强整数组成的列表。

你可以按任何顺序返回答案。在你的回答中，每个值最多出现一次。

 

示例 1：

输入：x = 2, y = 3, bound = 10
输出：[2,3,4,5,7,9,10]
解释：
2 = 2^0 + 3^0
3 = 2^1 + 3^0
4 = 2^0 + 3^1
5 = 2^1 + 3^1
7 = 2^2 + 3^1
9 = 2^3 + 3^0
10 = 2^0 + 3^2
示例 2：

输入：x = 3, y = 5, bound = 15
输出：[2,4,6,8,10,14]
'''
from typing import List
'''
思路：数学 哈希集合
生成2个指数list，expX = [x^0,x^1,x^2...<bound],expY=[y^0,y^1,y^2..<bound]
然后遍历expX，将其与expY中的元素进行求和，将<=bound的和加入哈希集合中
最后将哈希集合输出

时间复杂度：O(log(bound)^2))
空间复杂度：O(log(bound))
'''


class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        # 求出x,y的指数列表
        expX, expY = [1], [1]
        if x != 1:
            exp = x
            while exp < bound:
                expX.append(exp)
                exp *= x
        if y != 1:
            exp = y
            while exp < bound:
                expY.append(exp)
                exp *= y
        # 遍历x的指数列表，将其与y的指数相加，将<=bound的加入哈希集合
        ans = set()
        for a in expX:
            for b in expY:
                if a + b <= bound:
                    ans.add(a + b)
                else:
                    break
        return list(ans)


s = Solution()
print(s.powerfulIntegers(x=2, y=3, bound=10))
print(s.powerfulIntegers(x=3, y=5, bound=15))
print(s.powerfulIntegers(x=1, y=5, bound=26))
print(s.powerfulIntegers(x=1, y=1, bound=15))
