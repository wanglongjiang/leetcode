-- 编写一个 SQL 查询，找出每个部门获得前三高工资的所有员工。
-- 思路：子查询的意思是与父查询员工同部门的人当中，高于该员工工资的人数要少于3个
select d.name as Department, e.name as Employee, e.Salary
from employee e, department d
where e.DepartmentId = d.Id
and (
	select count(distinct e1.Salary)
	from employee e1
	where e1.departmentid=e.DepartmentId and e1.Salary>e.Salary
)<3
order by d.id,e.Salary desc
