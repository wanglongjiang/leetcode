'''
248. 中心对称数 III
中心对称数是指一个数字在旋转了 180 度之后看起来依旧相同的数字（或者上下颠倒地看）。

写一个函数来计算范围在 [low, high] 之间中心对称数的个数。

示例:

输入: low = "50", high = "100"
输出: 3
解释: 69，88 和 96 是三个在该范围内的中心对称数
注意:
由于范围可能很大，所以 low 和 high 都用字符串表示。
'''
'''
思路：数学
经过246、247两道题的进化，得知：
1位的中心对称数是3个
2位的中心对称数是4个
3位的中心对称数是4*3=12个
4位的中心对称数是4*5=20个
归纳得知，n位数（n>=2）：
当n为奇数=4 * 5^(n/2-1) * 3，第1部分4代表第1个数字有4种选择（0除外），第2部分5^(n/2-1)代表2..n/2每位共5种选择，第3部分3代表中间的数字有3种选择
当n为偶数=4 * 5^(n/2-1)
依据上面的算法可以算出len(low)-len(high)的所有对称数的数量。
然后需要减去小于low的对称数和大于high的对称数

TODO

时间复杂度：O(m+n)，m=low.length,n=high.length
空间复杂度：O(1)
'''


class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        def getSnum(n):  # 计算n位数的对称数数量
            if n == 1:
                return 3
            else:
                return 4 * 5**(n // 2 - 1) * (3 if n % 2 else 1)

        def getGreatSnum(num):  # 计算大于num的对称数数量
            carry = 0
            ans = 1
            n = len(num)
            if n % 2:  # 奇数位，需要处理中间的
                mid = n // 2
                if num[mid] == '0':
                    ans = 3
                elif num[mid] == '1':
                    ans = 2
                elif num[mid] <= '8':
                    ans = 1
                else:
                    ans = 3
                    carry = 1
            for i in range(n // 2 - 1, 0, -1):  # 处理1..mid之间的组合
                if num[i] == '9' and carry:
                    ans *= 5
                else:
                    newNum = int(num[i]) + (1 if carry else 0)
                    carry = 0
                    if newNum == 0:
                        if num[-(i + 1)] > '0':
                            ans *= 4
                        else:
                            ans *= 5
                    elif newNum == 1:
                        if num[-(i + 1)] > '1':
                            ans *= 3
                        else:
                            ans *= 4
                    elif newNum <= 6:
                        ans *= 3
                    elif newNum <= 8:
                        if num[-(i + 1)] > '8':
                            ans *= 1
                        else:
                            ans *= 2
                    else:
                        ans *= 1
                        if num[-(i + 1)] > '6':
                            ans *= 5
                            carry = 1
            if n > 1:  # 处理第0位
                if num[0] == '9' and carry:
                    ans = 0  # 有溢出，当前位没有大于num的对称数
                else:
                    newNum = int(num[0]) + (1 if carry else 0)
                    if newNum == 1:
                        if num[-1] > '1':
                            ans *= 3
                        else:
                            ans *= 4
                    elif newNum <= 6:
                        ans *= 3
                    elif newNum <= 8:
                        if num[-1] > '8':
                            ans *= 1
                        else:
                            ans *= 2
                    else:
                        ans *= 1
                        if num[-1] > '6':
                            ans = 0
            return ans

        ans = 0
        for i in range(len(low), len(high) + 1):
            ans += getSnum(i)
        return ans - (getSnum(len(low)) - getGreatSnum(low)) - getGreatSnum(high) + (1 if self.isStrobogrammatic(high) else 0)

    def isStrobogrammatic(self, num: str) -> bool:
        left, right = 0, len(num) - 1
        numMap = {'1': '1', '8': '8', '6': '9', '9': '6', '0': '0'}
        while left < right:
            if num[left] in numMap and num[right] != numMap[num[left]]:
                return False
            left += 1
            right -= 1
        return True if left != right else (num[left] == '0' or num[left] == '1' or num[left] == '8')


s = Solution()
print(s.strobogrammaticInRange(low="0", high="102"))
print(s.strobogrammaticInRange(low="50", high="100"))
