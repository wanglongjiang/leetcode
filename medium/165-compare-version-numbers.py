'''
比较版本号

给你两个版本号 version1 和 version2 ，请你比较它们。

版本号由一个或多个修订号组成，各修订号由一个 '.' 连接。每个修订号由 多位数字 组成，可能包含 前导零 。
每个版本号至少包含一个字符。修订号从左到右编号，下标从 0 开始，最左边的修订号下标为 0 ，下一个修订号下标为 1 ，以此类推。
例如，2.5.33 和 0.1 都是有效的版本号。

比较版本号时，请按从左到右的顺序依次比较它们的修订号。比较修订号时，只需比较 忽略任何前导零后的整数值 。
也就是说，修订号 1 和修订号 001 相等 。如果版本号没有指定某个下标处的修订号，则该修订号视为 0 。
例如，版本 1.0 小于版本 1.1 ，因为它们下标为 0 的修订号相同，而下标为 1 的修订号分别为 0 和 1 ，0 < 1 。

返回规则如下：

如果 version1 > version2 返回 1，
如果 version1 < version2 返回 -1，
除此之外返回 0。
'''
'''
思路：顺序读入2个字符串，从左到右依次比较.之间的部分。
'''


class Version:
    def __init__(self, s):
        self.s = s
        self.i = 0
        self.n = len(s)

    def next(self):  # 每次返回下一个修订号
        if self.isFinish():
            return 0
        j = self.i
        while j < self.n and self.s[j] != '.':
            j += 1
        num = int(self.s[self.i:j])
        if j < self.n:
            self.i = j + 1
        else:
            self.i = self.n
        return num

    def isFinish(self):
        return self.i == self.n


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1, ver2 = Version(version1), Version(version2)
        while not ver1.isFinish() or not ver2.isFinish():  # 只要有1个还未结束，需要进一步比较
            rev1, rev2 = ver1.next(), ver2.next()
            if rev1 > rev2:
                return 1
            elif rev1 < rev2:
                return -1
        return 0
