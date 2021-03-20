'''
完全平方数
给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

给你一个整数 n ，返回和为 n 的完全平方数的 最少数量 。

完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。
例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。
'''
'''
思路：回溯+二分查找。
1、将<n的完全平方数输出到数组nums中。
2、在nums中回溯查找和为n的组合
'''


class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        # 计算完全平方数
        for i in range(1, n + 1):
            square = i * i
            if square <= n:
                squares.append(square)
            else:
                break
        if squares[-1] == n:
            return 1
        m = len(squares)

        # 二分查找与target相同，或仅小于target的数
        def binSearch(start, end, target):
            if end - start <= 7:
                for i in range(start, end + 1):
                    if squares[i] == target:
                        return i
                    elif squares[i] > target:
                        return i - 1
                return end
            mid = (start + end) // 2
            if squares[mid] == target:
                return mid
            elif squares[mid] > target:
                return binSearch(start, mid, target)
            else:
                return binSearch(mid, end, target)

        # 查找和为n的组合
        minNum = [float('inf')]

        def backtrack(target, comLen):
            i = binSearch(0, m - 1, target)
            if squares[i] == target:
                return comLen + 1
            if comLen == minNum[0]:
                return comLen + 1
            return backtrack(target - squares[i], comLen + 1)

        for i in range(m - 1, -1, -1):
            minNum[0] = min(minNum[0], backtrack(n - squares[i], 1))
        return minNum[0]


s = Solution()
print(s.numSquares(12))
print(s.numSquares(13))
