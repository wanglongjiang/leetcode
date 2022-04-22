'''
587. 安装栅栏
在一个二维的花园中，有一些用 (x, y) 坐标表示的树。由于安装费用十分昂贵，你的任务是先用最短的绳子围起所有的树。只有当所有的树都被绳子包围时，花园才能围好栅栏。
你需要找到正好位于栅栏边界上的树的坐标。

 

示例 1:

输入: [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
输出: [[1,1],[2,0],[4,2],[3,3],[2,4]]
解释:

示例 2:

输入: [[1,2],[2,2],[4,2]]
输出: [[1,2],[2,2],[4,2]]
解释:

即使树都在一条直线上，你也需要先用绳子包围它们。
 

注意:

所有的树应当被围在一起。你不能剪断绳子来包围树或者把树分成一组以上。
输入的整数在 0 到 100 之间。
花园至少有一棵树。
所有树的坐标都是不同的。
输入的点没有顺序。输出顺序也没有要求。
'''
'''
此题为经典的求凸包的算法，详细的算法原理可以参考「凸包」。常见的凸包算法有多种，在此只描述 \texttt{Jarvis}Jarvis 算法、\texttt{Graham}Graham 算法、 \texttt{Andrew}Andrew 算法。

\texttt{Jarvis}Jarvis 算法背后的想法非常简单。首先必须要从凸包上的某一点开始，比如从给定点集中最左边的点开始，例如最左的一点 A_{1}A 
1
​
 。然后选择 A_{2}A 
2
​
  点使得所有点都在向量 \vec{A_{1}A_{2}} 
A 
1
​
 A 
2
​
 
​
 的左方或者右方，我们每次选择左方，需要比较所有点以 A_{1}A 
1
​
  为原点的极坐标角度。然后以 A_{2}A 
2
​
  为原点，重复这个步骤，依次找到 A_{3},A_{4},\ldots,A_{k}A 
3
​
 ,A 
4
​
 ,…,A 
k
​
 。
给定原点 pp，如何找到点 qq，满足其余的点 rr 均在向量 \vec{pq} 
pq
​
  的左边，我们使用「向量叉积」来进行判别。我们可以知道两个向量 \vec{pq},\vec{qr} 
pq
​
 , 
qr
​
  的叉积大于 00 时，则两个向量之间的夹角小于 180 \degree180°，两个向量之间构成的旋转方向为逆时针，此时可以知道 rr 一定在 \vec{pq} 
pq
​
  的左边；叉积等于 00 时，则表示两个向量之间平行，p,q,rp,q,r 在同一条直线上；叉积小于 00 时，则表示两个向量之间的夹角大于 180 \degree180°，两个向量之间构成的旋转方向为顺时针，此时可以知道 rr 一定在 \vec{pq} 
pq
​
  的右边。为了找到点 qq，我们使用函数 \texttt{cross}()cross() ，这个函数有 33 个参数，分别是当前凸包上的点 pp，下一个会加到凸包里的点 qq，其他点空间内的任何一个点 rr，通过计算向量 \vec{pq},\vec{qr} 
pq
​
 , 
qr
​
  的叉积来判断旋转方向，如果剩余所有的点 rr 均满足在向量 \vec{pq} 
pq
​
  的左边，则此时我们将 qq 加入凸包中。
下图说明了这样的关系，点 rr 在向量 \vec{pq} 
pq
​
  的左边。

从上图中，我们可以观察到点 pp，qq 和 rr 形成的向量相应地都是逆时针方向，向量 \vec{pq} 
pq
​
  和 \vec{qr} 
qr
​
  旋转方向为逆时针，函数 \texttt{cross}(p,q,r)cross(p,q,r) 返回值大于 00。

\begin{aligned} cross(p,q,r) &= \vec{pq} \times \vec{qr} \\ &= \begin{vmatrix} (q_x-p_x) & (q_y-p_y) \\ (r_x-q_x) & (r_y-p_y) \end{vmatrix} \\ &= (q_x-p_x) \times (r_y-p_y) - (q_y-p_y) \times (r_x-q_x) \end{aligned}
cross(p,q,r)
​
  
= 
pq
​
 × 
qr
​
 
= 
∣
∣
∣
∣
∣
​
  
(q 
x
​
 −p 
x
​
 )
(r 
x
​
 −q 
x
​
 )
​
  
(q 
y
​
 −p 
y
​
 )
(r 
y
​
 −p 
y
​
 )
​
  
∣
∣
∣
∣
∣
​
 
=(q 
x
​
 −p 
x
​
 )×(r 
y
​
 −p 
y
​
 )−(q 
y
​
 −p 
y
​
 )×(r 
x
​
 −q 
x
​
 )
​
 

我们遍历所有点 rr，找到对于点 pp 来说逆时针方向最靠外的点 qq，把它加入凸包。如果存在 22 个点相对点 pp 在同一条线上，我们应当将 qq 和 pp 同一线段上的边界点都考虑进来，此时需要进行标记，防止重复添加。

通过这样，我们不断将凸包上的点加入，直到回到了开始的点，下面的动图描述了该过程。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/erect-the-fence/solution/an-zhuang-zha-lan-by-leetcode-solution-75s3/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

from typing import List


class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def cross(p: List[int], q: List[int], r: List[int]) -> int:
            return (q[0] - p[0]) * (r[1] - q[1]) - (q[1] - p[1]) * (r[0] - q[0])

        n = len(trees)
        if n < 4:
            return trees

        leftMost = 0
        for i, tree in enumerate(trees):
            if tree[0] < trees[leftMost][0]:
                leftMost = i

        ans = []
        vis = [False] * n
        p = leftMost
        while True:
            q = (p + 1) % n
            for r, tree in enumerate(trees):
                # // 如果 r 在 pq 的右侧，则 q = r
                if cross(trees[p], trees[q], tree) < 0:
                    q = r
            # 是否存在点 i, 使得 p q i 在同一条直线上
            for i, b in enumerate(vis):
                if not b and i != p and i != q and cross(trees[p], trees[q], trees[i]) == 0:
                    ans.append(trees[i])
                    vis[i] = True
            if not vis[q]:
                ans.append(trees[q])
                vis[q] = True
            p = q
            if p == leftMost:
                break
        return ans
