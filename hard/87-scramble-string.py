'''
扰乱字符串
给定一个字符串 s1，我们可以把它递归地分割成两个非空子字符串，从而将其表示为二叉树。

下图是字符串 s1 = "great" 的一种可能的表示形式。

    great
   /    \\
  gr    eat
 / \\    /  \\
g   r  e   at
           / \\
          a   t
在扰乱这个字符串的过程中，我们可以挑选任何一个非叶节点，然后交换它的两个子节点。

例如，如果我们挑选非叶节点 "gr" ，交换它的两个子节点，将会产生扰乱字符串 "rgeat" 。

    rgeat
   /    \\
  rg    eat
 / \\    /  \\
r   g  e   at
           / \\
          a   t
我们将 "rgeat” 称作 "great" 的一个扰乱字符串。

同样地，如果我们继续交换节点 "eat" 和 "at" 的子节点，将会产生另一个新的扰乱字符串 "rgtae" 。

    rgtae
   /    \\
  rg    tae
 / \\    /  \\
r   g  ta  e
       / \\
      t   a
我们将 "rgtae” 称作 "great" 的一个扰乱字符串。

给出两个长度相等的字符串 s1 和 s2，判断 s2 是否是 s1 的扰乱字符串。

s1.length == s2.length
1 <= s1.length <= 30
s1 和 s2 由小写英文字母组成
'''
'''
思路，递归+记忆化
按照题目定义，按照任意位置分隔成2个子串，递归判断子串是否互为扰乱字符串
'''


class Solution:
    # 递归+记忆化
    def isScramble(self, s1: str, s2: str) -> bool:
        cache = {}
        from collections import Counter

        def issc(s1, s2):
            if s1 == s2:
                return True
            key = s1 + s2
            n = len(s1)
            if key in cache:
                return cache[key]
            if Counter(s1) != Counter(s2):  # 判断内部字符个数是否相同
                cache[key] = False
                return False
            for i in range(1, n):
                if issc(s1[:i], s2[:i]) and issc(s1[i:n], s2[i:n]):
                    return True
                if issc(s1[:i], s2[n - i:n]) and issc(s1[i:n], s2[:n - i]):
                    return True
            cache[key] = False
            return False

        return issc(s1, s2)


s = Solution()
print(s.isScramble("abc", "bca"))
print(s.isScramble(s1="aa", s2="aa"))
print(s.isScramble(s1="great", s2="rgeat"))
print(s.isScramble(s1="abcde", s2="caebd"))
