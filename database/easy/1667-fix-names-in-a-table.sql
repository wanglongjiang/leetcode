select user_id,concat(UPPER(substring(name,0,1)),LOWER(substring(name,1))) as name
from Users
order by user_id 