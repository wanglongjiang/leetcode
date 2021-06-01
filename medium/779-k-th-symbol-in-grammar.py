'''
第K个语法符号

在第一行我们写上一个 0。接下来的每一行，将前一行中的0替换为01，1替换为10。

给定行数 N 和序数 K，返回第 N 行中第 K个字符。（K从1开始）
注意：

N 的范围 [1, 30].
K 的范围 [1, 2^(N-1)].
解释:
第一行: 0
第二行: 01
第三行: 0110
第四行: 01101001
第5行： 0110100110010110
'''
from collections import deque
'''
思路1：暴力计算
按照定义，生成第n行的第k个数据

时间复杂度：O(2^n)
空间复杂度：O(K)

思路2：递归
第一行: 0
第二行: 01
第三行: 0110
第四行: 01101001
第5行： 0110100110010110
从上面的数字找一下规律，可以发现，每一行从中间分成2部分，左部分取反正好等于右部分。
所以：
> 如果k<=2^(n-2)，kthGrammar(n,k)=kthGrammar(n-2,k)
> 如果k>2^(n-2),kthGrammar(n,k)= kthGrammar(n-1,k-2^(n-2))取反
又，kthGrammar(1,1)=0

根据上面的思路写出递归函数
时间复杂度：O(logK)
空间复杂度：O(logK)
'''


class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if N == 1:
            return 0
        if K <= (1 << (N - 2)):
            return self.kthGrammar(N - 1, K)
        else:
            return 1 ^ self.kthGrammar(N - 1, K - (1 << (N - 2)))

    def kthGrammar1(self, N: int, K: int) -> int:
        q1, q2 = deque(), deque()
        q2.append(0)
        while len(q2) < K:
            if not q1:
                q1, q2 = q2, q1
            if q1.popleft():
                q2.append(1)
                q2.append(0)
            else:
                q2.append(0)
                q2.append(1)
        return q2[K - 1]


s = Solution()
print(s.kthGrammar(3, 1) == 0)
print(s.kthGrammar(3, 2) == 1)
print(s.kthGrammar(3, 3) == 1)
print(s.kthGrammar(3, 4) == 0)
print(s.kthGrammar(1, 1) == 0)
print(s.kthGrammar(2, 1) == 0)
print(s.kthGrammar(2, 2) == 1)
print(s.kthGrammar(4, 5) == 1)
