'''
交错字符串
给定三个字符串 s1、s2、s3，请你帮忙验证 s3 是否是由 s1 和 s2 交错 组成的。

两个字符串 s 和 t 交错 的定义与过程如下，其中每个字符串都会被分割成若干 非空 子字符串：

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
交错 是 s1 + t1 + s2 + t2 + s3 + t3 + ... 或者 t1 + s1 + t2 + s2 + t3 + s3 + ...
提示：a + b 意味着字符串 a 和 b 连接。
'''
'''
思路：
第1反应是遍历s3的字符，交替与s1、s2进行对比，如果能走到最后，就能证明是交错字符串
能不能找到一个交替字符串，不满足上面的算法呢？
可以找到：s1=aaab, s2=abc, s3=aabcaab，如果从s1开始对比，会无法走到最后

经过一番思考，尝试用回溯解决问题
对于s3的当前字符，与s1、s2的当前位置字符进行对比，（3个字符串初始都从0开始）
    如果s3[i]==s1[j] or s3[i]==s2[k] 需要先后尝试与s1、s2匹配，进入下一个字符
    如果都不相同，不能匹配。
'''


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len3, len1, len2 = len(s3), len(s1), len(s2)
        if len3 != len2 + len1:
            return False

        def backtrack(i, j, k):
            if i == len3:  # s3的当前位置已经匹配完成
                return True
            if j < len1 and s3[i] == s1[j]:
                if backtrack(i + 1, j + 1, k):
                    return True
            if k < len2 and s3[i] == s2[k]:
                if backtrack(i + 1, j, k + 1):
                    return True
            return False

        return backtrack(0, 0, 0)


s = Solution()
print(s.isInterleave(s1="aabcc", s2="dbbca", s3="aadbbcbcac"))
print(s.isInterleave(s1="aabcc", s2="dbbca", s3="aadbbbaccc"))
print(s.isInterleave(s1="", s2="", s3=""))
