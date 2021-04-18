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
'''
思路：暴力计算
从上面的数据可以看出，低一行是高一行的前缀，可以直接生成第N行的数据
时间复杂度：O(K)
空间复杂度：O(K)
TODO 计算错误
'''


class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        i = 0
        bits = [0]
        while len(bits) < K:
            if bits[i]:
                bits.append(0)
                bits.append(1)
            else:
                bits.append(1)
                bits.append(0)
            i += 1
        return bits[K - 1]


s = Solution()
print(s.kthGrammar(1, 1))
print(s.kthGrammar(2, 1))
print(s.kthGrammar(2, 2))
print(s.kthGrammar(4, 5))
