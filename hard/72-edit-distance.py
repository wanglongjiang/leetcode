'''
编辑距离
给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符

'''
'''
思路：求2个字符串的最长公共子序列（lcs），word1中2个子序列之间如果间隔小于word12个子序列的间隔，需要插入，其他word1的字符需要替换或者删除
时间复杂度：O(m*n)
空间复杂度：O(m*n)
'''


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)

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
        # 遍历lcs坐标，将word1比word2的lcs字串间缺少的字符数统计出来
        lcsLen = len(lcsPosition1)
        for i in range(lcsLen):
            print(word1[lcsPosition1[i]], end='')
        lack = 0 if (lcsPosition1[0] >= lcsPosition2[0]) else (lcsPosition2[0] - lcsPosition1[0])
        lack += 0 if (n2 - lcsPosition2[lcsLen - 1] <= n1 - lcsPosition1[lcsLen - 1]) else (n2 - lcsPosition2[lcsLen - 1] - (n1 - lcsPosition1[lcsLen - 1]))
        for i in range(1, lcsLen):
            interval1 = lcsPosition1[i] - lcsPosition1[i - 1]
            interval2 = lcsPosition2[i] - lcsPosition2[i - 1]
            if interval2 > interval1:
                lack += interval2 - interval1
        return lack + n1 - lcsLen


s = Solution()
print(s.minDistance("horse", "ros"))
print(s.minDistance("intention", "execution"))