-- 如果一个国家的面积超过 300 万平方公里，或者人口超过 2500 万，那么这个国家就是大国家。
-- 编写一个 SQL 查询，输出表中所有大国家的名称、人口和面积。

-- 思路：简单2个条件
select name, population, area
from world
where area>=3000000 or population>=25000000
