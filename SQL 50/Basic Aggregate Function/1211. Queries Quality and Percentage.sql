--Approach using Case When
SELECT query_name, round(AVG(rating/position),2) as quality, 
round(AVG(CASE WHEN rating<3 THEN 1 ELSE 0 END)*100,2) as poor_query_percentage
FROM Queries
WHERE query_name is not null
GROUP BY query_name


-- Approach 2
select q.query_name, round(avg(q.rating/q.position),2) quality, ifnull(round((p.rating_count/count(q.rating))*100, 2),0) poor_query_percentage
from queries as q left join (select query_name, count(rating) as rating_count from queries where rating < 3 group by query_name) p
on q.query_name = p.query_name
where q.query_name is not null
group by q.query_name
