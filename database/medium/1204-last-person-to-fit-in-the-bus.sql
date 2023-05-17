select person_name
from(
select person_name,sum(weight) over (order by turn) as weight_sum
from queue
order by turn
)t
where weight_sum<=1000
order by weight_sum desc
limit 1
