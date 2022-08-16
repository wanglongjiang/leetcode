 # 编写一个 SQL 查询，获取 Employee 表中第二高的薪水（Salary） 。
SELECT
    IFNULL(
    (SELECT DISTINCT  Salary
        FROM Employee
        ORDER BY Salary desc
        LIMIT 1 OFFSET 1),
    NULL) AS SecondHighestSalary