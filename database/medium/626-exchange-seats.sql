-- 小美是一所中学的信息科技老师，她有一张 seat 座位表，平时用来储存学生名字和与他们相对应的座位 id。
-- 其中纵列的 id 是连续递增的
-- 小美想改变相邻俩学生的座位。
-- 思路：子查询。子查询的意思是：名字取相邻id的名字。如果相邻id不存在，取自身名字。

select s1.id,ifnull((select student from seat s2 where s2.id=if(mod(s1.id,2)=1, s1.id+1, s1.id-1)), s1.student) as student
from seat s1
ORDER BY s1.id
