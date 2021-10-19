'''
1169. 查询无效交易
如果出现下述两种情况，交易 可能无效：

交易金额超过 ¥1000
或者，它和另一个城市中同名的另一笔交易相隔不超过 60 分钟（包含 60 分钟整）
每个交易字符串 transactions[i] 由一些用逗号分隔的值组成，这些值分别表示交易的名称，时间（以分钟计），金额以及城市。

给你一份交易清单 transactions，返回可能无效的交易列表。你可以按任何顺序返回答案。



示例 1：

输入：transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
输出：["alice,20,800,mtv","alice,50,100,beijing"]
解释：第一笔交易是无效的，因为第二笔交易和它间隔不超过 60 分钟、名称相同且发生在不同的城市。同样，第二笔交易也是无效的。
示例 2：

输入：transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
输出：["alice,50,1200,mtv"]
示例 3：

输入：transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
输出：["bob,50,1200,mtv"]


提示：

transactions.length <= 1000
每笔交易 transactions[i] 按 "{name},{time},{amount},{city}" 的格式进行记录
每个交易名称 {name} 和城市 {city} 都由小写英文字母组成，长度在 1 到 10 之间
每个交易时间 {time} 由一些数字组成，表示一个 0 到 1000 之间的整数
每笔交易金额 {amount} 由一些数字组成，表示一个 0 到 2000 之间的整数
'''
from typing import List
from collections import defaultdict
from sortedcontainers import SortedList
'''
思路：哈希 有序集合
设哈希表hashtab，key为交易名，value为有序集合
遍历所有交易，分拆成name,time,amount,city，
如果amount>1000则该记录标记为无效记录
对于一条记录，用name作为key找到有序集合sortedList，然后将(time,index)保存到sortedList中，如果其左右2侧60分钟内的记录的城市不同，需要标记为无效记录

时间复杂度：O(nlogn)
空间复杂度：O(n)
'''


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        hashtab = defaultdict(SortedList)
        n = len(transactions)
        invalid = set()  # 保存非法的交易索引
        for i, t in enumerate(transactions):
            record = t.split(',')  # 分拆成记录
            li = hashtab[record[0]]  # hashtab中同名的交易保存为有序集合
            time = int(record[1])
            amount = int(record[2])
            if amount > 1000:  # 超过1000的是非法记录
                invalid.add(i)
            city = record[3]
            start = li.bisect_left((time - 60, 0, city))  # 有序集合二分查找时间+-60分钟内的记录
            end = li.bisect_right((time + 60, n, city))
            for j in range(start, end):
                if li[j][2] != city:  # 时间范围内，不同城市的交易为非法交易
                    invalid.add(li[j][1])
                    invalid.add(i)
            li.add((time, i, city))  # 将时间、索引、城市构成的三元组加入有序集合
        ans = []
        for i in invalid:  # 遍历所有的索引，加入
            ans.append(transactions[i])
        return ans


s = Solution()
print(s.invalidTransactions(["alice,20,800,mtv", "alice,50,100,beijing"]))
print(s.invalidTransactions(["alice,20,800,mtv", "alice,50,1200,mtv"]))
print(s.invalidTransactions(["alice,20,800,mtv", "bob,50,1200,mtv"]))
