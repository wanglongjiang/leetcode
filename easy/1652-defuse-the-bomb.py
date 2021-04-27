'''
拆炸弹
你有一个炸弹需要拆除，时间紧迫！你的情报员会给你一个长度为 n 的 循环 数组 code 以及一个密钥 k 。

为了获得正确的密码，你需要替换掉每一个数字。所有数字会 同时 被替换。

如果 k > 0 ，将第 i 个数字用 接下来 k 个数字之和替换。
如果 k < 0 ，将第 i 个数字用 之前 k 个数字之和替换。
如果 k == 0 ，将第 i 个数字用 0 替换。
由于 code 是循环的， code[n-1] 下一个元素是 code[0] ，且 code[0] 前一个元素是 code[n-1] 。

给你 循环 数组 code 和整数密钥 k ，请你返回解密后的结果来拆除炸弹！

n == code.length
1 <= n <= 100
1 <= code[i] <= 100
-(n - 1) <= k <= n - 1
'''
from typing import List
'''
思路：前缀和
如果k=0之间返回为0的数组
否则求code的前缀和数组prefixSums
然后利用前缀和的性质，每位数字的解码结果通过O(1)次运算可以得到
时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * n
        prefixSums, ans = [0] * n, [0] * n
        prefixSums[0] = code[0]
        for i in range(1, n):  # 求前缀和
            prefixSums[i] = prefixSums[i - 1] + code[i]
        if k > 0:  # 向后求和
            for i in range(n):
                if i + k <= n - 1:  # 后面k个元素全部在右边
                    ans[i] = -prefixSums[i] + prefixSums[i + k]
                else:  # 部分元素在左边
                    ans[i] = -prefixSums[i] + prefixSums[n - 1] + prefixSums[k - (n - 1 - i) - 1]
        else:  # 向前求和
            k = -k
            for i in range(n):
                if i >= k:  # 全部在左边
                    start = i - k
                    if start == 0:
                        ans[i] = prefixSums[i - 1]
                    else:
                        ans[i] = prefixSums[i - 1] - prefixSums[start - 1]
                else:  # 部分在右边
                    remainder = k - i
                    if i > 0:
                        ans[i] += prefixSums[i - 1]
                    ans[i] += prefixSums[n - 1] - prefixSums[n - 1 - remainder]
        return ans


s = Solution()
print(s.decrypt(code=[5, 7, 1, 4], k=3))
print(s.decrypt(code=[1, 2, 3, 4], k=0))
print(s.decrypt(code=[2, 4, 9, 3], k=-2))
