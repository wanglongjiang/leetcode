SELECT
	d.NAME AS Department,
	e.NAME AS Employee,
	e.Salary AS Salary 
FROM
	department d,
	employee e,
	( SELECT departmentid, max( salary ) AS salary FROM employee GROUP BY departmentid ) ge 
WHERE
	d.id = e.DepartmentId 
	AND e.DepartmentId = ge.departmentid 
	AND e.Salary = ge.salary
    