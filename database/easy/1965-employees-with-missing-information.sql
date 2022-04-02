select employee_id
from(
select e.employee_id as employee_id
from Employees e
left join Salaries s
on e.employee_id=s.employee_id
where s.salary is null
union 
select s.employee_id as employee_id
from Salaries s
left join Employees e
on e.employee_id=s.employee_id
where e.name is null
) t
order by employee_id