--using subquery
# Write your MySQL query statement below
SELECT V.customer_id, COUNT(V.customer_id) as count_no_trans FROM Visits as V 
WHERE V.visit_id NOT IN (SELECT visit_id from Transactions)
GROUP BY V.customer_id

"""
- No of vistors visited the mall without making a transactions can be found using finding the number of visit_id that is NOT in Transactions.
- We need to do group by by customer_id to get the count of customer who came to mall without making a transaction multiple time.
"""

  --using Join
# Write your MySQL query statement below
SELECT v.customer_id,COUNT(v.visit_id) as count_no_trans
FROM Visits v
LEFT JOIN Transactions t on v.visit_id = t.visit_id 
WHERE transaction_id is null
GROUP by v.customer_id
