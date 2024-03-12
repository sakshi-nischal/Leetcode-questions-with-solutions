# Write your MySQL query statement below
SELECT P.product_name, S.year, S.price FROM Product as P, Sales as S
WHERE P.product_id = S.product_id

"""
- Displaying product_name, year, price where product_id are same.
"""
