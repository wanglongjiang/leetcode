select name,ifnull(sum(distance),0) as travelled_distance 
from users u
left join Rides r on u.id=r.user_id
group by u.id
order by sum(distance) desc,name
