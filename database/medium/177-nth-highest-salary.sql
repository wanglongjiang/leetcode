CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
	DECLARE
		offst INT;
	
	SET offst := n - 1;
	RETURN ( SELECT Salary FROM Employee GROUP BY Salary ORDER BY Salary DESC LIMIT offst, 1 );
END
