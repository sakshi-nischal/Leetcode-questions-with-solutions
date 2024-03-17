--Approach using Case When
SELECT query_name, round(AVG(rating/position),2) as quality, 
round(AVG(CASE WHEN rating<3 THEN 1 ELSE 0 END)*100,2) as poor_query_percentage
FROM Queries
WHERE query_name is not null
GROUP BY query_name
