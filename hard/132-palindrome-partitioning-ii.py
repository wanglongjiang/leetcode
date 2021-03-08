'''
分割回文串 II
给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文。

返回符合要求的 最少分割次数 。
'''
'''
思路1，利用131的分割回文串算法找出所有的回文串，然后找出其中长度最短的
    时间复杂度：O(n^3) 超出时间。。。。
思路2，也可以只调用131算法的前半部分，并进行优化。
    不再遍历所有位置开头的字符串，而是按需优化，只有1个字符串为回文串，才判断该字符串的下一个位置是否为回文串。
    时间复杂度：O(n^3) 超出时间。。。。
思路1、思路2 大体思路相同，但回文串的判断使用了O(n^3)的时间
思路3，动态规划。双重动态规划。
    1、判断一个字符串s[i:j]是否为回文串，可以从s[i+1:j-1]和s[i]==s[j]来判断
        通过1个二维数组，m来计算所有子字符串是否为回文串，相比上面的2个思路，时间复杂度降低了1个维度
    2、从第1个字符到最后1个字符最少可以划分多少回文串，可以通过1个辅助数组，
        针对每个位置i，向前搜索所有能到达i的回文串个数。
    时间复杂度：O(n^2)
'''


class Solution:
    # 思路3
    def minCut(self, s: str) -> int:
        n = len(s)
        # 判断所有子字符串是否为回文串
        m = [[True] * n for i in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                m[i][j] = s[i] == s[j] and m[i + 1][j - 1]
        # 查找最少回文串数
        minNums = [n - 1] * n  # 最多为n-1次分割
        for i in range(n):
            if m[0][i]:
                minNums[i] = 0
            else:
                for j in range(i):
                    if m[j + 1][i]:
                        minNums[i] = min(minNums[i], minNums[j] + 1)
        return minNums[n - 1]

    # 思路2
    def minCut2(self, s: str) -> int:
        n = len(s)

        def isPalin(i: int, j: int):
            if mem[i][j - i - 1] is not None:
                return mem[i][j - i - 1]
            for k in range((j - i) // 2):
                if s[i + k] != s[j - k - 1]:
                    mem[i][j - i - 1] = False
                    return False
            mem[i][j - i - 1] = True
            return True

        def backtrack(i, level, minCutNum):
            if level > minCutNum:
                return minCutNum
            for j in range(n, i, -1):
                if isPalin(i, j):
                    if j == n:
                        return level
                    else:
                        return min(minCutNum, backtrack(j, level + 1, minCutNum))
            return minCutNum

        # 记忆表
        mem = [None] * n
        for i in range(n):
            mem[i] = [None] * (n - i)
        return backtrack(0, 0, n - 1)

    # 思路1
    def minCut1(self, s: str) -> int:
        ans = []
        n = len(s)
        seq = []
        # 迭代所有可能子串，并判断是否回文，保存起来
        mem = [0] * n
        for i in range(n):
            mem[i] = [True] * (n - i)
            for j in range(i + 2, n + 1):
                subLen = (j - i) // 2
                for k in range(subLen):
                    if s[i + k] != s[j - k - 1]:
                        mem[i][j - i - 1] = False
                        break

        # 回溯
        def backtrack(k: int):
            for i in range(k + 1, n + 1):
                if mem[k][i - k - 1]:
                    if i == n:
                        seq.append(s[k:i])
                        ans.append(len(seq) - 1)
                        seq.pop()
                    else:
                        seq.append(s[k:i])
                        backtrack(i)
                        seq.pop()

        backtrack(0)
        return min(ans)


s = Solution()
print(s.minCut("fifgbeajcacehiicccfecbfhhgfiiecdcjjffbghdidbhbdbfbfjccgbbdcjheccfbhafehieabbdfeigbiaggchaeghaijfbjhi"))
print(s.minCut("ababababababababababababcbabababababababababababa"))
print(s.minCut("eegiicgaeadbcfacfhifdbiehbgejcaeggcgbahfcajfhjjdgj"))
print(s.minCut("aabbaa"))
print(s.minCut("aabb"))
print(s.minCut("aab"))
print(s.minCut("a"))
print(s.minCut("ab"))
