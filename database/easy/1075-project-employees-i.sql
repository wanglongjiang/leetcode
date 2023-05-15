SELECT
	p.project_id,
	round( sum( experience_years ) / count( p.employee_id ), 2 ) AS average_years 
FROM
	project p,
	employee e 
WHERE
	p.employee_id = e.employee_id 
GROUP BY
	p.project_id