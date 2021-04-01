'''
最后 K 个数的乘积
请你实现一个「数字乘积类」ProductOfNumbers，要求支持下述两种方法：

1. add(int num)

将数字 num 添加到当前数字列表的最后面。
2. getProduct(int k)

返回当前数字列表中，最后 k 个数字的乘积。
你可以假设当前列表中始终 至少 包含 k 个数字。
题目数据保证：任何时候，任一连续数字序列的乘积都在 32-bit 整数范围内，不会溢出。
'''
'''
思路：动态规划
设数组长度为n，
设置一个从左到右的连续乘积数组products
products[i]为0..i的连续乘积。
如果products[i-1]为0，则products[i]为nums[i]
那么最后k个数字的乘积为product[n]/product[n-k]
'''


class ProductOfNumbers:
    def __init__(self):
        self.products = []

    def add(self, num: int) -> None:
        if not num:  # 遇到0，将之前的乘积全部改为0
            if self.products:
                for i in range(len(self.products)):
                    self.products[i] = 0
            self.products.append(0)
            return

        # 非0项，如果前一项不为0，为prev*num，否则为num
        prev = 0
        if self.products:
            prev = self.products[-1]
        if prev:
            self.products.append(num * prev)
        else:
            self.products.append(num)

    def getProduct(self, k: int) -> int:
        d1 = self.products[len(self.products) - k]
        d = self.products[len(self.products) - k - 1]
        if not d1:
            return 0
        if not d:
            return self.products[-1]
        return self.products[-1] // d


productOfNumbers = ProductOfNumbers()
productOfNumbers.add(3)
productOfNumbers.add(0)
productOfNumbers.add(2)
productOfNumbers.add(5)
productOfNumbers.add(4)
print(productOfNumbers.getProduct(2))
print(productOfNumbers.getProduct(3))
print(productOfNumbers.getProduct(4))
productOfNumbers.add(8)
print(productOfNumbers.getProduct(2))
