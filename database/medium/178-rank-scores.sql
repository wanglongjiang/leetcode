select s1.Score,CONVERT(s2.rowno, SIGNED INTEGER) as `Rank`
from(
SELECT s1.Score
from scores s1
order by score desc)s1,

(select @rownum:=@rownum+1 AS rowno,s2.score
from
(SELECT score
from scores
GROUP BY score
order by score desc)s2,(SELECT @rowNum:=0) b)s2

where s1.score = s2.score
