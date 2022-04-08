select name,balance
from Users u,(
select u.account,sum(amount) as balance
from Users u
left join Transactions t on u.account = t.account
group by account
having sum(amount)>=10000 ) t
where u.account=t.account
