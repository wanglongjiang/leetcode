'''
不同的二叉搜索树
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？
'''
'''
思路：回溯。
二叉搜索树的根节点为node，所有的左子树节点小于node，所有的右子树节点大于node，其左右子树节点也满足这一性质。
根据这一特性，对于二叉搜索树nums[1..n]，如果第i个数为根节点，则nums[1..i-1]为左子树，nums[i+1..n]为右子树，再递归求左右子树的切分次数
时间复杂度：x， O(2^n)< x <O(n!)
空间复杂度：O(n)，最大递归深度n
'''


class Solution:
    def numTrees(self, n: int) -> int:
        def backtrack(start, end):
            treeNums = 0
            for i in range(start, end + 1):
                # 左子树或右子树的节点数大于1，树的种类大于1。以i为节点的树数量=左子树数量*右子树数量
                leftNums, rightNums = 1, 1
                if i - start > 1:
                    leftNums = backtrack(start, i - 1)
                if end - i > 1:
                    rightNums = backtrack(i + 1, end)
                treeNums += leftNums * rightNums
            return treeNums

        return backtrack(1, n)


s = Solution()
print(s.numTrees(1))
print(s.numTrees(3))
print(s.numTrees(5))
print(s.numTrees(8))
