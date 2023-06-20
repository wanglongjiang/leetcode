(SELECT u.name as results 
FROM MovieRating mr,Users u
WHERE mr.user_id=u.user_id
GROUP BY mr.user_id
order BY count(*) desc,u.name
limit 1) 
union all
(SELECT m.title as results
FROM MovieRating mr, Movies m
WHERE mr.movie_id=m.movie_id
and date_format(mr.created_at,'%Y-%m')='2020-02'
GROUP by mr.movie_id
order by sum(rating)/count(*) desc,m.title
limit 1)