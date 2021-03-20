'''
第一个错误的版本

你是产品经理，目前正在带领一个团队开发新的产品。不幸的是，你的产品的最新版本没有通过质量检测。
由于每个版本都是基于之前的版本开发的，所以错误的版本之后的所有版本都是错的。

假设你有 n 个版本 [1, 2, ..., n]，你想找出导致之后所有版本出错的第一个错误的版本。

你可以通过调用 bool isBadVersion(version) 接口来判断版本号 version 是否在单元测试中出错。
实现一个函数来查找第一个错误的版本。你应该尽量减少对调用 API 的次数。
'''


def isBadVersion(version):
    pass


'''
思路：二分查找
    对于mid如果为true，说明错误的版本号<=mid需要在<=mid的数字中查找
    否则，需要在>mid的查找
时间复杂度：O(logn)
空间复杂度：O(1)
'''


class Solution:
    def firstBadVersion(self, n) -> int:
        start, end = 1, n
        while start <= end:
            mid = (start + end) // 2
            r = isBadVersion(mid)
            if start == end:
                return mid if r else mid + 1
            if r:
                end = mid
            else:
                start = mid + 1
