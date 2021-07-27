-- 编写一个 SQL 查询以找出每行的人数大于或等于 100 且 id 连续的三行或更多行记录。
select *
from(
select t1.*
from stadium t1,stadium t2, stadium t3
where t1.people>=100 and t2.people>=100 and t3.people >=100
and t1.id =t2.id+1 and t2.id=t3.id+1
union
select t2.*
from stadium t1,stadium t2, stadium t3
where t1.people>=100 and t2.people>=100 and t3.people >=100
and t1.id =t2.id+1 and t2.id=t3.id+1
union
select t3.*
from stadium t1,stadium t2, stadium t3
where t1.people>=100 and t2.people>=100 and t3.people >=100
and t1.id =t2.id+1 and t2.id=t3.id+1
)t
order by visit_date 