# Write your MySQL query statement below
select r.contest_id, round(((count(r.contest_id)/(u.total_user))*100),2) percentage
from register r, (select count(user_id) total_user from users) u
group by r.contest_id
order by percentage desc, r.contest_id
