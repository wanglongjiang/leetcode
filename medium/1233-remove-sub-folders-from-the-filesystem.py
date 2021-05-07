'''
删除子文件夹

你是一位系统管理员，手里有一份文件夹列表 folder，你的任务是要删除该列表中的所有 子文件夹，并以 任意顺序 返回剩下的文件夹。

我们这样定义「子文件夹」：

如果文件夹 folder[i] 位于另一个文件夹 folder[j] 下，那么 folder[i] 就是 folder[j] 的子文件夹。
文件夹的「路径」是由一个或多个按以下格式串联形成的字符串：

/ 后跟一个或者多个小写英文字母。
例如，/leetcode 和 /leetcode/problems 都是有效的路径，而空字符串和 / 不是。

 

示例 1：

输入：folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
输出：["/a","/c/d","/c/f"]
解释："/a/b/" 是 "/a" 的子文件夹，而 "/c/d/e" 是 "/c/d" 的子文件夹。
示例 2：

输入：folder = ["/a","/a/b/c","/a/b/d"]
输出：["/a"]
解释：文件夹 "/a/b/c" 和 "/a/b/d/" 都会被删除，因为它们都是 "/a" 的子文件夹。
示例 3：

输入：folder = ["/a/b/c","/a/b/d","/a/b/ca"]
输出：["/a/b/c","/a/b/ca","/a/b/d"]
 

提示：

1 <= folder.length <= 4 * 10^4
2 <= folder[i].length <= 100
folder[i] 只包含小写字母和 /
folder[i] 总是以字符 / 起始
每个文件夹名都是唯一的
'''
from typing import List
'''
思路：字典树
1、先对folder按照长度进行排序
2、遍历folder，对于每个路径每到一个目录名，就判断是否在字典树中存在，
    如果在字典树中不存在，则继续向后搜索，直至整个路径都在字典树中不存在，加入字典树，加入结果
    如果前缀在字典树中存在，说明有父目录存在，需要跳过
时间复杂度：O(mn)，m为folder的长度，n为字符串的平均长度。排序需要O(mlogm)，查找需要O(mn)
空间复杂度：O(mn)，最坏情况下，所有路径都加入字典树
'''


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort(key=lambda s: len(s))  # 按照长度排序，确保父目录在前面进入字典树
        root = {}
        finishs = set()
        ans = []
        # 将folder中的目录依次尝试加入字典树
        for p in folder:
            node = root
            n = len(p)
            for i in range(n):
                if p[i] not in node:
                    node[p[i]] = {}
                node = node[p[i]]
                if i < n - 1 and p[i + 1] == '/':  # 如果当前字符是目录名的最后1个字母，需要判断当前目录名是否存在
                    if id(node) in finishs:  # 如果当前路径的前缀已经在字典树中存在，说明是子目录，需要跳过
                        break
            else:  # 循环没有提前退出，说明是新的路径，需要加入字典树的终点
                finishs.add(id(node))
                ans.append(p)
        return ans


s = Solution()
print(s.removeSubfolders(["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]))
print(s.removeSubfolders(["/a", "/a/b/c", "/a/b/d"]))
print(s.removeSubfolders(["/a/b/c", "/a/b/d", "/a/b/ca"]))
