-- 作为该电影院的信息部主管，您需要编写一个 SQL查询，找出所有影片描述为非 boring (不无聊) 的并且 id 为奇数 的影片，结果请按等级 rating 排列。

-- 思路：简单的where条件，排序
select *
from cinema
where description <>'boring'
and mod(id,2)=1
order by rating desc
