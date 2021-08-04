-- 给定 Employee 表，编写一个 SQL 查询，该查询可以获取收入超过他们经理的员工的姓名。在上面的表格中，Joe 是唯一一个收入超过他的经理的员工。
-- 思路：简单的连结
select e1.name as Employee
from Employee e1, Employee e2
where e1.managerId=e2.id and e1.salary>e2.salary
