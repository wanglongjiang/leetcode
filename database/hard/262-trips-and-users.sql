-- 写一段 SQL 语句查出 "2013-10-01" 至 "2013-10-03" 期间非禁止用户（乘客和司机都必须未被禁止）的取消率。
-- 非禁止用户即 Banned 为 No 的用户，禁止用户即 Banned 为 Yes 的用户。
-- 取消率 的计算方式如下：(被司机或乘客取消的非禁止用户生成的订单数量) / (非禁止用户生成的订单总数)。
-- 返回结果表中的数据可以按任意顺序组织。其中取消率 Cancellation Rate 需要四舍五入保留 两位小数 。
SELECT
	t.Request_at AS Day,
	round( sum( CASE t.`Status` WHEN 'completed' THEN 0 ELSE 1 END ) / count( * ), 2 ) AS `Cancellation Rate` 
FROM
	trips t,
	users d,
	users c 
WHERE
	t.Driver_Id = d.Users_Id 
	AND t.Client_Id = c.Users_Id 
	AND d.Banned = 'No' 
	AND c.Banned = 'No' 
    AND t.Request_at BETWEEN STR_TO_DATE('2013-10-01','%Y-%m-%d') and STR_TO_DATE('2013-10-03','%Y-%m-%d') 
GROUP BY
	t.Request_at