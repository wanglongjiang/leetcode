'''
在系统中查找重复文件

给定一个目录信息列表，包括目录路径，以及该目录中的所有包含内容的文件，您需要找到文件系统中的所有重复文件组的路径。
一组重复的文件至少包括二个具有完全相同内容的文件。

输入列表中的单个目录信息字符串的格式如下：

"root/d1/d2/.../dm f1.txt(f1_content) f2.txt(f2_content) ... fn.txt(fn_content)"

这意味着有 n 个文件（f1.txt, f2.txt ... fn.txt 的内容分别是 f1_content, f2_content ... fn_content）在目录 root/d1/d2/.../dm 下。
注意：n>=1 且 m>=0。如果 m=0，则表示该目录是根目录。

该输出是重复文件路径组的列表。对于每个组，它包含具有相同内容的文件的所有文件路径。文件路径是具有下列格式的字符串：

"directory_path/file_name.txt"

示例 1：

输入：
["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
输出：
[["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]
 

注：

最终输出不需要顺序。
您可以假设目录名、文件名和文件内容只有字母和数字，并且文件内容的长度在 [1，50] 的范围内。
给定的文件数量在 [1，20000] 个范围内。
您可以假设在同一目录中没有任何文件或目录共享相同的名称。
您可以假设每个给定的目录信息代表一个唯一的目录。目录路径和文件信息用一个空格分隔。

'''
from typing import List
from collections import defaultdict
'''
思路：哈希
遍历paths,以文件内容为key，文件名list为value，汇总相同内容的目录。
最后输出相同key,多个文件名的。

时间复杂度：O(nm),n为paths.length,m为paths[i]的平均长度
空间复杂度：O(nm)
'''


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for p in paths:
            i = 0
            while p[i] != ' ':
                i += 1
            folder = p[:i]
            while i < len(p):
                i += 1  # 跳过空格
                j = i
                while p[i] != '(':
                    i += 1
                fileName = p[j:i]
                i += 1  # 跳过左括号
                j = i
                while p[i] != ')':
                    i += 1
                content = p[j:i]
                hashmap[content].append(folder + '/' + fileName)
                i += 1  # 跳过右括号
        ans = []
        for li in hashmap.values():
            if len(li) > 1:
                ans.append(li)
        return ans


s = Solution()
print(s.findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]))
