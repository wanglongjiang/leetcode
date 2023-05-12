select name
from Employee e,
(select managerId 
 from Employee 
 where managerId is not null
 group by managerId
 having count(*)>=5) m
where e.id=m.managerId
