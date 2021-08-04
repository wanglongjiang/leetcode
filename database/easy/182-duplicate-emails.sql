-- 编写一个 SQL 查询，查找 Person 表中所有重复的电子邮箱。

-- 思路：用邮箱地址分组
select Email
from person
group by Email
having count(*)>1
