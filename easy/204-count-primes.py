'''
计数质数
统计所有小于非负整数 n 的质数的数量。
'''
import datetime
'''
思路：筛法 or 费马检查
思路1，暴力检测法，对于每一个奇数i，依次除以2..sqrt(i)，如果没有遇到能整除的数，则为素数。
    时间复杂度：O(n^2)
    空间复杂度：O(1)
思路2，筛法，设置一个大数组存储从2..n的所有整数，
    从2开始，将该数的整数倍下标元素设置为0（例如将4、6、8等），遇到3之后，将（6、9.。）等元素设置为0
    经过筛选之后，剩下的就是素数
    时间复杂度：O(n^2)
    空间复杂度：O(n)
思路3，使用费马检查的变形Miller-Rabin检测。费马检查是一个概率算法，有一些Carmichael数用费马检查无法检查出来，
可以用它的变形Miller-Rabin检测，这个检测的时间复杂度为O(logn)。针对每个数都检测一定次数。
    时间复杂度：O(nlogn)
    空间复杂度：O(1)
'''


class Solution:
    # 思路2，筛法
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        nums = [1] * (n + 1)
        nums[0] = 0
        nums[1] = 0
        count = 0
        for i in range(n + 1):
            if nums[i]:
                count += 1
                for j in range(2 * i, n + 1, i):  # 将素数的整数倍都清零
                    nums[j] = 0
        return count

    # 思路1，暴力检测法
    def countPrimes1(self, n: int) -> int:
        if n < 2:
            return 0

        def isPrime(num):
            sqrt = int(num**0.5)  # 求出n的平方根
            for i in range(3, sqrt + 1):
                if num % sqrt == 0:
                    return False
            return True

        count = 1
        for num in range(3, n + 1, 2):  # 从3开始，只检测奇数
            if isPrime(num):
                count += 1
        return count


s = Solution()
starttime = datetime.datetime.now()
print(s.countPrimes2(5000000))
endtime = datetime.datetime.now()
print('筛法时间：%d' % (endtime - starttime).seconds)
starttime = datetime.datetime.now()
print(s.countPrimes1(50000))
endtime = datetime.datetime.now()
print('暴力法时间：%d' % (endtime - starttime).seconds)
