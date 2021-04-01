'''
保证文件名唯一
给你一个长度为 n 的字符串数组 names 。你将会在文件系统中创建 n 个文件夹：在第 i 分钟，新建名为 names[i] 的文件夹。

由于两个文件 不能 共享相同的文件名，因此如果新建文件夹使用的文件名已经被占用，系统会以 (k) 的形式为新文件夹的文件名添加后缀，
其中 k 是能保证文件名唯一的 最小正整数 。

返回长度为 n 的字符串数组，其中 ans[i] 是创建第 i 个文件夹时系统分配给该文件夹的实际名称。

提示：

1 <= names.length <= 5 * 10^4
1 <= names[i].length <= 20
names[i] 由小写英文字母、数字和/或圆括号组成。

'''
from typing import List
'''
思路：字典树
根据输入建立字典树，如果在字典树中找到，尝试后面附加(1)开始寻找，直至找到不冲突的
时间复杂度：O(mn)
空间复杂度：O(mn)
'''


class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        trie = {}
        trieEnd = set()
        repetWord = {}

        # 添加单词
        def add(word):
            node = trie
            isNew = False
            for c in word:
                if c not in node:
                    node[c] = {}  # 每个新增节点都是dict
                    isNew = True
                node = node[c]
            nodeid = id(node)
            if isNew or nodeid not in trieEnd:
                trieEnd.add(nodeid)
                return word
            # 不是新节点，需要查找第1个未使用的(i)
            start = 1
            if nodeid in repetWord:
                start = repetWord[nodeid]
            for i in range(start, 100000):  # 后缀最大为5*10^4
                postfix = '(' + str(i) + ')'
                newnode = node
                for c in postfix:
                    if c not in newnode:
                        newnode[c] = {}
                        isNew = True
                    newnode = newnode[c]
                if isNew or id(newnode) not in trieEnd:
                    trieEnd.add(id(newnode))
                    repetWord[nodeid] = i + 1
                    return word + postfix

        ans = []
        for word in names:
            ans.append(add(word))
        return ans


s = Solution()
print(s.getFolderNames(["kingston(0)", "kingston", "kingston"]))
print(s.getFolderNames(["pes", "fifa", "gta", "pes(2019)"]))
print(s.getFolderNames(["gta", "gta(1)", "gta", "avalon"]))
print(s.getFolderNames(["onepiece", "onepiece(1)", "onepiece(2)", "onepiece(3)", "onepiece"]))
print(s.getFolderNames(["wano", "wano", "wano", "wano"]))
print(s.getFolderNames(["kaido", "kaido(1)", "kaido", "kaido(1)"]))
