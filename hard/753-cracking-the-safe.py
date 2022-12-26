'''
753. 破解保险箱
困难
113
相关企业
有一个需要密码才能打开的保险箱。密码是 n 位数, 密码的每一位是 k 位序列 0, 1, ..., k-1 中的一个 。

你可以随意输入密码，保险箱会自动记住最后 n 位输入，如果匹配，则能够打开保险箱。

举个例子，假设密码是 "345"，你可以输入 "012345" 来打开它，只是你输入了 6 个字符.

请返回一个能打开保险箱的最短字符串。

 

示例1:

输入: n = 1, k = 2
输出: "01"
说明: "10"也可以打开保险箱。
 

示例2:

输入: n = 2, k = 2
输出: "00110"
说明: "01100", "10011", "11001" 也能打开保险箱。
 

提示：

n 的范围是 [1, 4]。
k 的范围是 [1, 10]。
k^n 最大可能为 4096。
 
'''
'''
[TOC]

# 思路
欧拉回路

# 解题方法
> 想要打开保险柜的序列，必须含有所有的长度为n的序列组合，也就是k^n个子序列
> 而如果想要字符串最短，最好是每个长度为k的子序列，前k-1个字符是前一个子序列的后缀。
> 这种序列存不存在呢，考虑欧拉回路的定义，如果有向图的每个节点的入度和出度相同，那么存在欧拉回路。
> 恰好每个长度为k的子序列，它的后k-1个字符为前缀的序列有n个，它的前k-1个字符作为后缀的序列也有n个
> 那么可以用DFS找到一条欧拉回路。


# 复杂度
- 时间复杂度: 
> $O(k^n)$

- 空间复杂度: 
> $O(k^n)$
'''


class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        m = 10**(n - 1)
        ans = []
        marked = set()  # 保存已经遍历过的节点

        def dfs(x):
            prefix = x * 10
            for num in range(k):
                if prefix + num not in marked:
                    marked.add(prefix + num)
                    dfs((prefix + num) % m)
                    ans.append(num)

        dfs(0)
        return ''.join(map(str, ans)) + "0" * (n - 1)


s = Solution()
print(s.crackSafe(3, 2))
print(s.crackSafe(2, 4))
print(s.crackSafe(2, 3))
print(s.crackSafe(n=1, k=2))
print(s.crackSafe(n=2, k=2))
