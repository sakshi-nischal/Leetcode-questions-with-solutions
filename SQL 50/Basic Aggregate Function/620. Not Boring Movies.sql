# Write your MySQL query statement below
select id, movie, description, rating
from cinema
where id%2 <> 0 and lower(description) <> "boring"
order by rating desc
