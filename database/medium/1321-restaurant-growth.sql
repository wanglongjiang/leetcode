
# Write your MySQL query statement below
SELECT visited_on
,(amount+lag2+lag3+lag4+lag5+lag6+lag7) AS amount
,ROUND((amount+lag2+lag3+lag4+lag5+lag6+lag7)/7,2) AS average_amount
FROM
(SELECT visited_on
,amount
,lag(amount,1,0)OVER() AS lag2
,lag(amount,2,0)OVER() AS lag3
,lag(amount,3,0)OVER() AS lag4
,lag(amount,4,0)OVER() AS lag5
,lag(amount,5,0)OVER() AS lag6
,lag(amount,6,0)OVER() AS lag7
FROM (
  SELECT visited_on,SUM(amount) AS amount FROM Customer GROUP BY visited_on
  ) t1)t2
WHERE DATEDIFF(visited_on, (SELECT MIN(visited_on) FROM Customer)) >= 6
