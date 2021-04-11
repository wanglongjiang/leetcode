'''

已有方法 rand7 可生成 1 到 7 范围内的均匀随机整数，试写一个方法 rand10 生成 1 到 10 范围内的均匀随机整数。

不要使用系统的 Math.random() 方法。
'''


def rand7():
    pass


class Solution:
    def rand10(self):
        r = 41
        while r > 40:
            a = rand7()
            b = rand7()
            r = a + (b - 1) * 7
        return (r - 1) % 10 + 1
