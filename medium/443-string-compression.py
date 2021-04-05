'''
压缩字符串
给定一组字符，使用原地算法将其压缩。

压缩后的长度必须始终小于或等于原数组长度。

数组的每个元素应该是长度为1 的字符（不是 int 整数类型）。

在完成原地修改输入数组后，返回数组的新长度。

 

进阶：
你能否仅使用O(1) 空间解决问题？

提示：

所有字符都有一个ASCII值在[35, 126]区间内。
1 <= len(chars) <= 1000。
'''
from typing import List
'''
思路：一次遍历（官方的给这个思路叫双指针，指i和j）
使用变量pre存储前一个字符，如果与先字符不一致，重新开始计数，当计数大于1时输出到结果中
时间复杂度：O(n)
空间复杂度：O(1)，不算返回值，使用常数个辅助空间

'''


class Solution:
    def compress(self, chars: List[str]) -> int:
        pre, count = chars[0], 1
        n = len(chars)
        i, j = 1, 0
        while i < n:
            ch = chars[i]
            i += 1
            if pre != ch:
                chars[j] = pre
                j += 1
                if count > 1:
                    cnt = str(count)
                    for k in cnt:
                        chars[j] = k
                        j += 1
                count = 1
                pre = ch
            else:
                count += 1
        chars[j] = pre
        j += 1
        if count > 1:
            cnt = str(count)
            for k in cnt:
                chars[j] = k
                j += 1
        return j


s = Solution()

print(s.compress(["a", "a", "b", "b", "c", "c", "c"]))
print(s.compress(["a"]))
print(s.compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]))
