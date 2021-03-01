'''
简化路径
给你一个字符串 path ，表示指向某一文件或目录的 Unix 风格 绝对路径 （以 '/' 开头），请你将其转化为更加简洁的规范路径。

在 Unix 风格的文件系统中，一个点（.）表示当前目录本身；此外，两个点 （..） 表示将目录切换到上一级（指向父目录）；两者都可以是复杂相对路径的组成部分。
任意多个连续的斜杠（即，'//'）都被视为单个斜杠 '/' 。 对于此问题，任何其他格式的点（例如，'...'）均被视为文件/目录名称。

请注意，返回的 规范路径 必须遵循下述格式：

始终以斜杠 '/' 开头。
两个目录名之间必须只有一个斜杠 '/' 。
最后一个目录名（如果存在）不能 以 '/' 结尾。
此外，路径仅包含从根目录到目标文件或目录的路径上的目录（即，不含 '.' 或 '..'）。
返回简化后得到的 规范路径 。
'''
'''
思路:堆栈+贪心

'''


class Solution:
    def simplifyPath(self, path: str) -> str:
        pathStack = []
        i = 0
        n = len(path)
        while i < n:
            if path[i] == '/':
                while i < n and path[i] == '/':
                    i += 1
                if i == n:
                    break
            if path[i] == '.':
                dotStart = i
                while i < n and path[i] == '.':
                    i += 1
                if i < n and path[i] == '/':  # 前后都有斜线，且长度为1或2为相对目录，否则为文件名一部分
                    if i - dotStart == 2:
                        if len(pathStack) > 0:  # 连续2个.为上级目录
                            pathStack.pop()
                    elif i - dotStart == 1:
                        pass
                    else:
                        while i < n and path[i] != '/':
                            i += 1
                        pathStack.append(path[dotStart:i])
                else:
                    while i < n and path[i] != '/':  # .后面没有斜线，为文件名的一部分
                        i += 1
                    pathStack.append(path[dotStart:i])
                if i == n:
                    break
            if path[i] != '/':
                folderStart = i
                while i < n and path[i] != '/':
                    i += 1
                pathStack.append(path[folderStart:i])
        return '/' + '/'.join(pathStack)


s = Solution()
print(s.simplifyPath("/home/"))
print(s.simplifyPath("/../"))
print(s.simplifyPath("/home//foo/"))
print(s.simplifyPath("/a/./b/../../c/"))
