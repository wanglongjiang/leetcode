# 编写一个 SQL 查询，获取 Employee 表中第二高的薪水（Salary） 。
select Salary as SecondHighestSalary 
from Employee
order by Salary desc limit 1,1