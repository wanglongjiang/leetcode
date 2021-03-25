'''
编辑距离
给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符

'''
'''
思路：双重动态规划。
第1个动态规划求2个字符串的最长公共子序列（lcs）
第2个动态规划求公共子序列的某个字符匹配与否的最小编辑距离。
时间复杂度：O(m*n)，第1个动态规划需要O(mn)，第2个动态规划O(len(lcs))<O(min(m,n))
空间复杂度：O(m*n)，第1个动态规划需要O(mn)，第2个动态规划O(len(lcs))
'''


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)

        # 第1次动态规划求lcs
        def getCount(cm, x, y):
            if x < 0 or y < 0:
                return 0
            return cm[x][y]

        # 创建lcs查询矩阵
        def makeLcsCountMatrix():
            cm = [[0] * n2 for i in range(n1)]
            for i in range(n1):
                for j in range(n2):
                    if word1[i] == word2[j]:
                        cm[i][j] = getCount(cm, i - 1, j - 1) + 1
                    elif getCount(cm, i - 1, j) >= getCount(cm, i, j - 1):
                        cm[i][j] = getCount(cm, i - 1, j)
                    else:
                        cm[i][j] = getCount(cm, i, j - 1)
            return cm

        cm = makeLcsCountMatrix()
        # 下面2个数组存储2个单词的lcs坐标
        lcsPosition1, lcsPosition2 = [], []
        # 遍历矩阵，将lcs子串坐标找出来
        i, j = n1 - 1, n2 - 1
        while i >= 0 and j >= 0:
            lcsLeftUp = getCount(cm, i - 1, j - 1)
            lcsLeft = getCount(cm, i, j - 1)
            lcsUp = getCount(cm, i - 1, j)
            if cm[i][j] > lcsLeftUp and cm[i][j] > lcsLeft and cm[i][j] > lcsUp:
                lcsPosition1.append(i)
                lcsPosition2.append(j)
                i -= 1
                j -= 1
            elif lcsUp >= lcsLeft:
                i -= 1
            else:
                j -= 1
        if len(lcsPosition1) == 0:  # 没有lcs，需要变动的字符数为2个字符串的较长长度
            return max(n1, n2)
        lcsPosition1.reverse()
        lcsPosition2.reverse()
        # 第2次动态规划，设置2个数组match,nomatch与lcs长度相同，里面存储当前坐标匹配、不匹配的长度。动态规划方程如下：
        # 第i个坐标进行匹配，其编辑长度为 min(match[i-1],nomatch[i-1])+ max(lcsPosition1[i+1]-lcsPosition1[i],lcsPosition2[i+1]-lcsPosition2[i])-1
        # 第i个坐标不匹配，其编辑长度为 min( min(match[i-1],nomatch[i-1])+ max(lcsPosition1[i+1]-lcsPosition1[i],lcsPosition2[i+1]-lcsPosition2[i]),
        #   max(lcsPosition1[i+1], lcsPosition2[i+1]))
        # 第0个坐标匹配，其编辑长度为 max(lcsPosition1[0],lcsPosition1[0])+max(lcsPosition1[i+1]-lcsPosition1[0],lcsPosition2[i+1]-lcsPosition2[i])-1
        # 第0个坐标不匹配，其编辑长度为 max(lcsPosition1[i+1],lcsPosition2[i+1])
        lcsLen = len(lcsPosition1)
        match, nomatch = [0] * lcsLen, [0] * lcsLen
        rightIndex1, rightIndex2 = 0, 0
        if lcsLen == 1:
            rightIndex1 = n1
            rightIndex2 = n2
        else:
            rightIndex1 = lcsPosition1[1]
            rightIndex2 = lcsPosition2[1]
        match[0] = max(lcsPosition1[0], lcsPosition2[0]) + max(rightIndex1 - lcsPosition1[0], rightIndex2 - lcsPosition2[0]) - 1
        nomatch[0] = max(rightIndex1, rightIndex2)
        for i in range(1, lcsLen):
            if i + 1 == lcsLen:
                rightIndex1, rightIndex2 = n1, n2
            else:
                rightIndex1, rightIndex2 = lcsPosition1[i + 1], lcsPosition2[i + 1]
            match[i] = min(match[i - 1], nomatch[i - 1]) + max(rightIndex1 - lcsPosition1[i], rightIndex2 - lcsPosition2[i]) - 1
            nomatch[i] = min(match[i] + 1, max(rightIndex1, rightIndex2))
        return min(match[-1], nomatch[-1])


s = Solution()
print(s.minDistance("horse", "ros"))
print(s.minDistance("intention", "execution"))
